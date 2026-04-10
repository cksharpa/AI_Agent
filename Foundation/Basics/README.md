I have used "Jupyter Notebook" to start with basic understanding.

I'll try to use mostly free LLM Models available with Ollama
which will be running locally.

📌 Prerequisites

- Python 3.8+
- Ollama installed on your system
- [Optional] I have used cursor IDE for all development.

⚙️ Setup Instructions

1. Install Python package

pip install ollama

2. Pull required model

ollama pull llama3.2

Note : llama3.2 is not the latest one but good one to start with. You can also pull other free LLMs available with
Ollama to experiment with different  output results.

3. Verify available models

ollama list

4. Ensure Ollama server is running

ollama serve
