# Mobly

## Setup

```bash
# mac

pip install mobly aware
```

```bash
# linux

cd ~

sudo apt install python3-venv

python3 -m venv yen_py_env

source yen_py_env/bin/activate

pip install mobly
```

## Cmd

```bash

#-----------------------
# TEST 1
#-----------------------

python3 hello_world_test.py -c sample_config.yml


python3 test_1.py -c sample_config.yml



#-----------------------
# TEST 2
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

## Ref
- https://github.com/google/mobly/blob/master/docs/tutorial.md
- https://mobly.readthedocs.io/en/latest/index.html - Mobly pkg doc
- https://source.android.com/docs/core/tests/tradefed/testing/through-suite/multi-devices-suites?hl=zh-tw
- https://gitee.com/mirrors/Mobly/wikis/Getting-Started-with-Mobly