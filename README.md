<div align="center">

# Manmeet Singh

### AI Engineer · building systems that remember, reason, and respond

**Senior AI Engineer** · 3+ years across applied AI and data science

[Portfolio](https://manmeet75.github.io/Portfolio/) · [GitHub projects](https://github.com/MANMEET75?tab=repositories) · [LinkedIn](https://www.linkedin.com/in/manmeet75/)

</div>

---

```toml
# manmeet.engineer

[focus]
build = ["LLM applications", "agent workflows", "voice AI"]
engineer = ["retrieval + memory", "evaluation + guardrails", "inference + APIs"]
care_about = ["useful behavior", "reliability", "latency", "cost"]
```

I like the part of AI engineering after the first demo: making context useful, measuring whether the system gets things right, and getting it to work reliably for real people. My work spans language models, retrieval, agents, voice interfaces, and the infrastructure around them.

## The way I build

| | Question | Engineering focus |
| :--- | :--- | :--- |
| **01 · Context** | What should the system know? | Retrieval, long-term memory, hybrid search |
| **02 · Action** | What should it do with that context? | Agent workflows, tools, voice and APIs |
| **03 · Proof** | How do we know it works? | Evaluation, guardrails, failure analysis |
| **04 · Delivery** | Will it hold up in use? | Model serving, latency, cost, deployment |

## Building in public

### [Semantra](https://github.com/MANMEET75/semantra-classify) `·` local-first text classification

A Python package for few-shot classification without a hosted model API. It combines ONNX embeddings with BM25 matching and can return `Unknown` when the evidence is weak.

```python
from semantra import Classifier

classifier = Classifier()
classifier.add_class("billing", ["I was charged twice", "My invoice is wrong"])
classifier.add_class("support", ["The app will not open", "I need technical help"])

result = classifier.predict("There is an extra charge on my invoice")
print(result.class_name, result.confidence)
```

[Install from PyPI](https://pypi.org/project/semantra-classify/) · [Read the source and quick start](https://github.com/MANMEET75/semantra-classify#quick-start)

<details>
<summary><strong>Explore more public repositories</strong></summary>

| Repository | What you will find |
| :--- | :--- |
| [MCP Agentic Data Engineering](https://github.com/MANMEET75/MCP-Agentic-Data-Engineering) | Agent-driven automation for data engineering tasks using MCP |
| [Document Summarizer](https://github.com/MANMEET75/DocumentSummarizer-AgenticRAG-LlamaIndex) | Document summarization and retrieval with LlamaIndex and FastAPI |
| [DataMentor](https://github.com/MANMEET75/DataMentor) | A data science interview assistant built around Mistral |

[Browse all repositories →](https://github.com/MANMEET75?tab=repositories)

</details>

## Toolbox

| Area | Tools I use |
| :--- | :--- |
| **Languages and APIs** | Python · SQL · FastAPI |
| **LLM and agent work** | LangGraph · LlamaIndex · MCP · Ollama |
| **Retrieval and quality** | Embeddings · BM25 · Qdrant · Promptfoo |
| **Shipping** | Docker · GitHub Actions · AWS · GCP |

---

<div align="center">

**Have an interesting AI systems problem?** [Let's connect on LinkedIn](https://www.linkedin.com/in/manmeet75/).

</div>
