from typing import List

from pydantic import BaseModel, Field


class SourceConfig(BaseModel):
    url: str = Field(description="The URL of the source configuration.")


class AgentResponse(BaseModel):
    answer: str = Field(description="The agent's answer to the query")
    sources: List[SourceConfig] = Field(
        default_factory=list, description="List of sources used to generate the answer"
    )
