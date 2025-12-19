# Kafka Pub/Sub Basic System (Producer–Consumer)

## Project Overview

This project demonstrates a **basic Publish/Subscribe messaging system** using **Apache Kafka**.  
It showcases how producers can publish messages to a Kafka topic and how consumers can subscribe to and process these messages asynchronously.

The project is implemented using:
- **Kafka** (Docker-based)
- **Python producers and consumers**
- **JSON message format**
- **Kafdrop** for monitoring and visualization

This project was developed as part of the **Big Data Frameworks** course to illustrate core messaging concepts in Big Data architectures.

---

## Why Kafka?

Apache Kafka is a distributed event streaming platform designed for:
- High-throughput data ingestion
- Decoupled producer/consumer architectures
- Real-time data pipelines
- Scalability and fault tolerance

Kafka is a core building block in modern Big Data ecosystems and is widely used for log ingestion, streaming analytics, microservices communication, and IoT pipelines.

---

## Technologies Used

- Apache Kafka (Docker)
- Docker Compose
- Python 3.12
- kafka-python library
- Kafdrop (Kafka Web UI)

---

## Project Architecture

Producer → Kafka Broker → Consumer  
                     ↘  
                      Kafdrop (Monitoring UI)

Kafka acts as a buffer and decoupling layer between producers and consumers.

---

## Prerequisites

- Docker Desktop
- Python 3.10+
- Git

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd kafka-pubsub-basic
