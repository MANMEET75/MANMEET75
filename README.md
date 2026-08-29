<div align="center">

# Hi, I'm Manmeet Singh 👋

### AI Engineer • Machine Learning • NLP • Data & Analytics

I build practical, production-oriented AI systems that turn complex data and language problems into reliable developer tools.

[![GitHub](https://img.shields.io/badge/GitHub-MANMEET75-181717?style=flat&logo=github)](https://github.com/MANMEET75)
[![Python](https://img.shields.io/badge/Python-Expert%20Focus-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Open Source](https://img.shields.io/badge/Open%20Source-Projects-3DA639?style=flat&logo=opensourceinitiative&logoColor=white)](https://github.com/MANMEET75?tab=repositories)

</div>

## About me

- I design and ship AI/ML solutions with a focus on usability, performance, and maintainability.
- Interested in natural language processing, semantic search, multilingual AI, retrieval systems, and intelligent automation.
- I enjoy taking ideas from prototype to documented, testable, installable software.
- I care about low-latency inference, modular architecture, reproducibility, and real-world impact.

## Featured project

### [Semantra Classify](https://github.com/MANMEET75/semantra-classify)

An offline, few-shot semantic classification engine for Python.

Define classes with example sentences and classify new queries without model training, API keys, or server infrastructure.

**Highlights**

- Local ONNX embeddings with no external inference API
- Hybrid semantic similarity and BM25 lexical matching
- Multilingual and Hinglish-friendly classification
- Confidence thresholds with Unknown detection
- Top-k predictions and inference-latency reporting
- Persistence, concurrency-safe prediction, tests, and CI
- Installable directly from PyPI

Install: pip install semantra-classify

Example:

    from semantra import Classifier

    classifier = Classifier()

    classifier.add_class("billing", [
        "I was charged twice",
        "There is an issue with my invoice",
        "Why was money deducted from my account?"
    ])

    classifier.add_class("technical_support", [
        "The application is not opening",
        "I am getting an error",
        "The service stopped working"
    ])

    result = classifier.predict("My invoice has an incorrect charge")
    print(result.label, result.confidence, result.latency_ms)

## Technical focus

**Languages:** Python, SQL

**AI/ML:** NLP, semantic similarity, embeddings, information retrieval, classification, multilingual systems

**Engineering:** ONNX Runtime, BM25, vector search, REST/API integration, testing, CI/CD, packaging, performance optimization

**Data & analytics:** data modeling, dashboarding, business intelligence, exploratory analysis

## What I am building

I am focused on open-source AI tools that are:

- Easy to install and integrate
- Fully usable locally
- Fast enough for production workloads
- Modular and replaceable by design
- Well documented and backed by tests

## Explore more

- [All repositories](https://github.com/MANMEET75?tab=repositories)
- [Semantra Classify on PyPI](https://pypi.org/project/semantra-classify/)
- [Semantra Classify documentation](https://github.com/MANMEET75/semantra-classify#readme)

If you are building with NLP, semantic search, multilingual systems, or practical AI infrastructure, feel free to explore the projects and open an issue or discussion.

<div align="center">

### Build useful AI. Keep it open. Ship it well.

</div>
