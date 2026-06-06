from mcp.server.fastmcp import FastMCP
import json
import os

mcp = FastMCP("portfolio-server")

# ── Data ────────────────────────────────────────────────────────────────────

PORTFOLIO_DATA = {
    "personal": {
        "name": "Lim Jia Jing",
        "email": "limjiajing123@gmail.com",
        "phone": "+65 87845169",
        "linkedin": "https://www.linkedin.com/in/limjiajing123",
        "website": "https://limjiajing.com",
        "location": "Singapore",
        "residency_status": "Singapore Permanent Resident",
    },
    "summary": (
        "Aspiring Technology Consultant with experience in application development, "
        "cloud computing, DevSecOps practices, and large-scale system testing. "
        "Skilled in Python, Java, JavaScript, SQL, API testing, CI/CD workflows, "
        "and AWS/Docker deployments. Blends QA/Dev expertise with strong analytical "
        "skills from robotics engineering (ROS, LiDAR/IMU, microservices). Recently "
        "built an AI-powered portfolio chatbot using MCP, LiteLLM, Gemini AI, and a "
        "production RAG pipeline, and achieved Claude Certified Architect Foundation "
        "certification with a score of 983/1000."
    ),
    "education": {
        "university": "Nanyang Technological University, Singapore",
        "degree": "Bachelor of Mechanical Engineering (Honours Distinction)",
        "specialisation": "Robotics and Mechatronics",
        "period": "Aug 2020 - May 2024",
        "coursework": [
            "Robotics", "Mechatronics Engineering Design", "Machine Intelligence",
            "Realtime Software for Mechatronics System",
            "Introduction to Data Science and Artificial Intelligence",
            "Introduction to Computational Thinking",
            "Introduction to Digital Communications & Networking",
            "Introduction to Mechatronics Systems Design",
            "Mechatronics System Interfacing",
        ],
    },
    "experience": [
        {
            "company": "Cognizant Technology Solutions / United Overseas Bank",
            "role": "Associate (Test Automation Software Analyst)",
            "domain": "Banking Financial Services, UOB",
            "period": "June 2024 - Present",
            "highlights": [
                "Automated progression, regression, smoke, sanity, system, and usability testing using Tricentis Tosca",
                "Conducted functional and non-functional testing on B2B and B2C platforms (iOS, Android, Web, AS400) for TMRW and UOB Infinity using Perfecto, Postman, Oracle SQL, and SSH",
                "Performed API testing using Postman — validating JSON responses, status codes, and error handling",
                "Deployed defect-fixed builds from SIT to UAT using Jenkins, improving CI/CD pipeline efficiency",
                "Created and executed test cases with Zephyr for Jira ensuring end-to-end traceability",
                "Collaborated with developers, BAs, and QA teams via Jira and Confluence",
                "Actively participated in Agile SDLC sprints across full STLC",
                "Projects: EDP, UOBPay, NZOC, UOB Infinity, TMRW",
            ],
        },
        {
            "company": "ST Engineering Land Systems",
            "role": "Robotics Software Engineer (Internship)",
            "period": "Jan 2023 - Aug 2023",
            "highlights": [
                "Developed robotics software in C++, Python, and Golang with ROS 1/2 and SLAM systems",
                "Integrated SLAM algorithms (Cartographer, Gmapping) with Velodyne LiDAR data and Wireshark for network troubleshooting",
                "Created RViz plugins for interactive virtual map boundary definition",
                "Extracted and processed IMU data (heading, roll, pitch, yaw) for SPYDER hull-climbing robot",
                "Containerized microservices (GUIAPI, MySQL, FleetAPI, health checks) with Docker on private networks",
                "Recipient of Intern @ ST Engineering Award",
            ],
        },
        {
            "company": "Rehabilitation Research Institute of Singapore (RRIS) & NTU",
            "role": "Undergraduate Student Researcher (Robotic Software Engineer)",
            "period": "Aug 2023 - May 2024",
            "highlights": [
                "Final Year Project: Evaluating Navigation Among Crowds Algorithm for Shared Control of a Robotic Wheelchair (Grade: A)",
                "Developed and integrated navigation algorithms (Shared DWA, RDS) in C++ and Python using ROS",
                "Adapted open-source RDS collision-avoidance code for shared human-robot wheelchair control",
                "Built Python scripts for automated data logging and custom performance metrics",
                "Engineered simulation pipelines in Gazebo with custom RViz GUIs",
            ],
        },
    ],
    "projects": [
        {
            "name": "AI-Powered Personal Portfolio Website",
            "status": "Present (ongoing)",
            "description": (
                "Full-stack portfolio with an AI chatbot powered by Model Context Protocol (MCP), "
                "LiteLLM gateway, Gemini AI, Redis caching, a production RAG pipeline, and automated "
                "CI/CD on AWS EC2."
            ),
            "highlights": [
                "Built MCP server in Python (FastMCP) exposing portfolio tools via Streamable HTTP transport",
                "MCP client in Node.js backend uses dynamic ESM import() with StreamableHTTPClientTransport",
                "Gemini AI performs two-stage inference: first call selects the tool, second summarizes results",
                "LiteLLM proxy for cost-optimised LLM routing (Gemini primary, OpenRouter fallback)",
                "Redis caching reducing redundant API calls and improving response latency by ~40%",
                "Production RAG pipeline: hybrid search (BM25 + Cohere embeddings on Pinecone) with Cohere reranking, exposed as a semantic search MCP tool",
                "CI/CD pipeline with GitHub Actions: unit tests, MCP integration tests, smoke tests",
                "Deployed on AWS EC2 with ECR, Route53, Nginx reverse proxy",
                "LangFuse observability tracking token usage, latency, and cost",
                "Achieved Claude Certified Architect Foundation certification with score of 983/1000",
            ],
            "tech": [
                "Python", "Node.js", "Express", "React", "FastMCP",
                "MCP (Model Context Protocol)", "LiteLLM", "Gemini AI", "OpenRouter",
                "Redis", "Docker", "AWS EC2", "AWS ECR", "GitHub Actions", "Nginx",
                "Pinecone", "Cohere", "RAG",
            ],
        },
        {
            "name": "Evaluating Navigation Among Crowds Algorithm for Robotic Wheelchair",
            "period": "Aug 2023 - May 2024",
            "institution": "RRIS & NTU",
            "grade": "A",
            "description": (
                "Shared control robotic wheelchair navigation using DWA and RDS algorithms "
                "with Gazebo simulation and custom RViz GUIs."
            ),
            "tech": ["C++", "Python", "ROS", "Gazebo", "RViz"],
        },
        {
            "name": "Product Development Strategies for Vehicle Customisation & Personalisation",
            "period": "Jan 2024 - May 2024",
            "institution": "NTU Machine Intelligence",
            "description": (
                "Market survey analysis (n=50) using K-modes clustering, Multinomial Naive Bayes, "
                "and Association Rule Mining to identify customer personas."
            ),
            "tech": ["Python", "Pandas", "scikit-learn"],
        },
        {
            "name": "Waveform Generator",
            "period": "Jan 2024 - May 2024",
            "institution": "NTU Realtime Software for Mechatronics System",
            "description": (
                "Real-time waveform generator in C with multi-threading, timers, interrupts, "
                "D/A output control, and CLI configuration."
            ),
            "tech": ["C", "Real-time systems", "Multi-threading"],
        },
    ],
    "skills": {
        "languages": ["Python", "C++", "C", "Golang", "Java", "JavaScript", "SQL"],
        "frameworks": ["ReactJS", ".NET", "SpringBoot", "Pandas", "FastMCP"],
        "cloud_devops": ["AWS", "Docker", "Docker Compose", "Terraform", "Jenkins", "Redis", "GitHub Actions", "AWS ECR", "AWS EC2", "Nginx"],
        "testing": ["Tricentis Tosca", "Postman", "Selenium", "Playwright", "Zephyr for Jira", "Perfecto"],
        "databases": ["Oracle SQL", "Redis", "MySQL"],
        "ai_ml": ["LiteLLM", "MCP (Model Context Protocol)", "FastMCP", "Gemini AI", "OpenRouter", "Pinecone", "Cohere", "RAG", "Prompt Engineering"],
        "tools": ["Linux", "Windows", "ROS1/2", "Git", "GitHub", "Jira", "Confluence", "PuTTY", "Figma"],
        "languages_spoken": ["English (Proficient)", "Chinese (Proficient)", "Malay (Basic)", "Thai (Basic)"],
    },
    "achievements": [
        "Claude Certified Architect Foundation — Score: 983/1000",
        "Recipient of Associate of the Year Award — GenC (2025)",
        "Recipient of Intern @ ST Engineering Award (Aug 2023)",
        "Bachelor of Engineering with Honours Distinction — NTU (May 2024)",
        "Final Year Project Grade: A — Navigation Among Crowds Algorithm for Robotic Wheelchair",
    ],
    "leadership": [
        {
            "role": "Captain",
            "organisation": "Table Tennis, NTU Hall 12",
            "period": "Jan 2021 - Jan 2022",
            "description": "Led weekly training sessions for 20-30 individuals.",
        },
        {
            "role": "Captain",
            "organisation": "Basketball, Riverside Secondary School",
            "period": "Jan 2012 - Jan 2015",
            "description": "Led team in inter-school competitions.",
        },
    ],
}

