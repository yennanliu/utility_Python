# go to the server & directory you wanna share files from
# example : cd KafkaHelloWorld
# python 3
python -m http.server 18888

# python 2
# https://stackoverflow.com/questions/24444343/no-module-named-http-server/43939794
python -m SimpleHTTPServer 18888

# open the other terminal, and get the file via below
# example 1 : wget localhost:18888/build.sbt
# example 2 : wget <hostname>:18888/xxx.keytab
wget <server_ip>:18888/<file_you_wanna_get>
