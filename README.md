<div align="center">

# Manmeet Singh

### AI Engineer · NLP · Retrieval · Agentic Systems

I turn AI ideas into tools that developers can run, inspect, and improve.

[Portfolio](https://manmeet75.github.io/Portfolio/) · [Projects](https://github.com/MANMEET75?tab=repositories) · [LinkedIn](https://www.linkedin.com/in/manmeet75/)

</div>

```text
manmeet@build:~$ cat focus.txt

  language    → understand the request
  retrieval   → find the useful context
  agents      → connect tools to a workflow
  evaluation  → check what actually works

manmeet@build:~$ _
```

## `01 / featured build`

### [Semantra](https://github.com/MANMEET75/semantra-classify) — text classification that runs locally

Semantra combines semantic matching with keyword matching. It uses ONNX embeddings and BM25, then checks confidence before choosing a class. Ambiguous input can return `Unknown`.

```text
                           ┌─ ONNX embeddings ─┐
text input ────────────────┤                   ├─ score fusion ── class / Unknown
                           └─ BM25 matching ───┘
```

```python
from semantra import Classifier

classifier = Classifier()
classifier.add_class("billing", ["I was charged twice", "My invoice is wrong"])
classifier.add_class("support", ["The app will not open", "I need technical help"])

result = classifier.predict("There is an extra charge on my invoice")
print(result.class_name, result.confidence)
```

`pip install semantra-classify` · [Source and full quick start](https://github.com/MANMEET75/semantra-classify#quick-start) · [PyPI](https://pypi.org/project/semantra-classify/)

## `02 / other work`

| Repository | What it explores | Stack |
| :--- | :--- | :--- |
| [Document Summarizer](https://github.com/MANMEET75/DocumentSummarizer-AgenticRAG-LlamaIndex) | Document summarization and retrieval through an API | Python · LlamaIndex · FastAPI |
| [MCP Agentic Data Engineering](https://github.com/MANMEET75/MCP-Agentic-Data-Engineering) | Tool-driven data ingestion and workflows | Python · MCP · MongoDB · MySQL |
| [DataMentor](https://github.com/MANMEET75/DataMentor) | A data science interview assistant using a fine-tuned Mistral model | Python · Mistral · QLoRA |

<details>
<summary><strong>Open more projects</strong></summary>

- [VideoAnalytics-HAR](https://github.com/MANMEET75/VideoAnalytics-HAR) — human activity recognition.
- [HindBot](https://github.com/MANMEET75/HindBot) — document question answering.
- [Portfolio](https://github.com/MANMEET75/Portfolio) — source for my personal site.
- [All repositories](https://github.com/MANMEET75?tab=repositories)

</details>

## `03 / tools I work with`

`Python` · `SQL` · `NLP` · `Embeddings` · `RAG` · `ONNX Runtime` · `FastAPI` · `Docker` · `GitHub Actions` · `AWS`

---

**Building something in applied AI?** [Connect with me on LinkedIn](https://www.linkedin.com/in/manmeet75/).
