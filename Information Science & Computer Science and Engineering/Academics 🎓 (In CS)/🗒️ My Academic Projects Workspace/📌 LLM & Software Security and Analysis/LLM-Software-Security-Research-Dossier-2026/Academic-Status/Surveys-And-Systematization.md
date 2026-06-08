---
ai-generated: true
---

# Surveys And Systematization

Back: [Academic Status](Academic-Status.md)

Scope: surveys, SoKs, research agendas, meta-evaluation, and systematic studies that organize the LLM/software-security space.

Sources/time: 2024-present, checked on 2026-06-06. Formal entries draw from top security (IEEE S&P, USENIX Security, ACM CCS, NDSS), SE (ICSE, ESEC/FSE and FSE/PACMSE, ASE, ISSTA), PL (POPL, PLDI, OOPSLA, ICFP, primarily through PACMPL and relevant DBLP venue pages), and AI (NeurIPS, ICML, ICLR, AAAI) venues, plus selected journal, DBLP, DOI, or official accepted-paper/program pages when noted. arXiv entries come from targeted frontier sweeps over `cs.CR`, `cs.SE`, `cs.PL`, `cs.AI`, `cs.LG`, and `cs.CL`.

## Formal Published / Accepted Papers

| Key | Paper | Year | Source | Area fit | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Zhu2025SoftwareSecuritySurvey | [When Software Security Meets Large Language Models: A Survey](https://doi.org/10.1109/JAS.2024.124971) | 2025 | IEEE/CAA JAS | Software-security survey | General survey of LLM/software-security intersections. | Survey |
| Fan2025LLMSupplyChainAgenda | [Large Language Model Supply Chain: A Research Agenda](https://doi.org/10.1145/3708531) | 2025 | ACM TOSEM | Supply-chain agenda | Frames data/model/tool/RAG/package supply-chain risks. | Survey |
| Alam2026PHILTER | [SoK: PHILTER: Uncovering Security and Functional Gaps in AI-based Phishing Website Detection Literature via an LLM-based Reasoning Framework](https://www.usenix.org/conference/usenixsecurity26/cycle1-accepted-papers) | 2026 | USENIX Security | LLM-assisted review | Example of LLM-assisted literature review with expert validation. | Adjacent |
| Hu2025AVRSoK | [SoK: Automated Vulnerability Repair: Methods, Tools, and Assessments](https://dblp.org/rec/conf/uss/Hu0SGZXY025) | 2025 | USENIX Security / DBLP | AVR SoK | Reviews automated vulnerability repair methods and assessment. | Survey |
| SoK2025EffectiveAVR | [SoK: Towards Effective Automated Vulnerability Repair](https://dblp.org/rec/conf/uss/0095SW0025) | 2025 | USENIX Security / DBLP | AVR SoK | Focuses on requirements for effective vulnerability repair. | Survey |
| Evertz2026Pitfalls | [Chasing Shadows: Pitfalls in LLM Security Research](https://dblp.org/rec/conf/ndss/EvertzRNMNSGPSS26) | 2026 | NDSS / DBLP | Meta-evaluation | Discusses methodological pitfalls in LLM security research. | Negative/Evaluation |
| Tihanyi2025DigitalCyberExpert | [The Digital Cybersecurity Expert: How Far Have We Come?](https://arxiv.org/abs/2504.11783) | 2025 | IEEE S&P / arXiv | Capability evaluation | Broad calibration of LLM cybersecurity expertise claims. | Adjacent |

## arXiv / Frontier Preprints

| Key | Paper | Year | Source | Area fit | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Sheng2025LLMSoftwareSecuritySurvey | [LLMs in Software Security: A Survey of Vulnerability Detection Techniques and Insights](https://doi.org/10.48550/arXiv.2502.07049) | 2025 | arXiv | Vulnerability-detection survey | Broad orientation for LLM-based vulnerability detection. | Survey |
| SoK2026AIxCC | [SoK: DARPA's AI Cyber Challenge (AIxCC): Competition Design, Architectures, and Lessons Learned](https://arxiv.org/abs/2605.16910) | 2026 | arXiv | CRS SoK | Systematizes AIxCC cyber-reasoning architecture lessons. | Survey |
| 2603.13411 | [Human in the Loop for Fuzz Testing: Literature Review and the Road Ahead](https://arxiv.org/abs/2603.13411) | 2026 | arXiv | Fuzzing review | Reviews human-in-the-loop fuzzing, relevant to LLM-assisted fuzzing. | Survey |
| 2603.25146 | [Factors Influencing the Quality of AI-Generated Code: A Synthesis of Empirical Evidence](https://arxiv.org/abs/2603.25146) | 2026 | arXiv | Generated-code quality | Synthesizes empirical evidence on AI-generated code quality. | Survey |
| 2606.03394 | [Human-AI Collaboration and the Transformation of Software Engineering Work](https://arxiv.org/abs/2606.03394) | 2026 | arXiv | Human/SE transformation | Socio-technical context for code-agent adoption. | Adjacent |
| 2606.05608 | [The End of Software Engineering: How AI Agents Are Fundamentally Restructuring the Software Paradigm](https://arxiv.org/abs/2606.05608) | 2026 | arXiv | Position / roadmap | Speculative but useful for agent-era SE framing. | Adjacent |

## Notes

- Use surveys for orientation and source mining, not as final evidence for technical claims.
- Prefer SoKs that include clear inclusion criteria, source traceability, and expert validation.
