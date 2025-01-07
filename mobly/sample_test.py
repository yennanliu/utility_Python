import logging
import pprint

from mobly import asserts
from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device

# Number of seconds for the target to stay discoverable on Bluetooth.
DISCOVERABLE_TIME = 60


class HelloWorldTest(base_test.BaseTestClass):
    def setup_class(self):
        # Registering android_device controller module, and declaring that the test
        # requires at least two Android devices.
        self.ads = self.register_controller(android_device, min_number=2)
        # The device used to discover Bluetooth devices.
        self.discoverer = android_device.get_device(
            self.ads, label='discoverer')
        # Sets the tag that represents this device in logs.
        self.discoverer.debug_tag = 'discoverer'
        # The device that is expected to be discovered
        self.target = android_device.get_device(self.ads, label='target')
        self.target.debug_tag = 'target'
        self.target.load_snippet('mbs', android_device.MBS_PACKAGE)
        self.discoverer.load_snippet('mbs', android_device.MBS_PACKAGE)

    def setup_test(self):
        # Make sure bluetooth is on.
        self.target.mbs.btEnable()
        self.discoverer.mbs.btEnable()
        # Set Bluetooth name on target device.
        self.target.mbs.btSetName('LookForMe!')

    def test_bluetooth_discovery(self):
        target_name = self.target.mbs.btGetName()
        self.target.log.info('Become discoverable with name "%s" for %ds.',
                             target_name, DISCOVERABLE_TIME)
        self.target.mbs.btBecomeDiscoverable(DISCOVERABLE_TIME)
        self.discoverer.log.info('Looking for Bluetooth devices.')
        discovered_devices = self.discoverer.mbs.btDiscoverAndGetResults()
        self.discoverer.log.debug('Found Bluetooth devices: %s',
                                  pprint.pformat(discovered_devices, indent=2))
        discovered_names = [device['Name'] for device in discovered_devices]
        logging.info('Verifying the target is discovered by the discoverer.')
        asserts.assert_true(
            target_name in discovered_names,
            'Failed to discover the target device %s over Bluetooth.' %
            target_name)

    def teardown_test(self):
        # Turn Bluetooth off on both devices after test finishes.
        self.target.mbs.btDisable()
        self.discoverer.mbs.btDisable()


if __name__ == '__main__':
    test_runner.main()
