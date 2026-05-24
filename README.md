# AI-Powered Portfolio Chatbot

> Full-stack AI engineering project demonstrating Model Context Protocol (MCP), LiteLLM gateway, LangFuse observability, and automated CI/CD on AWS EC2.

**Live site:** [limjiajing.com](https://www.limjiajing.com) · **Author:** [Lim Jia Jing](https://www.linkedin.com/in/limjiajing123)

---

## What this project is

A personal portfolio website with an AI chatbot that answers questions about my background, skills, and experience. Built not just as a portfolio showcase, but as a real-world AI engineering system — with proper tool-augmented inference, observability, caching, and a three-layer CI/CD pipeline.

> **Claude Certified Architect Foundation** — Score: 983/1000

---

## Architecture

```
User (Browser)
      │
      ▼
React Frontend (Nginx · port 82)
      │  HTTPS via reverse proxy
      ▼
Node.js / Express Backend (port 5000)
      │              │               │
      ▼              ▼               ▼
MCP Server      LiteLLM           Redis
(Python)        Gateway           Cache
(port 8000)     (port 4000)
                     │
              ┌──────┴──────────┐
              ▼                 ▼
          Gemini AI         OpenRouter
          (primary)         (fallback)
              │
              ▼
          LangFuse
       (observability)

All services containerized · AWS EC2 · GitHub Actions CI/CD
```

---

## How the AI chatbot works

The chatbot uses a **two-stage inference pattern** via Model Context Protocol (MCP):

### Why MCP instead of context injection?

Traditional approach: dump the entire knowledge base into every prompt — wasteful, expensive, and imprecise.

MCP approach: define 9 specific tools. Gemini selects only the relevant tool and fetches precise data. Fewer tokens, higher accuracy, scales cleanly as portfolio data grows.

### Stage 1 — Tool selection

```
User: "what is jia jing's current job?"
              │
              ▼
    First Gemini call
    (receives list of 9 MCP tools)
              │
              ▼
    Gemini decides: call get_experience()
```

### Stage 2 — Response generation

```
    MCP server executes get_experience()
    Returns: raw work history JSON
              │
              ▼
    Second Gemini call
    (summarises tool result into natural language)
              │
              ▼
    "Jia Jing currently works at Cognizant/UOB
     as a Test Automation Software Analyst..."
```

---

## MCP Tools (9 total)

| Tool | Returns |
|---|---|
| `get_contact` | Email, phone, LinkedIn, website |
| `get_summary` | Professional summary |
| `get_education` | NTU degree, coursework |
| `get_experience` | Full work history with responsibilities |
| `get_projects` | Projects with tech stack and highlights |
| `get_skills` | Languages, frameworks, cloud, AI/ML, testing |
| `get_achievements` | Awards and certifications |
| `get_leadership` | Leadership and co-curricular roles |
| `search_portfolio` | Keyword search across all portfolio data |

---

## Tech stack

| Layer | Technology | Purpose |
|---|---|---|
| Frontend | React, Styled Components, Nginx | Portfolio UI |
| Backend | Node.js, Express.js | Chat API, orchestration |
| MCP Server | Python, FastMCP | 9 portfolio tools via Streamable HTTP |
| LLM Gateway | LiteLLM | Provider-agnostic routing and fallback |
| Primary LLM | Gemini AI (free tier) | Two-stage inference |
| Fallback LLM | OpenRouter | Automatic failover on rate limits |
| Cache | Redis | Response caching (~40% latency improvement) |
| Observability | LangFuse | Token usage, latency, cost, error tracking |
| Containers | Docker, Docker Compose | All services containerized |
| Registry | AWS ECR | Container image storage |
| Hosting | AWS EC2 | Production deployment |
| CI/CD | GitHub Actions | Automated testing and deployment |
| Reverse Proxy | Nginx | HTTPS, routing |
| Alerts | Discord Webhooks | API error notifications with cooldown |

---

## CI/CD pipeline

```
Push to preproduction branch
          │
          ▼
┌──────────────────────────────────┐
│        GitHub Actions CI         │
│                                  │
│  Step 1 — Unit tests             │
│  • LiteLLM and MCP mocked        │
│  • Tests backend logic only      │
│  • Deterministic, always pass    │
│                                  │
│  Step 2 — MCP integration tests  │
│  • Real Python MCP server        │
│  • Verifies all 9 tools return   │
│    correct data                  │
│  • No LLM involved               │
│                                  │
│  Step 3 — Smoke tests            │
│  • Health checks all services    │
│  • Backend, LiteLLM, MCP, Redis  │
└──────────────────────────────────┘
          │ all pass
          ▼
   Merge to main branch
          │
          ▼
┌──────────────────────────────────┐
│       Deploy Workflow            │
│  • Build Docker images           │
│  • Push to AWS ECR               │
│  • SSH into EC2                  │
│  • Run deploy.sh                 │
│  • Pull and restart containers   │
└──────────────────────────────────┘
          │
          ▼
   Discord notification
   (success or failure)
```

### Why mocked LLM tests in CI?

LLM calls are non-deterministic and rate-limited — they make unreliable CI tests. Unit tests mock the LLM to test whether the backend *handles* a successful response correctly. MCP integration tests verify tool correctness without any LLM involvement. Only deterministic tests run in CI.

---

## LangFuse observability

Every LLM call is tracked automatically via LiteLLM's native LangFuse callback integration:

- Full prompt and response for every request
- Token usage and estimated cost per call
- Latency breakdown across both Gemini calls
- Error tracking with stack traces
- Usage trends over time

Enabled by adding `success_callback: ["langfuse"]` and `failure_callback: ["langfuse"]` to `litellm_config.yaml` — no code changes required.

---

## Folder structure

```
portfolio_instance_only/
│
├── backend/
│   ├── server.js                 # Main Express server, MCP client, LiteLLM calls
│   ├── redis.js                  # Redis client setup
│   ├── discordAlertApiFail.js    # Discord webhook alerts
│   ├── axiosMock.js              # Axios mock for unit tests
│   ├── package.json
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Chatbot/          # AI chatbot UI component
│   │   │   └── UI/               # Shared UI components
│   │   ├── pages/
│   │   └── App.js
│   ├── package.json
│   └── Dockerfile
│
├── mcp-server/
│   ├── server.py                 # FastMCP server with 9 portfolio tools
│   ├── requirements.txt
│   └── Dockerfile
│
├── tests/
│   ├── smoke_test.py             # Health checks for all services
│   ├── test_backend.py           # Unit tests (mocked LLM)
│   ├── test_mcp.py               # MCP integration tests
│   └── test_frontend.py
│
├── .github/workflows/
│   ├── preprod.yml               # CI: test pipeline
│   └── deploy.yml                # CD: deploy to EC2
│
├── docker-compose.preprod.yml    # Preprod test environment
├── litellm_config.example.yaml   # LiteLLM config template
└── deploy.sh                     # EC2 deployment script
```

---

## Local setup

### Prerequisites
- Docker and Docker Compose
- Gemini API key — free at [aistudio.google.com](https://aistudio.google.com)
- OpenRouter API key — free at [openrouter.ai](https://openrouter.ai)
- LangFuse account — free at [cloud.langfuse.com](https://cloud.langfuse.com)

### 1. Clone the repo
```bash
git clone https://github.com/limjiajing123/portfolio_instance_only.git
cd portfolio_instance_only
```

### 2. Set up LiteLLM config
```bash
cp litellm_config.example.yaml litellm_config.yaml
# Add your API keys to litellm_config.yaml
```

### 3. Set environment variables
Create a `.env` file in the root:
```env
GEMINI_API_KEY=your_gemini_key
OPENROUTER_API_KEY=your_openrouter_key
DISCORD_WEBHOOK_URL=your_webhook_url
LANGFUSE_SECRET_KEY=your_langfuse_secret
LANGFUSE_PUBLIC_KEY=your_langfuse_public
LANGFUSE_HOST=https://cloud.langfuse.com
```

### 4. Start all services
```bash
docker compose up -d --build
```

### 5. Test
```bash
# Health check
curl http://localhost:5000/health

# Test the chatbot
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "what is jia jing email?"}'
```

### Local service ports
| Service | Port |
|---|---|
| Frontend | http://localhost:82 |
| Backend | http://localhost:5000 |
| MCP Server | http://localhost:8000 |
| LiteLLM | http://localhost:4000 |
| Redis | redis://localhost:6379 |

---

## Key engineering decisions

### Why LiteLLM instead of calling Gemini directly?
Vendor lock-in avoidance. LiteLLM provides a single OpenAI-compatible interface. Switching from Gemini to Claude or Llama requires changing one line in a config file. It also handles automatic fallback routing when Gemini hits rate limits.

### Why MCP instead of context injection?
Token efficiency and precision. Injecting the full portfolio as context on every request wastes tokens. MCP lets Gemini fetch only the data relevant to each question — reducing cost and improving answer accuracy.

### Why Redis caching?
The same question asked twice does not need two LLM calls. Redis caches responses with a 1-hour TTL, reducing API costs and improving response latency by approximately 40%.

### Why not ECS or EKS for production?
Intentional choice to learn deployment fundamentals. Understanding what managed services abstract away makes you a better engineer. The manual deploy script approach teaches EC2, ECR, networking, and container orchestration directly. ECS was explored during earlier phases of the project.

---

## Hardest bug fixed

**MCP SDK ESM/CommonJS incompatibility — `ERR_REQUIRE_ASYNC_MODULE`**

The backend crashed on startup because the MCP SDK (`@modelcontextprotocol/sdk`) uses ESM modules with top-level `await`, which CommonJS `require()` cannot load synchronously. The error message looked like a URL format issue — misleading and hard to trace.

Fix: switched from `require()` to dynamic `await import()` inside the MCP client functions, and pinned compatible versions between the Python server (`mcp==1.9.0`) and Node.js client (`@modelcontextprotocol/sdk@1.10.0`). They need to speak the same MCP protocol version.

**Lesson:** Error messages from module loaders are often symptoms, not root causes. Always check SDK changelogs when upgrading. Pin exact versions in production.

---

## What I'd build next

- **RAG pipeline** — store portfolio data in a vector database for semantic search instead of exact keyword matching in `search_portfolio`
- **LangFuse evals** — automated scoring of response quality, not just logging
- **Streaming responses** — stream Gemini output token by token for better UX
- **ECS migration** — move from manual deploy script to AWS ECS for automatic scaling and health management

---

## Author

**Lim Jia Jing** — Software Engineer, Singapore

- Email: limjiajing123@gmail.com
- LinkedIn: [linkedin.com/in/limjiajing123](https://www.linkedin.com/in/limjiajing123)
- Website: [limjiajing.com](https://limjiajing.com)

---

*Built entirely from scratch — no boilerplate AI project templates.*