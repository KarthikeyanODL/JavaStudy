import redisclient
from kafka import KafkaConsumer
import json
# To consume latest messages and auto-commit offsets

consumer = KafkaConsumer('transaction-rate','transaction-topic',group_id='my-group',
                         bootstrap_servers=['localhost:9092'])
for message in consumer:
    #print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
    #                                      message.offset, message.key,
    #                                      message.value))
    if message.topic == 'transaction-topic':
       redisclient.save_transaction(message.value)
    elif message.topic == 'transaction-rate':
       redisclient.rate_of_transaction(message.value)
    print ("%s" % message.topic)



KafkaConsumer(consumer_timeout_ms=1000)

