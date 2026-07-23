# 🧠 Intent-Based Conversation Router

A production-style AI system that classifies customer support transcripts, scores confidence, and automatically decides whether an AI agent should handle the conversation  or escalate it to a human.

Built to demonstrate the core decision layer inside enterprise AI voice and chat agent systems.

---

## 🔴 Live Demo

👉 **[Try it live](#)** ← *(replace with your Streamlit Cloud URL after deployment)*

---

## 🧩 What It Does

| Step | What Happens |
|------|-------------|
| 1 | Paste or load a customer support transcript |
| 2 | LLM classifies the intent from 7 categories |
| 3 | Confidence score is calculated (0–100%) |
| 4 | If confidence < 60% → escalate to human agent |
| 5 | On escalation → auto-generate Agent Handoff Briefing |

---

## 🎯 7 Intent Categories

- `lead_inquiry` — Customer interested in purchasing
- `billing_query` — Payment, invoice, or refund questions
- `product_complaint` — Unhappy after purchase (delayed delivery, wrong item, etc.)
- `cancellation_request` — Wants to cancel subscription or order
- `technical_issue` — Software bug, app crash, login error
- `general_inquiry` — Vague or unclassifiable question
- `escalation_request` — Explicitly asking for a human or manager

---

## 📋 Agent Handoff Briefing

When the AI is not confident enough to handle a conversation, it generates a structured briefing for the human agent taking over — so the customer never has to repeat themselves.

The briefing includes:
- **Customer Sentiment** — Angry / Frustrated / Neutral / Confused / Polite
- **Core Issue** — One-line summary of the problem
- **Key Details** — Order IDs, policy numbers, amounts mentioned
- **Urgency Level** — High / Medium / Low
- **Suggested First Action** — What the human agent should do immediately

---

## 🌐 Language Support

Handles **English**, **Hindi**, and **Hinglish** (mixed Hindi-English) — the dominant language pattern across Indian consumer support channels.

---

## 🏢 Target Verticals

Built around real use cases from Indian enterprise clients:

- 🛍️ Retail (Myntra-style)
- 💳 Fintech (Razorpay-style)
- 🏋️ Health & Fitness (Cult.fit-style)
- 🏥 Insurance (Tata AIG-style)
- 📚 EdTech (Unacademy-style)

---

## ⚙️ Tech Stack

| Layer | Tool |
|-------|------|
| LLM | LLaMA 3.3 70B via Groq API |
| Backend | Python |
| Frontend | Streamlit |
| Deployment | Streamlit Cloud |

---

## 🚀 Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/your-username/nurix-intent-router.git
cd nurix-intent-router
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your Groq API key**

Create `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "your_groq_api_key_here"
```
Get a free key at [console.groq.com](https://console.groq.com)

**4. Run**
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
nurix-intent-router/
├── app.py              # Streamlit UI
├── classifier.py       # Groq API + intent classification + handoff summary
├── examples.py         # 7 sample transcripts across verticals
├── requirements.txt
└── .streamlit/
    └── secrets.toml    # API key (not pushed to GitHub)
```

---

## 💡 Why This Project

Enterprise AI agent systems like those built by [Nurix AI](https://www.nurix.ai) need a reliable decision layer that answers one question on every conversation:

> *"Is the AI confident enough to handle this — or should a human take over?"*

This project implements that decision layer end to end, including the handoff context preservation problem — ensuring the human agent who takes over has full context without asking the customer to repeat themselves.

---

*Built by Mayank P. Savani*
