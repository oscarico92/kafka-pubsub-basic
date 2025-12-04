from kafka import KafkaConsumer

TOPIC = "demo-messages"

def main():
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers="localhost:9092",
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        value_deserializer=lambda v: v.decode("utf-8"),
        group_id="demo-consumer-group",
    )

    print("[CONSUMER] Listening for messages...")
    try:
        for message in consumer:
            print(f"[CONSUMER] Received: {message.value}")
    except KeyboardInterrupt:
        print("\n[CONSUMER] Stopped by user.")
    finally:
        consumer.close()

if __name__ == "__main__":
    main()
