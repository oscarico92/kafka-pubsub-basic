# consumer_json.py
from kafka import KafkaConsumer
import json

TOPIC = "demo-json-messages"
BOOTSTRAP_SERVERS = "localhost:29092"

def create_consumer():
    """
    KafkaConsumer qui désérialise automatiquement les clés et valeurs depuis JSON.
    """
    return KafkaConsumer(
        TOPIC,
        bootstrap_servers=BOOTSTRAP_SERVERS,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="demo-consumer-json",
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        key_deserializer=lambda k: k.decode("utf-8") if k is not None else None,
    )

def main():
    consumer = create_consumer()
    print(f"[CONSUMER-JSON] Listening for JSON messages on topic '{TOPIC}'...")

    for message in consumer:
        key = message.key
        event = message.value  # c'est déjà un dict Python grâce au value_deserializer

        print(
            f"[CONSUMER-JSON] key={key} | "
            f"user={event.get('user')} | "
            f"text={event.get('text')} | "
            f"index={event.get('index')} | "
            f"ts={event.get('timestamp')}"
        )

if __name__ == "__main__":
    main()
