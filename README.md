<div align="center">

# Manmeet Singh

### AI Engineer

Building useful AI systems with Python, NLP, retrieval, and agent workflows.

[Portfolio](https://manmeet75.github.io/Portfolio/) · [LinkedIn](https://www.linkedin.com/in/manmeet75/) · [All repositories](https://github.com/MANMEET75?tab=repositories)

</div>

```console
manmeet@github:~$ cat profile.txt
ROLE       AI Engineer
FOCUS      NLP · semantic search · local AI · agent systems
APPROACH   prototype → evaluate → package → deploy
CURRENT    building developer-friendly AI tools
```

## `> about`

I turn AI ideas into software people can run and use. My work covers language models, retrieval, classification, computer vision, and the APIs and workflows that bring them into applications.

```python
stack = {
    "languages": ["Python", "SQL"],
    "ai": ["NLP", "embeddings", "RAG", "agents", "computer vision"],
    "build": ["FastAPI", "ONNX Runtime", "Docker", "GitHub Actions"],
    "data": ["MongoDB", "MySQL", "AWS"],
}
```

## `> selected_projects`

### 01. [Semantra](https://github.com/MANMEET75/semantra-classify) — local-first text classification

Classify new text from a few examples, without training a model or calling a hosted inference API. It combines ONNX embeddings with BM25 matching and can return `Unknown` for ambiguous input.

`Python` · `ONNX Runtime` · `BM25` · `multilingual NLP` · [PyPI package](https://pypi.org/project/semantra-classify/)

<details>
<summary><strong>Run a minimal example</strong></summary>

```bash
pip install semantra-classify
```

```python
from semantra import Classifier

classifier = Classifier()
classifier.add_class("billing", ["I was charged twice", "My invoice is wrong"])
classifier.add_class("support", ["The app will not open", "I need technical help"])

result = classifier.predict("There is an extra charge on my invoice")
print(result.class_name, result.confidence)
```

[Documentation and more examples →](https://github.com/MANMEET75/semantra-classify#quick-start)

</details>

### 02. [Document Summarizer](https://github.com/MANMEET75/DocumentSummarizer-AgenticRAG-LlamaIndex) — document intelligence

A LlamaIndex-based document summarizer and retrieval application with a FastAPI interface.

`Python` · `LlamaIndex` · `RAG` · `FastAPI`

### 03. [MCP Agentic Data Engineering](https://github.com/MANMEET75/MCP-Agentic-Data-Engineering) — agent workflows

Experiments with tools for data ingestion, databases, object storage, scheduling, and task logging.

`Python` · `MCP` · `MongoDB` · `MySQL` · `Airflow`

### 04. [DataMentor](https://github.com/MANMEET75/DataMentor) — AI interview assistant

A data science interview assistant built around a fine-tuned Mistral model.

`Python` · `Mistral` · `QLoRA` · `AWS`

<details>
<summary><strong>More projects</strong></summary>

- [VideoAnalytics-HAR](https://github.com/MANMEET75/VideoAnalytics-HAR) — human activity recognition with a Streamlit prototype and API.
- [HindBot](https://github.com/MANMEET75/HindBot) — retrieval-based question answering over documents.
- [Email Semantic Search](https://github.com/MANMEET75/Email-SemanticSearchEngine-PoweredByOpenAI) — semantic search across email content.
- [Portfolio](https://github.com/MANMEET75/Portfolio) — personal website source.
- [Browse every repository →](https://github.com/MANMEET75?tab=repositories)

</details>

## `> connect`

Interested in applied AI, NLP, or developer tools? [Connect on LinkedIn](https://www.linkedin.com/in/manmeet75/) or explore the code above.