# ── RAG pipeline (lazy, built once at startup) ───────────────────────────────
# Wrapped in try/except so the 9 structured tools still work even if
# RAG dependencies or API keys are unavailable.

_rag_retriever = None
_rag_available = False

def _init_rag():
    """Build the RAG retriever once. Returns True if successful."""
    global _rag_retriever, _rag_available
    try:
        from langchain_cohere import CohereEmbeddings, CohereRerank
        from langchain_pinecone import PineconeVectorStore
        from langchain_community.retrievers import BM25Retriever
        from langchain_classic.retrievers import EnsembleRetriever, ContextualCompressionRetriever
        from langchain_core.documents import Document
        from portfolio_data import SECTIONS

        if not os.environ.get("COHERE_API_KEY") or not os.environ.get("PINECONE_API_KEY"):
            print("RAG: API keys not set, semantic search tool disabled.")
            return False

        embeddings = CohereEmbeddings(
            model="embed-english-v3.0",
            cohere_api_key=os.environ["COHERE_API_KEY"]
        )
        vectorstore = PineconeVectorStore.from_existing_index(
            index_name="portfolio-rag",
            embedding=embeddings
        )
        semantic_retriever = vectorstore.as_retriever(search_kwargs={"k": 6})

        documents = [Document(page_content=s["content"], metadata={"section": s["section"]})
                     for s in SECTIONS]
        bm25_retriever = BM25Retriever.from_documents(documents)
        bm25_retriever.k = 6

        hybrid = EnsembleRetriever(
            retrievers=[bm25_retriever, semantic_retriever],
            weights=[0.4, 0.6]
        )
        reranker = CohereRerank(
            model="rerank-english-v3.0",
            cohere_api_key=os.environ["COHERE_API_KEY"],
            top_n=3
        )
        _rag_retriever = ContextualCompressionRetriever(
            base_compressor=reranker,
            base_retriever=hybrid
        )
        _rag_available = True
        print("RAG: semantic search pipeline ready.")
        return True
    except Exception as e:
        print(f"RAG: initialization failed ({e}), semantic search tool disabled.")
        return False

