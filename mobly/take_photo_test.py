from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device
import time

class CameraTest(base_test.BaseTestClass):
    def setup_class(self):
        # This will run before any test method starts
        print(">>> CameraTest start")
        self.ads = self.register_controller(android_device)
        self.dut = self.ads[0]

    def test_open_camera(self):
        print(">>> Opening Camera app")
        # Launch Camera app using adb shell
        self.dut.adb.shell('am start -a android.media.action.IMAGE_CAPTURE')
        time.sleep(2)  # Give time for the camera app to open

    def test_take_photo(self):
        print(">>> Taking a photo")
        # Simulate pressing the camera shutter button
        self.dut.adb.shell('input keyevent 27')
        time.sleep(3)  # Wait for the photo to be taken and saved

    def test_save_photo(self):
        print(">>> Ensuring the Camera directory exists")
        # Ensure the Camera directory exists on the device
        #PATH = 'card \DCIM\Camera'
        self.dut.adb.shell('mkdir -p /card/DCIM/Camera')
        
        time.sleep(5)  # Wait to make sure the photo has been saved
        
        # List files in the Camera directory to confirm photo exists
        photos = self.dut.adb.shell('ls /card/DCIM/Camera').decode('utf-8')  # Decode bytes to string
        if "No such file or directory" in photos:
            print(">>> No photos found in Camera directory.")
            return
        
        # Copy the first photo found to a new file name
        self.dut.adb.shell('cp /card/DCIM/Camera/*.jpg /card/DCIM/Camera/photo_taken_1.jpg')
        time.sleep(1)  # Ensure the copy is complete
        
        # Verify the photo has been copied and saved
        result = self.dut.adb.shell('ls /card/DCIM/Camera/photo_taken_1.jpg')
        print(f"Photo saved at: {result}")
    
    def test_exit_camera(self):
        print(">>> Exiting Camera app")
        # Exit the Camera app using the back button
        self.dut.adb.shell('input keyevent 4')  # Press back button
        time.sleep(1)  # Ensure the transition happens

    def teardown_class(self):
        # This will run after all tests have finished
        print(">>> CameraTest completed")

if __name__ == '__main__':
    test_runner.main()
