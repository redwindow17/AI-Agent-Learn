
```markdown
# AI-Agent-Learn
```
- A brief description of the project
- Setup and installation instructions
- Example usage (especially for whereIAm agent.py)
- Dependencies
- Contribution guidelines (optional)
- License (optional)


```markdown
# AI-Agent-Learn

AI-Agent-Learn is a collection of AI-powered agent utilities and tools, including code agents, search tools, and data retrievers. This project demonstrates how to build and compose modular AI agents for a variety of information gathering tasks.

## Features

- Modular agent design powered by `smolagents` and LangChain
- Real-time weather retrieval with OpenWeatherMap API
- Guest information retrieval from datasets
- Natural language web search using DuckDuckGo
- Easily extensible with new tools and datasets

## Example: whereIAm agent

The `whereIAm agent.py` script demonstrates an agent (`alfred`) that can answer complex queries by combining tools for weather, search, and guest info.

### Example Usage

```bash
python "whereIAm agent.py"
```

#### Sample Query

```python
query = "Tell me about halish ricard J and his location and climate"
response = alfred.run(query)
print("AI Response:")
print(response)
```

## Dependencies

- Python 3.8+
- smolagents
- langchain
- langchain_community
- datasets
- requests

Install dependencies with:

```bash
pip install smolagents langchain langchain_community datasets requests
```

## Configuration

Some tools require API keys (e.g., OpenWeatherMap, Azure OpenAI). Make sure to set these in the code before running.

## Contributing

Pull requests are welcome! For major changes