# ── Tools ────────────────────────────────────────────────────────────────────

@mcp.tool()
def get_contact() -> str:
    """Get Jia Jing's contact information including email, phone, LinkedIn and website."""
    return json.dumps(PORTFOLIO_DATA["personal"], indent=2)


@mcp.tool()
def get_summary() -> str:
    """Get a professional summary of who Jia Jing is and what he does."""
    return PORTFOLIO_DATA["summary"]


@mcp.tool()
def get_education() -> str:
    """Get Jia Jing's education background, university, degree and coursework."""
    return json.dumps(PORTFOLIO_DATA["education"], indent=2)


@mcp.tool()
def get_experience() -> str:
    """Get Jia Jing's full work experience including all roles and responsibilities."""
    return json.dumps(PORTFOLIO_DATA["experience"], indent=2)


@mcp.tool()
def get_projects() -> str:
    """Get Jia Jing's projects including tech stack, descriptions and highlights."""
    return json.dumps(PORTFOLIO_DATA["projects"], indent=2)


@mcp.tool()
def get_skills() -> str:
    """Get Jia Jing's technical skills including languages, frameworks, tools, cloud and AI/ML."""
    return json.dumps(PORTFOLIO_DATA["skills"], indent=2)


@mcp.tool()
def get_achievements() -> str:
    """Get Jia Jing's achievements, awards and honours."""
    return json.dumps(PORTFOLIO_DATA["achievements"], indent=2)


