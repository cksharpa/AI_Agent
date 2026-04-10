# Deep Research Agent

Deep research agent is a multi-agent system which includes :

1. "planner_agent" : To plan relevant web information and comes up with set of optimized web search queries to
effectively answer a given question.

2. "research_agent" : Run web search for each item in search plan, gather initial level of relevant web information and
generate a concise summary.

3. "senior_research_agent" : Get the preliminary research findings from research_agent, review it thoroughly, add
insights and write a clear, structured report.

4. "email_agent" : Responsible for formatting the report and send as email.

# Advanced Research Tool

Advance research tool is a deep research agent with "gradio" python library to create interactive user interfaces.

📌 Prerequisites
- Install Gradio python library using "pip install gradio" in python3 virtual environment
- All environment variables(API_KEYs and Endpoints) are properly set and loaded

Execute "python3 deep_research_tool.py" to run the tool. 

