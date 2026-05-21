from mcp.server.fastmcp import FastMCP
import json

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
        "skills from robotics engineering (ROS, LiDAR/IMU, microservices). Passionate "
        "about contributing to national ICT projects and growing across Cloud, AppDev, "
        "DevSecOps, Cybersecurity, and Infrastructure. Recently built an AI-powered "
        "portfolio chatbot using Model Context Protocol (MCP), LiteLLM, and Gemini AI, "
        "and achieved Claude Certified Architect Foundation certification with a score of 983/1000."
    ),
    "education": {
        "university": "Nanyang Technological University, Singapore",
        "degree": "Bachelor of Mechanical Engineering (Honours Distinction)",
        "specialisation": "Robotics and Mechatronics",
        "period": "Aug 2020 - May 2024",
        "coursework": [
            "Robotics",
            "Mechatronics Engineering Design",
            "Machine Intelligence",
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
                "Automated progression, regression, smoke, sanity, system, and usability testing using Tricentis Tosca, reducing release defects",
                "Conducted functional and non-functional testing on B2B and B2C platforms (iOS, Android, Web, AS400) for TMRW and UOB Infinity using Perfecto, Postman, Oracle SQL, and SSH",
                "Performed API testing using Postman — validating JSON responses, status codes, and error handling for backend service reliability",
                "Deployed defect-fixed builds from SIT to UAT using Jenkins, improving CI/CD pipeline efficiency",
                "Created and executed test cases with Zephyr for Jira ensuring end-to-end traceability and Agile alignment",
                "Collaborated with developers, BAs, and QA teams via Jira and Confluence",
                "Actively participated in Agile SDLC sprints across full STLC",
                "Projects: EDP, UOBPay, NZOC, UOB Infinity, TMRW, FLMS, FSCM",
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
                "Demonstrated that treating moving obstacles as static yielded safer navigation than dynamic modeling",
            ],
        },
    ],
    "projects": [
        {
            "name": "AI-Powered Personal Portfolio Website",
            "status": "Present (ongoing)",
            "description": (
                "Full-stack portfolio with an AI chatbot powered by Model Context Protocol (MCP), "
                "LiteLLM gateway for provider-agnostic LLM routing, Gemini AI for inference, "
                "Redis caching, and automated CI/CD pipeline on AWS EC2. This is a real-world "
                "AI engineering project demonstrating end-to-end AI system design."
            ),
            "highlights": [
                "Built MCP server in Python (FastMCP) exposing 9 portfolio tools via Streamable HTTP transport — get_contact, get_summary, get_education, get_experience, get_projects, get_skills, get_achievements, get_leadership, search_portfolio",
                "MCP client in Node.js backend uses dynamic ESM import() with StreamableHTTPClientTransport for tool-based AI responses",
                "Gemini AI performs two-stage inference: first call selects the right MCP tool, second call summarizes tool results into natural language",
                "LiteLLM proxy for cost-optimised LLM routing (Gemini free tier as primary, OpenRouter/Llama as fallback)",
                "Redis caching reducing redundant API calls and improving response latency by ~40%",
                "CI/CD pipeline with GitHub Actions: preproduction branch runs unit tests (mocked LLM), MCP integration tests, and smoke tests before auto-deploying to main",
                "Containerized all services (React frontend, Node.js backend, Python MCP server, LiteLLM, Redis) with Docker and Docker Compose",
                "Deployed on AWS EC2 with ECR container registry, Route53 DNS, HTTPS via Nginx reverse proxy",
                "Discord webhook alerts for API errors with cooldown to prevent notification spam",
                "Achieved Claude Certified Architect Foundation certification with score of 983/1000",
            ],
            "tech": [
                "React", "Node.js", "Express", "Python", "FastMCP",
                "MCP (Model Context Protocol)", "LiteLLM", "Gemini AI", "OpenRouter",
                "Redis", "Docker", "Docker Compose", "AWS EC2", "AWS ECR",
                "GitHub Actions", "Nginx", "Streamable HTTP",
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
                "and Association Rule Mining to identify customer personas and customisation patterns."
            ),
            "tech": ["Python", "Pandas", "scikit-learn"],
        },
        {
            "name": "Waveform Generator",
            "period": "Jan 2024 - May 2024",
            "institution": "NTU Realtime Software for Mechatronics System",
            "description": (
                "Real-time waveform generator in C with multi-threading, timers, interrupts, "
                "D/A output control, and CLI configuration for oscilloscope visualization."
            ),
            "tech": ["C", "Real-time systems", "Multi-threading"],
        },
    ],
    "skills": {
        "languages": ["Python", "C++", "C", "Golang", "Java", "JavaScript", "SQL"],
        "frameworks": ["ReactJS", ".NET", "SpringBoot", "Pandas", "FastMCP"],
        "cloud_devops": [
            "AWS", "Docker", "Docker Compose", "Terraform", "Jenkins",
            "Redis", "GitHub Actions", "AWS ECR", "AWS EC2", "Nginx",
        ],
        "testing": [
            "Tricentis Tosca", "Postman", "Selenium", "Playwright",
            "Zephyr for Jira", "Perfecto",
        ],
        "databases": ["Oracle SQL", "Redis", "MySQL"],
        "tools": [
            "Linux", "Windows", "ROS1/2", "Git", "GitHub",
            "Jira", "Confluence", "Postman", "PuTTY", "Figma", "Microsoft Office",
        ],
        "ai_ml": [
            "LiteLLM", "MCP (Model Context Protocol)", "FastMCP",
            "Gemini AI", "OpenRouter", "Gen AI APIs",
            "Prompt Engineering", "K-modes Clustering", "Naive Bayes",
            "Streamable HTTP Transport",
        ],
        "languages_spoken": [
            "English (Proficient)", "Chinese (Proficient)",
            "Malay (Basic)", "Thai (Basic)",
        ],
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
            "description": "Led weekly training sessions for 20-30 individuals, maintaining discipline and collaborative learning.",
        },
        {
            "role": "Captain",
            "organisation": "Basketball, Riverside Secondary School",
            "period": "Jan 2012 - Jan 2015",
            "description": "Led team to participate in inter-school competitions, fostering teamwork and sportsmanship.",
        },
    ],
}

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
    Search across all portfolio content for a specific topic or keyword.
    Use this when the question doesn't fit neatly into one category,
    or when looking for a specific technology, company, or skill.
    """
    query_lower = query.lower()
    results = {}

    # search experience
    matched_exp = []
    for exp in PORTFOLIO_DATA["experience"]:
        searchable = (
            exp["company"] + exp["role"] + " ".join(exp["highlights"])
        ).lower()
        if query_lower in searchable:
            matched_exp.append(exp)
    if matched_exp:
        results["experience"] = matched_exp

    # search projects
    matched_proj = []
    for proj in PORTFOLIO_DATA["projects"]:
        searchable = (
            proj["name"] + proj["description"] + " ".join(proj.get("tech", []))
            + " ".join(proj.get("highlights", []))
        ).lower()
        if query_lower in searchable:
            matched_proj.append(proj)
    if matched_proj:
        results["projects"] = matched_proj

    # search skills
    for category, skill_list in PORTFOLIO_DATA["skills"].items():
        for skill in skill_list:
            if query_lower in skill.lower():
                if "skills" not in results:
                    results["skills"] = {}
                results["skills"][category] = skill_list
                break

    # search achievements
    matched_ach = [a for a in PORTFOLIO_DATA["achievements"] if query_lower in a.lower()]
    if matched_ach:
        results["achievements"] = matched_ach

    if not results:
        return json.dumps({"message": f"No results found for '{query}'"})

    return json.dumps(results, indent=2)


# ── Run ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    app = mcp.streamable_http_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)