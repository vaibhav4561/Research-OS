# 🤖 ResearchOS — AI Multi-Agent Research Assistant

ResearchOS is a production-ready AI research assistant that leverages a **multi-agent architecture** to automate the complete research workflow—from searching the web to generating comprehensive research reports and evaluating their quality.

The system combines **LangChain**, **FastAPI**, **Streamlit**, **PostgreSQL**, and modern LLM workflows to deliver an end-to-end research experience.

---

# 🚀 Features

### 🔍 Intelligent Search Agent

* Searches the web using Tavily Search API
* Retrieves recent and reliable information
* Selects relevant sources for further analysis

### 🌐 Reader Agent

* Scrapes webpages using BeautifulSoup
* Extracts clean textual content
* Removes unnecessary HTML elements

### ✍️ Writer Agent

* Generates professional research reports
* Produces well-structured markdown output
* Combines search results with scraped knowledge

### 🧠 Critic Agent

* Reviews generated reports
* Assigns quality score
* Identifies strengths
* Suggests improvements
* Provides final evaluation

### 🗄️ Research History

* Stores generated reports in PostgreSQL
* Retrieve previous research
* View historical reports
* Persistent storage

### 🎨 Modern User Interface

* Built with Streamlit
* Interactive research workflow
* Real-time progress indicators
* Download generated reports
* Expandable research history

---

# 🏗️ System Architecture

```text
                    User
                      │
                      ▼
              Streamlit Frontend
                      │
              REST API Request
                      │
                      ▼
              FastAPI Backend
                      │
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
 Search Agent     Reader Agent     Writer Agent
      │               │                │
      └───────────────┼────────────────┘
                      ▼
               Critic Agent
                      │
                      ▼
             PostgreSQL Database
```

---

# 🔄 Research Pipeline

```text
User Query
     │
     ▼
Search Agent
     │
     ▼
Reader Agent
     │
     ▼
Writer Agent
     │
     ▼
Critic Agent
     │
     ▼
Store Report in PostgreSQL
     │
     ▼
Return Results to Streamlit
```

---

# 🛠️ Tech Stack

## AI & LLM

* Mistral AI
* LangChain
* LangGraph
* LCEL (LangChain Expression Language)

## Backend

* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic

## Frontend

* Streamlit

## Search & Scraping

* Tavily Search API
* BeautifulSoup
* Requests

## Database

* PostgreSQL

## Deployment

* Render (Backend)
* Streamlit Community Cloud (Frontend)
* Neon PostgreSQL (Database)

---

# 📂 Project Structure

```text
ResearchOS
│
├── app.py                         # Streamlit Frontend
├── requirements.txt
├── README.md
│
└── backend
    │
    ├── app
    │   │
    │   ├── agents
    │   │     ├── search_agent.py
    │   │     ├── reader_agent.py
    │   │     ├── writer_agent.py
    │   │     ├── critic_agent.py
    │   │     └── llm.py
    │   │
    │   ├── api
    │   │     └── research.py
    │   │
    │   ├── database
    │   │     ├── database.py
    │   │     └── models.py
    │   │
    │   ├── services
    │   │     └── pipeline.py
    │   │
    │   ├── utils
    │   │     └── tools.py
    │   │
    │   └── main.py
    │
    └── requirements.txt
```

---

# 📸 Screenshots

## Home Dashboard

<img width="1907" height="878" alt="Screenshot 2026-06-08 184940" src="https://github.com/user-attachments/assets/37faa8b1-8239-4a69-9d18-eddd5cec50ff" />


---

## Research Pipeline

<img width="1905" height="940" alt="Screenshot 2026-06-08 184749" src="https://github.com/user-attachments/assets/28b86cbe-c679-4b81-a538-96b31955f800" />


---

## Generated Report

<img width="1906" height="900" alt="Screenshot 2026-06-08 184859" src="https://github.com/user-attachments/assets/462c1350-2eb2-4942-b4a2-59f9ffd58553" />


---


# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/vaibhav4561/Research-OS.git

cd Research-OS
```

## Create Virtual Environment

```bash
uv venv
```

Activate environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
uv pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
MISTRAL_API_KEY=your_key
TAVILY_API_KEY=your_key

DATABASE_URL=your_postgresql_database_url
```

---

## Run Backend

```bash
cd backend

python -m uvicorn app.main:app --reload
```

---

## Run Frontend

```bash
streamlit run app.py
```

---

# 📡 REST API

## Generate Research

```http
POST /research
```

---

## Get Research History

```http
GET /research/history
```

---

## Get Research by ID

```http
GET /research/history/{id}
```

---

# 💡 Example Topics

* Artificial Intelligence
* Future of Robotics
* Quantum Computing
* Autonomous Vehicles
* Climate Change
* Cybersecurity
* Large Language Models
* Space Exploration

---

# 📚 What I Learned

This project strengthened my understanding of:

* Multi-Agent AI Systems
* LangChain & LangGraph
* AI Workflow Orchestration
* Prompt Engineering
* FastAPI Development
* REST API Design
* PostgreSQL Integration
* SQLAlchemy ORM
* Streamlit UI Development
* Production AI Architecture
* Full-Stack AI Application Development

---

# 🚀 Future Enhancements

* RAG with Vector Database
* PDF Export
* Research Citations
* Authentication
* Multi-user Support
* Async Agent Execution
* Streaming Responses
* Docker Deployment
* Cloud Storage Integration

---

# 🤝 Contributing

Contributions are welcome.

Feel free to fork the repository, create a feature branch, and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Vaibhav Jain**

GitHub: https://github.com/vaibhav4561

LinkedIn: https://www.linkedin.com/in/vaibhav-jain-93958a2b5/

If you found this project useful, consider giving it a ⭐ on GitHub.
