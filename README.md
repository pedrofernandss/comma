# Comma

An enterprise-grade news curation bot designed to deliver daily technology updates to corporate communication platforms (Slack, Teams, Discord).

> **Current Status:** 🚧 *Undergoing major refactoring from Node.js/Serverless to Java/Spring Boot & Kubernetes.*

### Why "Comma"?

The name "Comma" reflects the core philosophy of the project. In writing, a comma signifies a pause, not a full stop. It suggests that the story continues. This bot is built on the same idea: the pursuit of knowledge is a continuous journey, not a destination. There is always another article to read, another idea to explore, another connection to be made.

Never a period, always a comma.

---

## 🎯 About The Project

Staying up-to-date in the tech industry is a challenge. Comma solves this by curating high-quality articles and delivering them directly to where teams work.

Originally built as a TypeScript Serverless function for WhatsApp, the project is pivoting to a robust **Java** architecture. The goal of this evolution is not just to deliver news, but to implement **strict Software Engineering standards**, focusing on Design Patterns, SOLID principles, and a modern DevOps lifecycle.

It operates as a **Cloud-Native Batch Job** (Scale-to-Zero), prioritizing cost efficiency and architectural elegance over always-on availability.

## ✨ Features 

* **Architecture:** Runs as a scheduled task (CronJob) that initializes, executes, and terminates to save resources.
* **Multi-Channel Support:** Designed with polymorphism to easily support Slack, Microsoft Teams, and Discord via Webhooks.
* **Smart Curation:** Fetches news via RSS feeds from trusted tech sources.
* **Persistency:** Uses Azure SQL Database to track history and prevent duplicate content.
* **DevOps Centric:** Fully containerized with Docker and orchestrated via Kubernetes.

## 🛠️ Tech Stack

### Core
* **Language:** Java 21 (LTS)
* **Framework:** Spring Boot 3.x (CLI Mode)
* **Build Tool:** Gradle
* **Database:** Azure SQL (via Spring Data JPA/Hibernate)

### DevOps & Infrastructure
* **Containerization:** Docker (Multi-stage builds)
* **Orchestration:** Kubernetes (CronJob resources)
* **CI/CD:** GitHub Actions (Automated testing, building, and publishing to GHCR)
* **Registry:** GitHub Container Registry

## 🧩 Key Design Patterns
To ensure maintainability and educational value, this project implements:
* **Strategy Pattern:** To handle different notification channels (Slack, Teams, etc.) interchangeably.
* **Repository Pattern:** To abstract data persistence.
* **Dependency Injection:** Managed by Spring Context.
