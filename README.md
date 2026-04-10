# AI_Agent
Maintaining this repo for AI Agents related learning and projects.

Important Notes :

- Used Cursor and VS code IDE for all development

- Python 3.10+ is recommended

- Important "pip install" in python venv :  gradio, exa_py, sendgrid, ipykernel, pydantic, pushover-complete, openai-agents

- I have tried using mostly free LLM models like "gpt-oss-20b", "deepseek-r1" and models available with Ollama. Also, free tools like Exa search tool, Sendgrid for sending emails, pushover for notifications etc. 

- However, each project has been tested with paid LLMs and tools too (mostly like  gpt-4o-mini, websearchtool). So,Feel
free to replace models and tools for better and optimal  results.

- Instead of managing separate API keys for OpenAI, Anthropic, DeepSeek, Google etc, I have used one OpenRouter API key to
access all of them. This simplifies to use multiple AI models both free and paid versions.

- trace(), used in projects is part of the OpenAI Agents SDK and relies on OpenAI’s native tracing infrastructure. It is not compatible with OpenRouter-based API configurations. To enable tracing and view execution details at the OpenAI Traces dashboard, a valid OpenAI API key (OPENAI_API_KEY) is required. However, this does not impact the core execution of the code, When using an OpenRouter API key and will continue to run successfully without tracing.

- CrewAI requires Python >=3.10 and <3.14.
