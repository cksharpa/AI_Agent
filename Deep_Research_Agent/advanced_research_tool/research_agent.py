from agents import Agent, WebSearchTool, ModelSettings, function_tool
from exa_py import Exa
import os

#Instead of using WebSearchTool, using Exa search tool which is free
#exa = Exa(api_key=os.environ["EXA_API_KEY"])

@function_tool
def exa_search_tool(query: str) -> str:
    """Search the web for latest information"""
    
    results = exa.search_and_contents(query, num_results=3)
    
    return "\n\n".join(
        f"{r.title}\n{r.text[:300]}"
        for r in results.results
    )

instructions= "You are an research assistant. Given a search query, gather relevant \
web information and generate a compact summary. \
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

research_agent = Agent(
    name="Research Assistant", 
    instructions=instructions,
    tools=[exa_search_tool],
    model="gpt-oss-20b",
    model_settings=ModelSettings(tool_choice="required"))