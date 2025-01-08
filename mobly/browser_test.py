from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device
import time

class BrowserTest(base_test.BaseTestClass):
    def setup_class(self):
        # This will run before any test method starts
        print(">>> BrowserTest start")
        self.ads = self.register_controller(android_device)
        self.dut = self.ads[0]

    def test_open_browser(self):
        print(">>> Opening browser and visiting www.google.com")
        # Launch browser and visit www.google.com using adb shell
        self.dut.adb.shell('am start -a android.intent.action.VIEW -d "http://www.google.com"')
        time.sleep(5)  # Wait for the page to load

    def test_exit_browser(self):
        print(">>> Exiting browser")
        # Exit the browser using the back button (back to home screen or app list)
        self.dut.adb.shell('input keyevent 4')  # Press back button
        time.sleep(2)  # Ensure the transition happens

    def teardown_class(self):
        # This will run after all tests have finished
        print(">>> BrowserTest completed")

if __name__ == '__main__':
    test_runner.main()