@mcp.tool()
def get_leadership() -> str:
    """Get Jia Jing's leadership experience and co-curricular activities."""
    return json.dumps(PORTFOLIO_DATA["leadership"], indent=2)


@mcp.tool()
def search_portfolio(query: str) -> str:
    """
    Keyword search across all portfolio content for a specific topic.
    Use this for exact term matching when looking for a specific
    technology, company, or skill.
    """
    query_lower = query.lower()
    results = {}
    matched_exp = []
    for exp in PORTFOLIO_DATA["experience"]:
        searchable = (exp["company"] + exp["role"] + " ".join(exp["highlights"])).lower()
        if query_lower in searchable:
            matched_exp.append(exp)
    if matched_exp:
        results["experience"] = matched_exp
    matched_proj = []
    for proj in PORTFOLIO_DATA["projects"]:
        searchable = (proj["name"] + proj["description"] + " ".join(proj.get("tech", []))
                      + " ".join(proj.get("highlights", []))).lower()
        if query_lower in searchable:
            matched_proj.append(proj)
    if matched_proj:
        results["projects"] = matched_proj
    for category, skill_list in PORTFOLIO_DATA["skills"].items():
        for skill in skill_list:
            if query_lower in skill.lower():
                results.setdefault("skills", {})[category] = skill_list
                break
    matched_ach = [a for a in PORTFOLIO_DATA["achievements"] if query_lower in a.lower()]
    if matched_ach:
        results["achievements"] = matched_ach
    if not results:
        return json.dumps({"message": f"No results found for '{query}'"})
    return json.dumps(results, indent=2)


@mcp.tool()
def search_portfolio_semantic(query: str) -> str:
    """
    Semantic search across all portfolio content using a RAG pipeline
    (hybrid keyword + vector search with reranking). Use this for
    open-ended, conceptual, or natural-language questions that don't
    map to a specific category — for example "what makes Jia Jing
    unique" or "tell me about his AI work". Falls back gracefully if
    the semantic search service is unavailable.
    """
    if not _rag_available:
        return json.dumps({
            "message": "Semantic search is currently unavailable. "
                       "Try a specific tool like get_experience or get_skills."
        })
    try:
        results = _rag_retriever.invoke(query)
        seen, chunks = set(), []
        for r in results:
            if r.page_content not in seen:
                seen.add(r.page_content)
                chunks.append({
                    "section": r.metadata.get("section", "unknown"),
                    "content": r.page_content
                })
        if not chunks:
            return json.dumps({"message": f"No relevant information found for '{query}'"})
        return json.dumps({"results": chunks}, indent=2)
    except Exception as e:
        return json.dumps({"message": f"Semantic search error: {str(e)}"})


# ── Run ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    # Initialize RAG once at startup (before serving requests)
    _init_rag()
    app = mcp.streamable_http_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)