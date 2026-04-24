from pydantic import BaseModel, Field
from typing import List


class JobSearchIntent(BaseModel):
    search_query: str = Field(description="Clean job search query")
    target_role: str = Field(description="Main job title the user is looking for")
    location: str = Field(description="Target location")
    remote: bool = Field(description="Whether the user wants remote jobs")


class RankedJob(BaseModel):
    title: str
    company: str
    location: str
    url: str
    relevance_reason: str


class FinalJobResponse(BaseModel):
    summary: str
    jobs: List[RankedJob]