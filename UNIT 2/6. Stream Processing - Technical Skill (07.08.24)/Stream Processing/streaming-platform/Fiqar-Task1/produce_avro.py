import json
from uuid import uuid4
from confluent_kafka import KafkaException
from confluent_kafka.avro import AvroProducer
from confluent_kafka import avro

def delivery_callback(error, message):
    if error:
        print(f"Failed to send the message: {error}")
    else:
        print(f"Message with the key {message.key()} has been produced to the topic {message.topic()}")

def load_avro_schema_from_file():
    key_schema_string = """
    {"type": "string"}
    """
    key_schema = avro.loads(key_schema_string)
    value_schema = avro.load('/Users/tawhe/Documents/streaming-platform/Fiqar-Task1/schemas/click_event.avsc')
    return key_schema, value_schema

def produce():
    config = {
        'bootstrap.servers': "34.101.224.54:19092",
        'schema.registry.url': "http://34.101.224.54:18081"
    }

    key_schema, value_schema = load_avro_schema_from_file()

    producer = AvroProducer(
        config,
        default_key_schema=key_schema,
        default_value_schema=value_schema
    )
    
    event_types = ["CLICK", "PAGE_VIEW", "PURCHASE", "USER_REGISTRATION", "LOGIN", "LOGOUT"]
    countdata = 0

    try:
        while countdata < 2000:
            key = str(uuid4())
            event_type = event_types[countdata % len(event_types)]
            
            value = {
                "user_id": 2,
                "event_type": event_type,
                "ts": "2023-12-12",
                "page_url": "http://example.com" if event_type in ["PAGE_VIEW", "CLICK"] else None,
                "product_id": "prod123" if event_type == "PURCHASE" else None,
                "user_email": "user@example.com" if event_type == "USER_REGISTRATION" else None,
                "location": "New York" if event_type in ["LOGIN", "LOGOUT"] else None,
                "device_type": "mobile" if event_type in ["CLICK", "PAGE_VIEW"] else None
            }

            producer.produce(
                topic="Fiqar_DE4_stock_avro_topic",
                key=key,
                value=value,
                on_delivery=delivery_callback
            )
            countdata += 1
        
        producer.poll(10000)
        producer.flush()

    except KafkaException as e:
        print(f"Error occurred during message production: {e}")

    print("Done!")

def main():
    produce()

if __name__ == "__main__":
    main()
