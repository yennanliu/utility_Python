# Mobly

## Setup

```bash
# mac

pip install mobly aware
```

```bash
# install mobly

cd ~

sudo apt install python3-venv

python3 -m venv yen_py_env

source yen_py_env/bin/activate

pip install mobly
```


```bash

# install adb

sudo apt update

sudo apt install adb

# validate

adb

# get connected devices
adb devices
```

## Cmd

```bash

# https://github.com/google/mobly/blob/master/docs/tutorial.md

cd ~ && source yen_py_env/bin/activate


#-----------------------
# TEST 1
#-----------------------

python3 hello_world_test.py -c sample_config.yml

#-----------------------
# TEST 2
#-----------------------

# should see words popup at device monitor
python3 hello_world_test_2.py -c sample_config.yml

python3 hello_world_test_2.py -c sample_config.yml --test_case test_bye test_hello test_bye

python3 hello_world_test_2.py -c sample_config_2.yml --test_bed AbcTestBed


#-----------------------
# TEST 3
#-----------------------

python3 sample_test.py -c sample_config_3.yml


#-----------------------
# TEST 4
#-----------------------

python3 many_greetings_test.py -c sample_config.yml


#-----------------------
# TEST 5
#-----------------------

python3 open_setting_test.py  -c sample_config.yml


#-----------------------
# TEST 6
#-----------------------

python3 take_photo_test.py -c sample_config.yml


#-----------------------
# TEST 7
#-----------------------

python3 browser_test.py -c sample_config.yml


#-----------------------
# TEST ?
#-----------------------

python3 instrumentation_test.py -c sample_config.yml
```


## Glossary

-  1) `SL4A` (Scripting Layer for Android)
	- provides a runtime environment to run Python, Perl, Lua, and other scripts on Android devices. It exposes Android's Java APIs to these languages, allowing you to write powerful automation scripts for Android without needing to use Java.
	- When you use load_sl4a, it makes SL4A’s functionality available in your Mobly test scripts. It simplifies the process of working with Android devices, as you can directly control the device and access its features using the Python scripting language in Mobly.
	- features:
		- Access to Android’s Java-based APIs (e.g., managing applications, sending intents, controlling Wi-Fi, etc.).
		- Ability to automate and interact with Android device features using simple scripts.
		- Integration with the Android Debug Bridge (ADB) for device control.
	- Typical Use Cases for load_sl4a
		- Interacting with the device: You can interact with Android apps, simulate UI events, or control device settings.
		- Running shell commands: SL4A allows you to send shell commands to the device, useful for operations like checking device status, installing/uninstalling apps, etc.
		- Automated testing: It enables you to create test automation scripts that interface with Android devices directly via high-level scripting languages.

- 2) Android Debug Bridge (`ADB`)
	-  a versatile command-line tool that enables communication between a computer and an Android device (either physical or virtual). It is a fundamental part of the Android development environment and is used by developers, testers, and automation frameworks to manage and interact with Android devices. ADB allows you to perform a wide variety of tasks, including debugging, installing apps, and interacting with the device’s operating system and hardware.
	- https://developer.android.com/tools/adb?hl=zh-tw#:~:text=Android%20Debug%20Bridge%20(%20adb%20)%20is,you%20communicate%20with%20a%20device.

	- Key Features of ADB:
		- Device Communication: ADB facilitates communication between the development machine (like your computer) and the Android device (such as a smartphone, tablet, or emulator).
		- Debugging: It helps developers debug Android applications by enabling features like log capture, debugging remote processes, and controlling device behavior.
		- File Management: You can transfer files between your computer and Android devices, install APKs, and manage the file system.
		- Shell Access: ADB allows access to the Android device’s command shell, enabling you to run system commands directly on the device.
		- App Installation and Management: ADB is used to install, uninstall, and manage Android apps from the command line, which is essential for automation and testing.

- 3) `application.apk`
	- In Mobly, an application.apk typically refers to the Android application package (APK) file that is used in the automation testing process. The APK file is the package format used by Android to distribute and install applications. It contains all the necessary resources, assets, and code (compiled in .dex files) for an Android app to run.
	- When performing automated testing using Mobly, you often need to interact with or test specific Android applications. The application.apk is the actual Android app file that you may install, launch, and interact with during the test.
	- usage
		- install the app
		- test automation
		- interaction with the app


- 4) `Android Instrumentation` 
	- a framework provided by the Android operating system that allows developers to perform automated testing of Android applications. It provides a way to execute code in the context of an Android application and interact with its components, such as Activities, Services, Broadcast Receivers, and other parts of the app. Instrumentation enables developers and testers to run tests that interact with the app’s UI, check for specific behaviors, and verify the app's functionality under various conditions.
 
- 5) `am start`
	- The am start command is used in Android's `Android Debug Bridge (ADB)` to start an Activity on an Android device. It's part of the Android Activity Manager (am) tool, which allows you to interact with the system and launch apps, activities, or services from the command line.

- 6) `ADB` (Andriod Debug Bridge)
- 7) `AM` (Android Activity Manager)




## QA

- 1) Difference between `Android Instrumentation` and `Mobly` ?
	- `Android Instrumentation` is ideal for testing individual apps and UI interactions at the app level.
	- `Mobly`, on the other hand, is designed for more complex scenarios, such as end-to-end testing across multiple devices and device management, making it more suitable for large-scale testing environments.


## Ref
- https://github.com/google/mobly/blob/master/docs/tutorial.md
- https://mobly.readthedocs.io/en/latest/index.html - Mobly pkg doc
- https://source.android.com/docs/core/tests/tradefed/testing/through-suite/multi-devices-suites?hl=zh-tw
- https://gitee.com/mirrors/Mobly/wikis/Getting-Started-with-Mobly