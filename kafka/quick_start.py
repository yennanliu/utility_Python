##############################################
# V1 
##############################################
# set up consumer 
from kafka import KafkaConsumer
consumer = KafkaConsumer('my_topic', group_id= 'group1', bootstrap_servers= ['localhost:9092'])
for msg in consumer:
    print(msg)

# set up producer 
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
future = producer.send('my_topic' , key= b'my_key', value= b'my_value', partition= 0)
result = future.get(timeout= 10)
print(result)


##############################################
# V2 
##############################################
# set up consumer 
from kafka import KafkaConsumer
from kafka import TopicPartition
consumer = KafkaConsumer(group_id= 'group2', bootstrap_servers= ['localhost:9092'], consumer_timeout_ms=1000)  # deal with time out cases
consumer.assign([TopicPartition(topic= ['my_topic', 'my_topic2'], partition= 0)])  # receive multiple topics 
for msg in consumer:
    print(msg)

# set up producer 
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
future = producer.send('my_topic' , key= b'my_key', value= b'my_value', partition= 0)
result = future.get(timeout= 10)
print(result)


##############################################
# V3 
##############################################
# set up consumer 
from kafka import KafkaConsumer
import json
consumer = KafkaConsumer(group_id= 'group2', bootstrap_servers= ['localhost:9092'], value_deserializer=lambda m: json.loads(m.decode('ascii')))
consumer.subscribe(pattern= '^my.*')  # set up receive pattern 
for msg in consumer:
    print(msg)

# set up producer 
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
future = producer.send('my_topic' , key= b'my_key', value= b'my_value', partition= 0)
result = future.get(timeout= 10)
print(result)
