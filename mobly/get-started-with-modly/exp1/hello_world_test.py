from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device

class HelloWorldTest(base_test.BaseTestClass):

  def setup_class(self):
    # Registering android_device controller module declares the test's
    # dependency on Android device hardware. By default, we expect at least one
    # object is created from this.
    self.ads = self.register_controller(android_device)
    self.dut = self.ads[0]
    self.dut.load_sl4a() # starts sl4a.

  def test_hello(self):
    self.dut.sl4a.makeToast('Hello World!')

if __name__ == "__main__":
  test_runner.main()