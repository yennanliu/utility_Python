# Note - setup mobly-bundled-snippets


## Cmd

```bash

git clone https://github.com/google/mobly-bundled-snippets.git

cd mobly-bundled-snippets

#-------------------
# V1
#--------------------

# build via gradle
./gradlew assembleDebug

#-------------------
# V2
#--------------------

# build via `Android stuido`
# run `/gradlew assembleDebug` cmd in gradle box in   `Android stuido`



# push to android (make sure adb setup work)
adb install -d -r -g ./build/outputs/apk/debug/mobly-bundled-snippets-debug.apk
```

## Ref
- https://github.com/google/mobly-bundled-snippets