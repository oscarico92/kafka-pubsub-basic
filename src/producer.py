from kafka import KafkaProducer
import time

TOPIC = "demo-messages"

def main():
    producer = KafkaProducer(
    bootstrap_servers="localhost:29092",
    value_serializer=lambda v: v.encode("utf-8"),
    )

    messages = [
        "Salut, il fait beau aujourd'hui !",
        "Message 1 from producer",
        "Message 2 from producer",
        "Au revoir, bonne journée",
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
