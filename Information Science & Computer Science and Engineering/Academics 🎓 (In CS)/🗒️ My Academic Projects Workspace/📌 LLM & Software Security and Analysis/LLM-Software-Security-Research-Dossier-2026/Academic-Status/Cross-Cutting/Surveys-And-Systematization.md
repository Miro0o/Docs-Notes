---
ai-generated: true
last-reviewed: 2026-07-30
---

# Cross-Cutting: Surveys And Systematization

Back: [Academic Status](../Academic-Status.md)

Scope: surveys, SoKs, research agendas, and methodological critiques that organize the LLM/software-security space.

Checked: 2026-07-30. Use these sources for orientation and source mining; validate technical claims against primary method/evaluation papers.

## Canonical Literature

| Key | Paper | Year | Source | Coverage | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Zhu2025SoftwareSecuritySurvey | [When Software Security Meets Large Language Models: A Survey](https://doi.org/10.1109/JAS.2024.124971) | 2025 | IEEE/CAA JAS | Broad software security | Maps major LLM/software-security task families. | Survey |
| Fan2025LLMSupplyChainAgenda | [Large Language Model Supply Chain: A Research Agenda](https://doi.org/10.1145/3708531) | 2025 | ACM TOSEM | Supply chain | Connects data, model, retrieval, tool, and package supply chains. | Survey |
| Hu2025AVRSoK | [SoK: Automated Vulnerability Repair: Methods, Tools, and Assessments](https://dblp.org/rec/conf/uss/Hu0SGZXY025) | 2025 | USENIX Security / DBLP | Vulnerability repair | Systematizes methods, tools, and assessment criteria. | Survey |
| SoK2025EffectiveAVR | [SoK: Towards Effective Automated Vulnerability Repair](https://dblp.org/rec/conf/uss/0095SW0025) | 2025 | USENIX Security / DBLP | Vulnerability repair | Focuses on requirements for effective, validated repair. | Survey |
| Tihanyi2025DigitalCyberExpert | [The Digital Cybersecurity Expert: How Far Have We Come?](https://arxiv.org/abs/2504.11783) | 2025 | IEEE S&P / arXiv | Cyber capability | Calibrates broad “digital cyber expert” claims. | Negative/Evaluation |
| Sheng2025LLMSoftwareSecuritySurvey | [LLMs in Software Security: A Survey of Vulnerability Detection Techniques and Insights](https://doi.org/10.48550/arXiv.2502.07049) | 2025 | arXiv | Vulnerability detection | Surveys detection methods and persistent evaluation weaknesses. | Survey |
| Alam2026PHILTER | [SoK: PHILTER: Uncovering Security and Functional Gaps in AI-based Phishing Website Detection Literature via an LLM-based Reasoning Framework](https://www.usenix.org/conference/usenixsecurity26/cycle1-accepted-papers) | 2026 | USENIX Security | LLM-assisted review | Demonstrates an expert-validated LLM-assisted evidence-synthesis workflow. | Accepted/program record |
| Evertz2026Pitfalls | [Chasing Shadows: Pitfalls in LLM Security Research](https://dblp.org/rec/conf/ndss/EvertzRNMNSGPSS26) | 2026 | NDSS / DBLP | Research methodology | Identifies recurring validity and evaluation pitfalls. | Negative/Evaluation |
| SoK2026AIxCC | [SoK: DARPA’s AI Cyber Challenge (AIxCC): Competition Design, Architectures, and Lessons Learned](https://arxiv.org/abs/2602.07666) | 2026 | USENIX Security / arXiv | Cyber-reasoning systems | Systematizes competition design and CRS architecture lessons. | Survey |
| Kim2026AgenticAISoK | [SoK: Attack and Defense Landscape of Agentic AI Systems](https://www.usenix.org/conference/usenixsecurity26/technical-sessions) | 2026 | USENIX Security | Agent security | Organizes agent architecture, attacks, and defenses. | Accepted/program record |

## Reading Guidance

- Begin with the methodological critiques (`Evertz2026Pitfalls`, detector reliability papers) before claims-heavy surveys.
- For AIxCC, distinguish competition architecture from independently replicated security performance.
- For agent security, separate application-layer prompt/memory failures from OS/runtime isolation failures.
- The broad SE/HCI survey `2603.13411` is canonical in the sibling [Surveys and Systematization](../../../LLM-Software-Research-Dossier-2026/Academic-Status/Surveys-And-Systematization.md) page; security-fuzzing work may cite it without duplicating its paper row.
