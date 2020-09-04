# go to the server & directory you wanna share files from
# for axample 
# cd KafkaHelloWorld
python -m http.server 18888

# open the other terminal, and get the file via below
# wget localhost:18888/build.sbt
wget <server_ip>:18888/<file_you_wanna_get>