from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device

class HelloWorldTest(base_test.BaseTestClass):
  def setup_class(self):


    print(">>> HelloWorldTest start")
    
    # Registering android_device controller module declares the test's
    # dependency on Android device hardware. By default, we expect at least one
    # object is created from this.
    print(">>> android_device = " + str(android_device))
    self.ads = self.register_controller(android_device)
    self.dut = self.ads[0]
    print(">>> self.ads  = " + str(self.ads))
    print(">>> self.dut  = " + str(self.dut))
    # Start Mobly Bundled Snippets (MBS).
    self.dut.load_snippet('mbs', android_device.MBS_PACKAGE)

  def test_hello(self):
    self.dut.mbs.makeToast('Hello World!')

if __name__ == '__main__':
  test_runner.main()