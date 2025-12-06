# producer_json.py
from kafka import KafkaProducer
import json
import time
import uuid
import random

TOPIC = "demo-json-messages"
BOOTSTRAP_SERVERS = "localhost:29092"

def create_producer():
    """
    KafkaProducer qui sérialise automatiquement les valeurs en JSON.
    """
    return KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        key_serializer=lambda k: k.encode("utf-8") if k is not None else None,
    )

def main():
    producer = create_producer()

    users = ["Oscar", "Alice", "Bob"]
    messages = [
        "Hello Kafka with JSON!",
        "This is a JSON event",
        "Last JSON message, bye 👋",
    ]

    for i, text in enumerate(messages, start=1):
        event = {
            "event_id": str(uuid.uuid4()),
            "type": "chat_message",
            "user": random.choice(users),
            "text": text,
            "index": i,
            "timestamp": time.time(),
        }

        key = event["user"]  # clé = nom de l'utilisateur (pour le partitionnement)

        print(f"[PRODUCER-JSON] Sending (key={key}): {event}")
        producer.send(TOPIC, key=key, value=event)

        time.sleep(0.5)

    producer.flush()
    print("[PRODUCER-JSON] Done.")

if __name__ == "__main__":
    main()
