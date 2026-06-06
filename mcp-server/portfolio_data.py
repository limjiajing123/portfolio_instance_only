"""
Shared portfolio data — imported by index_documents.py and query_rag.py.

IMPORTANT RAG PRINCIPLE: content is phrased the way ANSWERS are phrased,
not the way a resume is formatted. Each chunk includes natural-language
phrasing and the kinds of words people use in questions ("current job",
"works as", "studied at") so the retriever can match questions to content.
"""

SECTIONS = [
    {"content": """Jia Jing's contact information.
You can reach Lim Jia Jing by email at limjiajing123@gmail.com.
His LinkedIn profile is https://www.linkedin.com/in/limjiajing123.
His personal website is https://limjiajing.com.
He is based in Singapore and is a Singapore Permanent Resident.""",
     "section": "contact"},

    {"content": """Who is Jia Jing and what does he do professionally.
Lim Jia Jing is an aspiring Technology Consultant and AI engineer based in Singapore.
He works in application development, cloud computing, DevSecOps, and large-scale
system testing. He combines QA and development expertise with analytical skills
from a robotics engineering background. He is skilled in Python, Java, JavaScript,
SQL, API testing, CI/CD workflows, and AWS and Docker deployments.""",
     "section": "summary"},

    {"content": """Jia Jing's current job and present employment.
Jia Jing currently works as an Associate, Test Automation Software Analyst,
at Cognizant Technology Solutions, deployed to United Overseas Bank (UOB) in
Banking Financial Services. This is his current role and primary occupation,
which he has held since June 2024.
In this job he:
- Automates regression, smoke, sanity, system and usability testing using Tricentis Tosca
- Conducts functional and non-functional testing on iOS, Android, Web and AS400 platforms
- Performs API testing using Postman, validating JSON responses and status codes
- Deploys defect-fixed builds from SIT to UAT using Jenkins
- Works on projects including EDP, UOBPay, NZOC, UOB Infinity and TMRW""",
     "section": "experience"},

    {"content": """Jia Jing's past work experience as a Robotics Software Engineer intern.
From January 2023 to August 2023, Jia Jing worked as a Robotics Software Engineer
intern at ST Engineering Land Systems. In this job he:
- Developed robotics software in C++, Python and Golang using ROS 1 and ROS 2 with SLAM
- Integrated SLAM algorithms such as Cartographer and Gmapping with Velodyne LiDAR
- Containerized microservices with Docker on private networks
- Received the Intern at ST Engineering Award""",
     "section": "experience"},

    {"content": """Jia Jing's past work as an undergraduate robotics researcher.
From August 2023 to May 2024, Jia Jing worked as an Undergraduate Student Researcher
and Robotic Software Engineer at the Rehabilitation Research Institute of Singapore
(RRIS) and NTU. In this role he:
- Completed his Final Year Project on a Navigation Among Crowds Algorithm for a Robotic Wheelchair, grade A
- Developed navigation algorithms (Shared DWA and RDS) in C++ and Python using ROS
- Built automated data logging scripts with custom performance metrics""",
     "section": "experience"},

    {"content": """Jia Jing's main AI project: the AI-Powered Personal Portfolio Website.
Jia Jing built an AI chatbot portfolio website. In this project he:
- Built an MCP server in Python (FastMCP) exposing 9 portfolio tools via Streamable HTTP
- Integrated a LiteLLM gateway routing to Gemini AI with an OpenRouter fallback
- Implemented Redis caching, reducing API calls and improving latency by about 40 percent
- Built a CI/CD pipeline with GitHub Actions: unit tests, MCP integration tests, smoke tests
- Deployed on AWS EC2 with ECR, Route53 and an Nginx reverse proxy
- Added LangFuse observability tracking token usage, latency and cost
- Built a production RAG pipeline with hybrid search and Cohere reranking
Technologies used: Python, Node.js, React, MCP, LiteLLM, Gemini AI, Redis, Docker, AWS, Pinecone, Cohere.""",
     "section": "projects"},

    {"content": """Jia Jing's robotics research project on wheelchair navigation.
Jia Jing built a robotic wheelchair navigation research project at NTU and RRIS.
He developed Shared DWA and RDS navigation algorithms in C++ and Python, built
Gazebo simulation pipelines and custom RViz GUIs.
Technologies used: C++, Python, ROS, Gazebo, RViz.""",
     "section": "projects"},

    {"content": """Jia Jing's machine learning project on vehicle customisation.
Jia Jing built a machine learning project analysing vehicle customisation and
personalisation at NTU. He used K-modes clustering to segment customers and a
Multinomial Naive Bayes model to forecast customisation likelihood.
Technologies used: Python, Pandas, scikit-learn.""",
     "section": "projects"},

    {"content": """Jia Jing's technical skills and technologies he knows.
Programming languages: Python, C++, C, Golang, Java, JavaScript, SQL.
Frameworks: ReactJS, .NET, SpringBoot, Pandas, FastMCP.
Cloud and DevOps: AWS, Docker, Docker Compose, Terraform, Jenkins, Redis, GitHub Actions.
AI and machine learning: LiteLLM, MCP (Model Context Protocol), Gemini AI, OpenRouter,
Pinecone, Cohere, RAG, prompt engineering.
Testing tools: Tricentis Tosca, Postman, Selenium, Playwright, Zephyr for Jira, Perfecto.
Databases: Oracle SQL, Redis, MySQL.""",
     "section": "skills"},

    {"content": """Where Jia Jing studied: his education background.
Jia Jing studied at Nanyang Technological University (NTU) in Singapore.
He graduated with a Bachelor of Mechanical Engineering with Honours Distinction,
specialising in Robotics and Mechatronics. He studied there from August 2020 to May 2024.""",
     "section": "education"},

    {"content": """Jia Jing's certifications, awards and achievements.
Jia Jing holds the Claude Certified Architect Foundation certification with a score of 983 out of 1000.
His other awards and recognition include:
- Associate of the Year Award at GenC, 2025
- Intern at ST Engineering Award, August 2023
- Bachelor of Engineering with Honours Distinction from NTU, May 2024
- Final Year Project grade A for the Navigation Among Crowds Algorithm for a Robotic Wheelchair""",
     "section": "achievements"},

    {"content": """Jia Jing's leadership experience and co-curricular activities.
Jia Jing was Captain of the Table Tennis Team at Hall 12, NTU, from January 2021 to
January 2022, leading weekly training sessions for 20 to 30 people.
He was also Captain of the Basketball Team at Riverside Secondary School from 2012 to 2015,
leading the team in inter-school competitions.""",
     "section": "leadership"},
]
