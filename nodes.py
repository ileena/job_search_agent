from typing import List
import os

from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain_core.prompts import ChatPromptTemplate

from schemas import JobSearchIntent, FinalJobResponse


llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

search_tool = TavilySearch(max_results=5)


def understand_request(state):
    structured_llm = llm.with_structured_output(JobSearchIntent)

    prompt = ChatPromptTemplate.from_template("""
You are a smart career assistant.

Understand the user request and extract:
- clean search query
- main target role
- target location
- remote true or false

User request:
{user_request}
""")

    chain = prompt | structured_llm

    response = chain.invoke({
        "user_request": state["user_request"]
    })

    return {
        "keywords": response.search_query,
        "target_role": response.target_role,
        "location": response.location,
        "remote": response.remote
    }


def search_jobs(state):
    try:
        remote_text = "remote" if state["remote"] else ""

        search_query = f"""
{state["target_role"]} {remote_text} jobs in {state["location"]}
apply careers
"""

        results = search_tool.invoke({
            "query": search_query
        })

        jobs = results.get("results", [])

        return {
            "jobs": jobs
        }

    except Exception:
        return {
            "jobs": []
        }


def rank_jobs(state):
    jobs = state["jobs"]

    if not jobs:
        return {
            "final_answer": '{"summary":"No jobs found. Try another search.","jobs":[]}'
        }

    structured_llm = llm.with_structured_output(FinalJobResponse)

    text = ""

    for job in jobs:
        text += f"""
Title: {job.get("title")}
URL: {job.get("url")}
Summary: {job.get("content")}
-------------------
"""

    prompt = ChatPromptTemplate.from_template("""
You are a smart career assistant.

User request:
{user_request}

Target role:
{target_role}

Location:
{location}

Remote:
{remote}

Jobs found:
{jobs}

Select the best matching jobs.

For each job:
- Extract title
- Extract company if available, otherwise use "Unknown"
- Extract location if available, otherwise use the user's target location
- Include URL
- Explain why it is relevant
""")

    chain = prompt | structured_llm

    response = chain.invoke({
        "user_request": state["user_request"],
        "target_role": state["target_role"],
        "location": state["location"],
        "remote": state["remote"],
        "jobs": text
    })

    return {
        "final_answer": response.model_dump_json(indent=2)
    }