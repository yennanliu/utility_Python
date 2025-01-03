# https://blog.csdn.net/gitblog_00091/article/details/139208861

from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device

class MyTest(base_test.BaseTestClass):
  def setup_class(self):
    # Registering android_device controller module declares the test's
    # dependency on Android device hardware. By default, we expect at least one
    # object is created from this.
    self.ads = self.register_controller(android_device)
    self.dut = self.ads[0]
    # Start Mobly Bundled Snippets (MBS).
    self.dut.load_snippet('mbs', android_device.MBS_PACKAGE)

  def test_something(self):
    self.dut.mbs.makeToast('TEST 123 !!')

if __name__ == '__main__':
  test_runner.main()