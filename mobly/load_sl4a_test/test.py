from mobly import base_test
from mobly import test_runner


"""

How load_sl4a Works:


Initialization: Calling self.load_sl4a() in your test script initializes the SL4A interface. After this, you can use the self.sl4a object to access various SL4A APIs.
SL4A Object: After loading SL4A, self.sl4a becomes available as an object that you can use to call SL4A methods.
Device Communication: Through self.sl4a, you can send commands to the Android device and receive results, such as retrieving the battery status or running shell commands.


Key Features You Can Access with SL4A

Some of the features you can access through SL4A after calling load_sl4a include:

Device Interaction: Interact with UI elements, trigger events like clicks, swipes, or typing.
Shell Commands: Execute shell commands on the device.
Sensors and Hardware: Access the device's sensors, including accelerometers, GPS, and more.
Application Control: Launch apps, interact with them, and manage them.
File System: Read/write files on the Android device.

"""

class MyTest(base_test.BaseTestClass):
    def test_sl4a_interaction(self):
        # Load SL4A on the device
        self.load_sl4a()

        # Now you can use SL4A APIs, for example:
        # Get the device's current battery level
        battery_level = self.sl4a.get_battery_level()
        self.log.info("Battery Level: %d%%" % battery_level)

        # Execute a shell command
        result = self.sl4a.shell('echo Hello, World!')
        self.log.info("Shell command result: %s" % result)

if __name__ == '__main__':
    test_runner.main()
