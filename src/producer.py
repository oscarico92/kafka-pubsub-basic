from kafka import KafkaProducer
import time

TOPIC = "demo-messages"

def main():
    producer = KafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda v: v.encode("utf-8"),
    )

    messages = [
        "Hello Kafka!",
        "Message 1 from producer",
        "Message 2 from producer",
        "Last message, bye 👋",
    ]

    for msg in messages:
        print(f"[PRODUCER] Sending: {msg}")
        producer.send(TOPIC, msg)
        producer.flush()
        time.sleep(1)

    print("[PRODUCER] Done.")
    producer.close()

if __name__ == "__main__":
    main()
