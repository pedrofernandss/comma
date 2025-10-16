# Comma

A serverless curation bot that sends a daily article about AI and technology via WhatsApp to help you stay updated and to stimulate your critical thinking in a simple and direct way.

### Why "Comma"?

The name "Comma" reflects the core philosophy of the project. In writing, a comma signifies a pause, not a full stop. It suggests that the story continues. This bot is built on the same idea: the pursuit of knowledge is a continuous journey, not a destination. There is always another article to read, another idea to explore, another connection to be made.

Never a period, always a comma.

---

## 🎯 About The Project

In the midst of an overwhelming volume of newsletters, blogs, and news, staying up-to-date in the tech industry is a challenge. This project was born to solve this problem by delivering a single, high-quality article per day directly to WhatsApp, a personal and high-engagement channel.

The initial version was built for Discord but failed due to low adoption, teaching a valuable lesson about the importance of User Experience (UX) and the choice of delivery channel.

## ✨ Features

* Daily, automatic execution via a Timer Trigger.
* Random selection of news sources from a configuration file.
* Database connection to prevent sending duplicate articles.
* Sends messages to multiple recipients via WhatsApp (Twilio).
* "Retry loop" logic to ensure a new article is found.

## 🛠️ Tech Stack

* **Language:** TypeScript
* **Environment:** Node.js
* **Cloud:** Azure Functions (Serverless), Azure SQL Database
* **Testing:** Jest (with a TDD approach)
* **APIs:** Twilio (WhatsApp)
* **Build Tools:** `tsc`, `tsc-alias`, `copyfiles`

## 🔮 Next Steps
* Implement a CI/CD pipeline with GitHub Actions to automate deployments
