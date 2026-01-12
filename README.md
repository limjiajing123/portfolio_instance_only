🚀 Jia Jing’s Full-Stack Portfolio Website
AI-Powered • Dockerized • CI/CD Automated • AWS Deployed
<div align="center">

🔹 React Frontend
🔹 Node.js Express Backend
🔹 AI Chatbot (OpenRouter)
🔹 Redis Caching
🔹 AWS EC2 + ECS-style Deployment
🔹 Docker Compose Architecture
🔹 GitHub Actions CI/CD + Monitoring
🔹 Discord Alerts for Production Failures

</div>
🌐 Live Website

👉 https://www.limjiajing.com

This is the production version of my personal portfolio website, fully deployed on AWS and backed by a smart AI assistant with caching, monitoring, and automated health checks.

🧩 Project Overview

This project is a full-stack, production-ready portfolio system that includes:

⚛️ React frontend served by Nginx

🟩 Node.js backend API

🤖 AI-powered chatbot (OpenRouter → DeepSeek/Grok models)

🧠 Redis cache layer

🐳 Dockerized microservice architecture

☁️ EC2-based deployment (via script & GitHub Actions)

🔄 Automated CI/CD (preprod → main auto-merge + deploy)

🚨 Health monitoring & Discord alert system

🧪 Preproduction smoke testing (pytest + Docker Compose)

🛠️ Tech Stack
Frontend

React

Styled Components

Axios

Nginx (serving build output)

Backend

Node.js

Express

OpenRouter API

Redis (Upstash in production)

DevOps / Infra

Docker

Docker Compose

AWS EC2

AWS ECR

GitHub Actions

Reverse proxy architecture

Secure environment variables & secrets

Monitoring

Discord Alerts

GitHub Actions scheduled health checks

Error notification system built directly into backend

🧱 Project Architecture
1️⃣ High-Level System Architecture
2️⃣ Docker + AWS Deployment Architecture
3️⃣ AI Chatbot Request Flow
📁 Folder Structure

A clean, readable, professional folder visualization.

📦 portfolio_instance_only
│
├── 📁 backend
│   ├── server.js
│   ├── redis.js
│   ├── discordAlertApiFail.js
│   ├── axiosMock.js
│   ├── portfolioKnowledge.js
│   ├── package.json
│   ├── package-lock.json
│   └── Dockerfile
│
├── 📁 frontend
│   ├── public
│   │   ├── index.html
│   │   ├── favicon.ico
│   │   └── robots.txt
│   │
│   ├── src
│   │   ├── components/
│   │   │   ├── Chatbot/
│   │   │   └── UI/
│   │   ├── pages/
│   │   │   ├── Home.js
│   │   │   └── About.js
│   │   ├── hooks/
│   │   ├── App.js
│   │   └── index.js
│   │
│   ├── package.json
│   ├── package-lock.json
│   └── Dockerfile
│
├── 📁 tests
│   ├── smoke_test.py
│   ├── test_backend.py
│   └── test_frontend.py
│
├── docker-compose.yml
├── docker-compose.preprod.yml
├── deploy.sh
├── open-router-monitor.yml
└── README.md

🧠 AI Chatbot Logic Explained
User Message
    ↓
Frontend (React)
    ↓
Backend (/api/chat)
    ↓
Redis Cache
    ├── Cache Hit → return instantly
    └── Cache Miss → call OpenRouter AI
                          ↓
                     Save to Redis
                          ↓
                      Return to user


✔ Caching reduces OpenRouter cost
✔ Faster repeated responses
✔ Discord alert triggers if API fails

⚙️ CI/CD Pipeline

Automated using GitHub Actions:

1️⃣ Preproduction branch (testing stage)

Build frontend & backend

Start services via Docker Compose

Run Python smoke tests

Mock AI responses

If all good → auto-trigger deploy job

2️⃣ Auto-merge preproduction → main

GitHub Actions merges branches

Commits tagged with [skip ci] to avoid loops

3️⃣ Deployment to EC2

Build Docker images

Push to ECR

SSH into EC2

Run deploy.sh (pull & restart containers)

4️⃣ Post-deploy health checks

Frontend load check

Backend health endpoint

Discord success/failure notification

🚨 Monitoring & Alerts
Backend error alerts (Discord)

If /api/chat fails → instant Discord message:

Timestamp

User message

Error status

Error details

Cooldown to prevent spam

Scheduled OpenRouter Monitoring

Every 30 minutes:

GitHub Actions pings OpenRouter

If unhealthy → Discord alert

🐳 Docker Development
Start everything locally:
docker-compose up --build

Preproduction environment:
NODE_ENV=test docker-compose -f docker-compose.preprod.yml up --build


Frontend → http://localhost:82


Backend → http://localhost:5000


Redis → redis://localhost:6379

☁️ Deployment Script (deploy.sh)

The EC2 instance:

Logs into ECR

Pulls fresh images

Rebuilds Redis, backend, frontend containers

Automatically restarts everything

No downtime. Fully automated.

🔒 Environment Variables
Backend:
REDIS_PORT=6379
NODE_ENV=production

Frontend:

None required.

📦 Install (Local Development)
git clone https://github.com/limjiajing123/portfolio_instance_only.git
cd portfolio_instance_only
docker-compose up --build

🎨 Screenshots / Demo (Optional)

(Add your own images here if you want visual showcase.)

🙌 Creator

Built entirely by Jia Jing
🔗 https://www.limjiajing.com

Skills demonstrated:

Full-stack engineering

DevOps + AWS Infrastructure

CI/CD orchestration

AI integration

Docker & service networking

Monitoring & alerting

Testing automation

⭐ If you like this project…

Feel free to:

🌟 Star the repo
🤝 Contact me for opportunities
💬 Ask questions
📧 Connect via email