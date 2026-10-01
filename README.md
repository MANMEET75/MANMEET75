<div align="center">

# Manmeet Singh

**AI engineer building practical NLP tools, agent workflows, and data products.**

[Portfolio](https://manmeet75.github.io/Portfolio/) · [Projects](https://github.com/MANMEET75?tab=repositories) · [LinkedIn](https://www.linkedin.com/in/manmeet75/) · [Semantra on PyPI](https://pypi.org/project/semantra-classify/)

</div>

```text
$ whoami
Manmeet — Python • NLP • applied AI • data engineering

$ current_focus
Local-first AI that is useful, testable, and easy to integrate.
```

## Build with me

I work across the path from **idea → model → API → deployment**. My projects span semantic search, document intelligence, AI agents, computer vision, and analytics. I care about clear interfaces, measurable behavior, and tools developers can actually run.

<details open>
<summary><strong>🚀 Featured work</strong></summary>

| Project | What it does | Explore |
| --- | --- | --- |
| **Semantra** | Offline, few-shot text classification with ONNX embeddings and BM25. Supports English and multilingual input without a hosted inference API. | [Code](https://github.com/MANMEET75/semantra-classify) · [Package](https://pypi.org/project/semantra-classify/) |
| **Document Summarizer** | LlamaIndex-based document summarization and retrieval with a FastAPI interface. | [Code](https://github.com/MANMEET75/DocumentSummarizer-AgenticRAG-LlamaIndex) |
| **MCP Agentic Data Engineering** | Agent workflows for data ingestion, databases, object storage, scheduling, and task logging. | [Code](https://github.com/MANMEET75/MCP-Agentic-Data-Engineering) |
| **DataMentor** | A data science interview assistant built around a fine-tuned Mistral model. | [Code](https://github.com/MANMEET75/DataMentor) |

</details>

## Try something I built

Semantra runs locally after installation. Define intent classes with examples and classify new text:

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

[Read the full quick start →](https://github.com/MANMEET75/semantra-classify#quick-start)

## Toolbox

| Area | Tools and topics |
| --- | --- |
| **Core** | Python, SQL, REST APIs, Git, Docker |
| **AI and search** | NLP, embeddings, retrieval, classification, LlamaIndex, Hugging Face, ONNX Runtime, BM25 |
| **Data and delivery** | FastAPI, MongoDB, MySQL, GitHub Actions, AWS, analytics and dashboards |

<details>
<summary><strong>🧭 Explore more projects</strong></summary>

- [VideoAnalytics-HAR](https://github.com/MANMEET75/VideoAnalytics-HAR) — human activity recognition with a Streamlit prototype and API.
- [HindBot](https://github.com/MANMEET75/HindBot) — question answering over documents with retrieval.
- [Email Semantic Search](https://github.com/MANMEET75/Email-SemanticSearchEngine-PoweredByOpenAI) — semantic search across email content.
- [Portfolio](https://github.com/MANMEET75/Portfolio) — my personal website.
- [All public repositories](https://github.com/MANMEET75?tab=repositories) — browse the rest of my work.

</details>

---

**Interested in building useful AI tools together?** [Connect on LinkedIn](https://www.linkedin.com/in/manmeet75/) or [explore my repositories](https://github.com/MANMEET75?tab=repositories).
