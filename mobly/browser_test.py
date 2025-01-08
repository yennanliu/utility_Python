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

        #self.dut.adb.shell('am start -a android.intent.action.VIEW -d "http://www.github.com"')
        time.sleep(5)  # Wait for the page to load
        self.search_github()


    def search_github(self):
        print(">>> Searching for 'github' on Google")

        # Focus on the search bar: tapping on the search bar (coordinates need to be accurate
        # ABS_MT_POSITION_X : 00001725
        # ABS_MT_POSITION_Y:  000014ab

        #self.dut.adb.shell('input tap 540 160')  # Coordinates for the Google search bar (adjust as needed)
        self.dut.adb.shell('input tap 5941 5291')

        time.sleep(1)  # Give it some time to focus

        # Simulate typing 'github' into the search box
        self.dut.adb.shell('input text "github"')
        time.sleep(1)  # Allow time for the text to be typed in

        # Simulate pressing the search button (Enter key)
        self.dut.adb.shell('input keyevent 66')  # Enter key (search)
        time.sleep(3)  # Wait for the search results to load

    def test_click_first_result(self):
        print(">>> Clicking the first search result for GitHub")
        # Simulate clicking the first result (coordinates of the first result)
        # Coordinates for first result can be different based on your device or screen resolution,
        # you may need to adjust it based on your test device's screen size.
        self.dut.adb.shell('input tap 540 960')  # Example coordinates for tapping on the first result
        time.sleep(5)  # Wait for the page to load

    def test_exit_browser(self):
        print(">>> Exiting browser")
        # Exit the browser using the back button (back to home screen or app list)
        self.dut.adb.shell('input keyevent 4')  # Press back button
        time.sleep(1)  # Ensure the transition happens

    def teardown_class(self):
        # This will run after all tests have finished
        print(">>> BrowserTest completed")

if __name__ == '__main__':
    test_runner.main()
