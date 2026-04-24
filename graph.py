from typing import TypedDict, List

from langgraph.graph import StateGraph, START, END

from nodes import understand_request, search_jobs, rank_jobs


class JobState(TypedDict):
    user_request: str
    keywords: str
    target_role: str
    location: str
    remote: bool
    jobs: List[dict]
    final_answer: str


def build_graph():
    workflow = StateGraph(JobState)

    workflow.add_node("understand_request", understand_request)
    workflow.add_node("search_jobs", search_jobs)
    workflow.add_node("rank_jobs", rank_jobs)

    workflow.add_edge(START, "understand_request")
    workflow.add_edge("understand_request", "search_jobs")
    workflow.add_edge("search_jobs", "rank_jobs")
    workflow.add_edge("rank_jobs", END)

    return workflow.compile()