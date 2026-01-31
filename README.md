# Comma

A serverless curation bot that sends a daily article about AI and technology to help you stay updated and to stimulate your critical thinking in a simple and direct way.

### Why "Comma"?

The name "Comma" reflects the core philosophy of the project. In writing, a comma signifies a pause, not a full stop. It suggests that the story continues. This bot is built on the same idea: the pursuit of knowledge is a continuous journey, not a destination. There is always another article to read, another idea to explore, another connection to be made.

Never a period, always a comma.

---

## 🎯 About The Project

In the midst of an overwhelming volume of newsletters, blogs, and news, and other countless sources staying up-to-date in the tech industry is a challenge. This project was born to solve this problem by delivering each day one carefully selected piece directly to the user, ensuring relevance without overwhelming volume.

To make the content even more accessible, the bot uses Large Language Models (LLMs) to generate concise summaries of the articles, helping readers grasp the essence quickly while still encouraging deeper exploration.

The initial version failed due to low adoption, teaching a valuable lesson about the importance of User Experience (UX). Today, the focus is on providing a seamless and engaging experience across platforms.

## Features

* Daily, automatic execution via a Timer Trigger.
* Random selection of news sources from a configuration file.
* Database connection to prevent sending duplicate articles.
* Sends messages across multiple platforms such as WhatsApp (Twilio), Discord, and Telegram.
* "Retry loop" logic to ensure a new article is found.

## Tech Stack

* **Language:** Java
* **Frameworks:** Spring, and Spring AI
* **AI/LLM:** Groq
* **Build & Deploy:** Gradle, Docker
* **Cloud:** Azure
* **Integration:** Discord, WhatsApp (Twilio)

## 🔮 Next Steps
* Implement a CI/CD pipeline with GitHub Actions to automate deployments
* Expand observability with LangSmith for prompt debugging and evaluation
