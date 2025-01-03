# Mobly

## Setup

```bash
# mac

pip install mobly aware
```

```bash
# linux

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

cd android_integ_test

atest CtsWifiAwareTestCases
```


## Ref
- https://github.com/google/mobly/blob/master/docs/tutorial.md
- https://source.android.com/docs/core/tests/tradefed/testing/through-suite/multi-devices-suites?hl=zh-tw
