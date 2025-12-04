# kafka-pubsub-basic

## Project Overview

This project demonstrates a basic Publish/Subscribe messaging system using Apache Kafka, running entirely in Docker.
A Python producer publishes messages to a Kafka topic, while a consumer listens and processes them in real-time.

This project is part of the Big Data Frameworks coursework and aims to illustrate the core idea of distributed streaming systems.

## Why Kafka ?

Apache Kafka is one of the most widely used distributed streaming platforms.
I selected it because:

- It is the standard for real-time message streaming.

- It is easy to deploy using Docker.

- It implements a simple but powerful Pub/Sub model.

- It is used everywhere: microservices, IoT, real-time analytics, event-driven architectures.

This project recreates a minimal version of that ecosystem.


┌──────────┐     SENDS MESSAGES     ┌──────────┐
│ Producer │ ─────────────────────▶ │  Kafka   │
└──────────┘                        │  Broker  │
                                    └──────────┘
                                             │
                                             │ STREAMS MESSAGES
                                             ▼
                                    ┌────────────┐
                                    │  Consumer  │
                                    └────────────┘

## Installation & Setup

### 1) Clone the Repository
git clone
cd kafka-pubsub-basic  

### 2) Start Kafka & Zookeeper with Docker
Your docker-compose.yml automatically starts the required services:
docker compose up -d
Verify containers:
docker ps
Expected result:
kafka    Running
zookeeper Running

### 3) Install Python Dependencies
pip install kafka-python

## Usage
### Start the Consumer (listens for messages)
python consumer.py
Expected output:
[CONSUMER] Listening for messages...

### Start the Producer (sends messages)
python producer.py

Expected output:
[PRODUCER] Sending: Hello Kafka!
[PRODUCER] Sending: Message 1 from producer
[PRODUCER] Sending: Message 2 from producer
[PRODUCER] Sending: Last message, bye 👋

## What Happens Next?

The consumer receives everything in real-time:
[CONSUMER] Received: Hello Kafka!
[CONSUMER] Received: Message 1 from producer
[CONSUMER] Received: Message 2 from producer
[CONSUMER] Received: Last message, bye 👋

## Screenshots (Proof of Execution)

## Folder Structure

kafka-pubsub-basic/
│
├── docker-compose.yml
├── producer.py
├── consumer.py
├── README.md
└── media/
    ├── producer.png
    └── consumer.png


## My Setup Notes (Troubleshooting & Learnings)

