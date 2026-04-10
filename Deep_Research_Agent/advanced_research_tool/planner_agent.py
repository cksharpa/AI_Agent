from pydantic import BaseModel, Field
from agents import Agent

TOTAL_SEARCHES = 3

instructions1 = f"You are an research assistant. Given a search query, gather relevant \
web information and come up with a set of web searches to perform to best answer the query. \
Output {TOTAL_SEARCHES} terms to query for. \
\
Requirements: \
Length: 3-4 paragraphs, under 300 words \
Content: only essential insights and main points \
Style: concise, compressed, and information-dense \
\
Rules: \
Exclude filler, repetition, and low-value details \
Do not add explanations, opinions, or extra commentary \
Output only the final summary"

class WebSearchItem(BaseModel):
    reason: str = Field(description="Your reasoning for why this is important to the query.")

    query: str = Field(description="The search term to use for the web search.")

class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="A list of web searches to perform the best answer the query.")

planner_agent = Agent(
    name="PlannerAgent",
    instructions=instructions1,
    model="gpt-oss-20b",
    output_type=WebSearchPlan,
)