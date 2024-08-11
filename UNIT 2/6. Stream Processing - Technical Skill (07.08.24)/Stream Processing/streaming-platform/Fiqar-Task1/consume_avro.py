from confluent_kafka import KafkaError, KafkaException
from confluent_kafka.avro import AvroConsumer
from confluent_kafka.avro.serializer import SerializerError

def consume():
    config = {
        'bootstrap.servers': '34.101.224.54:19092',
        'group.id': 'Fiqar_DE4_consumer_group',
        'schema.registry.url': 'http://34.101.224.54:18081',
        'auto.offset.reset': 'earliest'
    }

    consumer = AvroConsumer(config)
    consumer.subscribe(['Fiqar_DE4_stock_avro_topic'])

    try:
        while True:
            try:
                message = consumer.poll(1.0)

                if message is None:
                    continue

                if message.error():
                    if message.error().code() == KafkaError._PARTITION_EOF:
                        print(f"Reached end at {message.topic()} [{message.partition()}] offset {message.offset()}")
                    else:
                        raise KafkaException(message.error())
                else:
                    value = message.value()
                    event_type = value.get("event_type")

                    if event_type == "CLICK":
                        # Handle CLICK event
                        pass
                    elif event_type == "PAGE_VIEW":
                        # Handle PAGE_VIEW event
                        pass
                    elif event_type == "PURCHASE":
                        # Handle PURCHASE event
                        pass
                    elif event_type == "USER_REGISTRATION":
                        # Handle USER_REGISTRATION event
                        pass
                    elif event_type == "LOGIN":
                        # Handle LOGIN event
                        pass
                    elif event_type == "LOGOUT":
                        # Handle LOGOUT event
                        pass

                    print(f"Consumed message from topic {message.topic()}, partition {message.partition()}, offset {message.offset()}")
                    print(f"Key: {message.key()}, Value: {value}")

            except SerializerError as e:
                print(f"Message deserialization failed: {e}")
                continue

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
        print("Consumer closed")

def main():
    consume()

if __name__ == "__main__":
    main()
