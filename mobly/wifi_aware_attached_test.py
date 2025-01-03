#  Copyright (C) 2024 The Android Open Source Project
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

# https://source.android.com/docs/core/tests/tradefed/testing/through-suite/multi-devices-suites?hl=zh-tw

# Lint as: python3
"""ACTS Wi-Fi Aware Attached test reimplemented in Mobly."""
import sys

from aware import aware_lib_utils as autils
from aware import constants
from mobly import asserts
from mobly import base_test
from mobly import records
from mobly import test_runner
from mobly import utils
from mobly.controllers import android_device


RUNTIME_PERMISSIONS = (
    'android.permission.ACCESS_FINE_LOCATION',
    'android.permission.ACCESS_COARSE_LOCATION',
    'android.permission.NEARBY_WIFI_DEVICES',
)
PACKAGE_NAME = constants.WIFI_AWARE_SNIPPET_PACKAGE_NAME


class WifiAwareAttachTest(base_test.BaseTestClass):
  """Wi-Fi Aware Attach test class."""

  ads: list[android_device.AndroidDevice]

  def setup_class(self):
    # Register two Android devices.
    self.ads = self.register_controller(android_device, min_number=1)

    def setup_device(device: android_device.AndroidDevice):
      device.load_snippet('wifi_aware_snippet', PACKAGE_NAME)
      for permission in RUNTIME_PERMISSIONS:
        device.adb.shell(['pm', 'grant', PACKAGE_NAME, permission])
      asserts.abort_all_if(
          not device.wifi_aware_snippet.wifiAwareIsAvailable(),
          f'{device} Wi-Fi Aware is not available.',
      )

    # Set up devices in parallel.
    utils.concurrent_exec(
        setup_device,
        param_list=[[ad] for ad in self.ads],
        max_workers=1,
        raise_on_exception=True,
    )

  def setup_test(self):
    for ad in self.ads:
      autils.control_wifi(ad, True)
      aware_avail = ad.wifi_aware_snippet.wifiAwareIsAvailable()
      if not aware_avail:
        ad.log.info('Aware not available. Waiting ...')
        state_handler = ad.wifi_aware_snippet.wifiAwareMonitorStateChange()
        state_handler.waitAndGet(constants.WifiAwareBroadcast.WIFI_AWARE_AVAILABLE)

  def teardown_test(self):
    utils.concurrent_exec(
        self._teardown_test_on_device,
        param_list=[[ad] for ad in self.ads],
        max_workers=1,
        raise_on_exception=True,
    )
    utils.concurrent_exec(
        lambda d: d.services.create_output_excerpts_all(self.current_test_info),
        param_list=[[ad] for ad in self.ads],
        raise_on_exception=True,
    )

  def _teardown_test_on_device(self, ad: android_device.AndroidDevice) -> None:
    ad.wifi_aware_snippet.wifiAwareCloseAllWifiAwareSession()
    ad.wifi_aware_snippet.wifiAwareMonitorStopStateChange()
    autils.set_airplane_mode(ad, False)
    autils.control_wifi(ad, True)

  def on_fail(self, record: records.TestResult) -> None:
    android_device.take_bug_reports(
        self.ads, destination=self.current_test_info.output_path
    )

  def test_attach(self) -> None:
    """Basic attaching request.

    Validates that attaching to the Wi-Fi Aware service works
    without IdentityChanged callback.
    """
    dut = self.ads[0]
    handler = dut.wifi_aware_snippet.wifiAwareAttached(False)
    handler.waitAndGet(constants.AttachCallBackMethodType.ATTACHED)
    autils.callback_no_response(
        handler, constants.AttachCallBackMethodType.ID_CHANGED
    )

  def test_attach_with_identity(self) -> None:
    """Basic attaching request with extra callback.

    Validates that attaching to the Wi-Fi Aware service works
    with IdentityChanged callback.
    """
    dut = self.ads[0]
    handler = dut.wifi_aware_snippet.wifiAwareAttached(True)
    handler.waitAndGet(constants.AttachCallBackMethodType.ATTACHED)
    handler.waitAndGet(constants.AttachCallBackMethodType.ID_CHANGED)

  def test_attach_multiple_sessions(self):
    """Multiple attaching request.

    Validates that attaching to the Wi-Fi Aware service works with
    multiple request at same time.
    """
    dut = self.ads[0]
    handler_1 = dut.wifi_aware_snippet.wifiAwareAttached(False)
    handler_2 = dut.wifi_aware_snippet.wifiAwareAttached(True)
    handler_3 = dut.wifi_aware_snippet.wifiAwareAttached(False)
    handler_1.waitAndGet(constants.AttachCallBackMethodType.ATTACHED)
    autils.callback_no_response(
        handler_1, constants.AttachCallBackMethodType.ID_CHANGED, 10, True
    )
    handler_2.waitAndGet(constants.AttachCallBackMethodType.ATTACHED)
    handler_2.waitAndGet(constants.AttachCallBackMethodType.ID_CHANGED)
    handler_3.waitAndGet(constants.AttachCallBackMethodType.ATTACHED)
    autils.callback_no_response(
        handler_3, constants.AttachCallBackMethodType.ID_CHANGED, 10, True
    )

  def test_attach_with_no_wifi(self):
    """WiFi Aware attempt to attach with wifi off.

    Validates that if trying to attach with Wi-Fi disabled will receive
    the expected failure callback. As a side-effect also validates that the
    broadcast for Aware unavailable is received.
    """
    dut = self.ads[0]
    state_handler = dut.wifi_aware_snippet.wifiAwareMonitorStateChange()
    autils.control_wifi(dut, False)
    state_handler.waitAndGet(constants.WifiAwareBroadcast.WIFI_AWARE_NOT_AVAILABLE)
    attach_callback = dut.wifi_aware_snippet.wifiAwareAttached(True)
    attach_callback.waitAndGet(constants.AttachCallBackMethodType.ATTACH_FAILED)
    dut.wifi_aware_snippet.wifiAwareMonitorStopStateChange()

  def test_attach_with_location_off(self):
    """Function/Attach test cases/attempt to attach with location mode off.

    Validates that if trying to attach with device location mode off will
    receive the expected failure callback. As a side-effect also validates
    that the broadcast for Aware unavailable is received.
    """
    dut = self.ads[0]
    asserts.skip_if(
        autils.check_android_os_version(
            dut, constants.Operator.GREATER_EQUAL, constants.AndroidVersion.T
        ),
        'From T build Aware will not be disabled due to location off',
    )
    state_handler = dut.wifi_aware_snippet.wifiAwareMonitorStateChange()
    dut.adb.shell('settings put secure location_mode 0')
    state_handler.waitAndGet(constants.WifiAwareBroadcast.WIFI_AWARE_NOT_AVAILABLE)
    attach_callback = dut.wifi_aware_snippet.wifiAwareAttached(True)
    attach_callback.waitAndGet(constants.AttachCallBackMethodType.ATTACH_FAILED)
    dut.adb.shell('settings put secure location_mode 3')
    state_handler.waitAndGet(constants.WifiAwareBroadcast.WIFI_AWARE_AVAILABLE)
    dut.wifi_aware_snippet.wifiAwareMonitorStopStateChange()

  def test_attach_apm_toggle_attach_again(self):
    """Function/Attach test cases/attempt to attach with airplane mode on.

    Validates that enabling Airplane mode while Aware is on resets it
    correctly, and allows it to be re-enabled when Airplane mode is then
    disabled.
    """
    dut = self.ads[0]
    asserts.skip_if(
        not dut.is_adb_root,
        'APM toggle needs Android device(s) with root permission',
    )
    state_handler = dut.wifi_aware_snippet.wifiAwareMonitorStateChange()
    attach_callback = dut.wifi_aware_snippet.wifiAwareAttached(True)
    attach_callback.waitAndGet(constants.AttachCallBackMethodType.ATTACHED)
    autils.set_airplane_mode(dut, True)
    if autils.check_android_os_version(
        dut, constants.Operator.GREATER_EQUAL, constants.AndroidVersion.T
    ):
      if not autils._check_wifi_status(dut):
        return
      else:
        autils.control_wifi(dut, False)
    autils.callback_no_response(
        state_handler,
        constants.WifiAwareBroadcast.WIFI_AWARE_AVAILABLE,
        10,
        True,)
    state_handler.waitAndGet(constants.WifiAwareBroadcast.WIFI_AWARE_NOT_AVAILABLE)
    autils.set_airplane_mode(dut, False)
    state_handler.waitAndGet(constants.WifiAwareBroadcast.WIFI_AWARE_AVAILABLE)
    attach_callback = dut.wifi_aware_snippet.wifiAwareAttached(True)
    attach_callback.waitAndGet(constants.AttachCallBackMethodType.ATTACHED)
    dut.wifi_aware_snippet.wifiAwareMonitorStopStateChange()


if __name__ == '__main__':
  # Take test args
  if '--' in sys.argv:
    index = sys.argv.index('--')
    sys.argv = sys.argv[:1] + sys.argv[index + 1 :]

  test_runner.main()