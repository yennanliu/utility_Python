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

-  `SL4A` (Scripting Layer for Android)
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

## Ref
- https://github.com/google/mobly/blob/master/docs/tutorial.md
- https://source.android.com/docs/core/tests/tradefed/testing/through-suite/multi-devices-suites?hl=zh-tw
- https://gitee.com/mirrors/Mobly/wikis/Getting-Started-with-Mobly