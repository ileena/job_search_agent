# 🚀 Job Search Agent

An AI-powered Job Search Agent built with **LangChain**, **LangGraph**, **Tavily**, and **OpenRouter**.

This project demonstrates how to build a real AI Agent that understands user intent, searches the web for live job opportunities, ranks the best matches, and returns structured, reliable results.

---

# 🌟 Why This Project Matters

Most beginner AI projects only generate text.

This project goes beyond chatbots by demonstrating how to build an **AI system that can think, search, decide, and return usable outputs**.

Instead of:

> “Here are some jobs...”

This agent performs a complete workflow:

```text
Understand Request
↓
Extract Search Intent
↓
Search Live Jobs
↓
Rank Best Matches
↓
Return Structured Results
```

---

# 🧠 Example Input

```text
Find remote Product Analyst jobs in Saudi Arabia
```

---

# ✅ Example Output

```text
Summary:
Found 3 relevant opportunities.

1. Product Analyst
Company: TechCorp
Location: Remote - Saudi Arabia

2. Senior Product Analyst
Company: Growth Labs
Location: Riyadh
```

---

# ⚙️ Tech Stack

* **Python**
* **LangChain** → LLM orchestration
* **LangGraph** → Multi-step workflow engine
* **OpenRouter** → Multi-model AI access
* **Tavily** → Real-time web search
* **Pydantic** → Structured output schemas
* **dotenv** → Environment management

---

# 🏗️ Architecture

```text
User Input
↓
LangGraph Workflow
├── Understand Request
├── Search Jobs
├── Rank Results
↓
Final Response
```

---

# 📁 Project Structure

```text
job-search-agent/
│── main.py
│── graph.py
│── nodes.py
│── schemas.py
│── .env
│── .gitignore
│── requirements.txt
│── README.md
```

---

# 📌 File Responsibilities

## schemas.py = Data Structure Layer

Defines the shape of data used by the system.

Examples:

* JobSearchIntent
* RankedJob
* FinalJobResponse

Why important:

* Reliable outputs
* Easy API integration
* Frontend ready
* Validation support

---

## nodes.py = Agent Logic Layer

Contains the actual steps the AI agent performs.

Examples:

* understand_request()
* search_jobs()
* rank_jobs()

Why important:

* Clean business logic
* Reusable steps
* Easier maintenance

---

## graph.py = Workflow Layer

Defines how nodes connect using LangGraph.

```text
START
↓
understand_request
↓
search_jobs
↓
rank_jobs
↓
END
```

Why important:

* Clear orchestration
* State passing
* Easy scaling
* Better than giant functions

---

## main.py = Application Entry Point

Responsible for:

* Loading environment variables
* Building the graph
* Accepting user input
* Running the app
* Printing results

Run with:

```bash
python main.py
```

---

# 🧩 Why Schema Was Important

LLMs often return inconsistent natural language.

Instead of relying on paragraphs, I used schemas to produce reliable outputs such as:

```json
{
  "target_role": "Product Analyst",
  "location": "Saudi Arabia",
  "remote": true
}
```

This makes the product production-ready for:

* APIs
* Dashboards
* Databases
* Frontend applications

---

# 💼 Why LangGraph?

LangGraph was selected because real AI agents require multiple steps.

Instead of one giant prompt, LangGraph allows:

* Clear workflow design
* Reusable nodes
* State management
* Scalable architecture

---

# 🚀 Installation

```bash
git clone https://github.com/yourusername/job-search-agent.git
cd job-search-agent
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```

---

# ▶️ Run Project

```bash
python main.py
```

---

# 📈 Future Improvements

* Streamlit UI
* Save search history
* Email alerts
* Salary filtering
* Country filters
* CV matching engine
* LinkedIn direct integration
* LangSmith monitoring

---

---

# 👨‍💻 What I Learned

* Building AI workflows
* Tool calling
* Structured outputs
* Search augmentation
* Product-focused AI engineering

---

# ⭐ Final Note

This project reflects the transition from **using AI tools** to **engineering AI systems**.
