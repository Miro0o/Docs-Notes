---
ai-generated: true
---

# LLM App, Agent, And Security-Tool Attack Surfaces

Back: [Academic Status](Academic-Status.md)

Scope: risks introduced by LLM apps, coding assistants, security tools, RAG, MCP/tool protocols, agent permissions, execution isolation, prompt/tool injection, package hallucination, and agent resource governance.

Sources/time: 2024-present, checked on 2026-06-06. Formal entries draw from top security (IEEE S&P, USENIX Security, ACM CCS, NDSS), SE (ICSE, ESEC/FSE and FSE/PACMSE, ASE, ISSTA), PL (POPL, PLDI, OOPSLA, ICFP, primarily through PACMPL and relevant DBLP venue pages), and AI (NeurIPS, ICML, ICLR, AAAI) venues, plus selected journal, DBLP, DOI, or official accepted-paper/program pages when noted. arXiv entries come from targeted frontier sweeps over `cs.CR`, `cs.SE`, `cs.PL`, `cs.AI`, `cs.LG`, and `cs.CL`.

## Formal Published / Accepted Papers

| Key | Paper | Year | Source | Area fit | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Yan2024CodeBreaker | [An LLM-Assisted Easy-to-Trigger Backdoor Attack on Code Completion Models](https://dblp.org/rec/conf/uss/YanWDHLKH24) | 2024 | USENIX Security / DBLP | Code-model poisoning | LLM-assisted backdoor payloads for code completion models. | Core |
| Liu2024LLMSmith | [Demystifying RCE Vulnerabilities in LLM-Integrated Apps](https://dblp.org/rec/conf/ccs/LiuDML024) | 2024 | ACM CCS / DBLP | LLM app RCE | Shows conventional RCE/file risks in LLM-integrated apps. | Core |
| Hui2024PLeak | [PLeak: Prompt Leaking Attacks against Large Language Model Applications](https://dblp.org/rec/conf/ccs/0002Y0BC24) | 2024 | ACM CCS / DBLP | Prompt leakage | Prompt-extraction attacks against LLM applications. | Adjacent |
| Klemmer2024AIAssistantsSecurity | [Using AI Assistants in Software Development: A Qualitative Study on Security Practices and Concerns](https://dblp.org/rec/conf/ccs/KlemmerHPLBPMRV24) | 2024 | ACM CCS / DBLP | Developer security practice | Human/practice evidence around AI assistant security. | Adjacent |
| Zhang2025IsolateGPT | [IsolateGPT: An Execution Isolation Architecture for LLM-Based Agentic Systems](https://www.ndss-symposium.org/wp-content/uploads/2025-1131-paper.pdf) | 2025 | NDSS | Execution isolation | Treats LLM-agent execution as systems security. | Core |
| Spracklen2025PackageHallucinations | [We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs](https://dblp.org/rec/conf/uss/SpracklenWSMV25) | 2025 | USENIX Security / DBLP | Package supply chain | Measures hallucinated dependencies and attack opportunities. | Core |
| Li2025CodeGuarder | [Give LLMs a Security Course: Securing Retrieval-Augmented Code Generation via Knowledge Injection](https://dblp.org/rec/conf/ccs/LinWQCM25) | 2025 | ACM CCS / DBLP | Secure RAG coding | Adds security knowledge to RAG code generation. | Core |
| Ye2025ImportSnare | [ImportSnare: Directed 'Code Manual' Hijacking in Retrieval-Augmented Code Generation](https://dblp.org/rec/conf/ccs/YeSQ25) | 2025 | ACM CCS / DBLP | RAG/code supply chain | Shows retrieval/code-manual hijacking against code generation. | Core |
| Hu2025AgentSentinel | [AgentSentinel: An End-to-End and Real-Time Security Defense Framework for Computer-Use Agents](https://dblp.org/rec/conf/ccs/HuCZ025) | 2025 | ACM CCS / DBLP | Computer-use agents | Real-time defense framework for computer-use agents. | Core |
| Chen2025SecAlign | [SecAlign: Defending Against Prompt Injection with Preference Optimization](https://dblp.org/rec/conf/ccs/ChenZMC0025) | 2025 | ACM CCS / DBLP | Prompt injection defense | Preference optimization defense against prompt injection. | Core |
| Shafran2025RAGJamming | [Machine Against the RAG: Jamming Retrieval-Augmented Generation with Blocker Documents](https://dblp.org/rec/conf/uss/ShafranSS25) | 2025 | USENIX Security / DBLP | RAG attack | Blocks/manipulates RAG using adversarial documents. | Core |
| Zou2025PoisonedRAG | [PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models](https://dblp.org/rec/conf/uss/ZouGW025) | 2025 | USENIX Security / DBLP | RAG poisoning | Corrupts RAG knowledge bases. | Core |
| Liu2025AgentTaint | [Make Agent Defeat Agent: Automatic Detection of Taint-Style Vulnerabilities in LLM-based Agents](https://dblp.org/rec/conf/uss/Liu0LDCYYSLZ0025) | 2025 | USENIX Security / DBLP | Agent vulnerability detection | Detects taint-style vulnerabilities in LLM agents. | Core |
| Hou2025LLMAppStores | [On the (In)Security of LLM App Stores](https://dblp.org/rec/conf/sp/HouZW25) | 2025 | IEEE S&P / DBLP | LLM app stores | Security study of LLM app-store ecosystems. | Core |
| Luo2026AgentDoS | [Autonomy Comes with Costs: Detecting DoS Vulnerabilities in LLM-based Agents](https://www.usenix.org/conference/usenixsecurity26/cycle1-accepted-papers) | 2026 | USENIX Security | Agent resource risk | Finds resource-lifecycle DoS vulnerabilities in agents. | Core |
| Wu2026AgentPermissions | [Towards Automating Data Access Permissions in AI Agents](https://sp2026.ieee-security.org/accepted-papers.html) | 2026 | IEEE S&P | Agent permissions | Treats agent data access as a security policy problem. | Core |
| Li2026WebCloak | [WebCloak: Characterizing and Mitigating Threats from LLM-Driven Web Agents as Intelligent Scrapers](https://sp2026.ieee-security.org/accepted-papers.html) | 2026 | IEEE S&P | Web agents | Characterizes threats from LLM-driven web agents. | Core |
| Li2026ACE | [ACE: A Security Architecture for LLM-Integrated App Systems](https://dblp.org/rec/conf/ndss/LiMRRON26) | 2026 | NDSS / DBLP | LLM app architecture | Security architecture for LLM-integrated apps. | Core |
| Syros2026SAGA | [SAGA: A Security Architecture for Governing AI Agentic Systems](https://dblp.org/rec/conf/ndss/SyrosSGNO26) | 2026 | NDSS / DBLP | Agent governance | Architecture for governing agentic systems. | Core |
| Wu2026LLMServingCache | [Cache Me, Catch You: Cache Related Security Threats in LLM Serving Frameworks](https://dblp.org/rec/conf/ndss/WuYCGQ26) | 2026 | NDSS / DBLP | LLM serving security | Cache-related threats in LLM serving frameworks. | Core |
| Gadey2026TEEAnnotations | [Automated Code Annotation with LLMs for Establishing TEE Boundaries](https://dblp.org/rec/conf/ndss/GadeyGSSD26) | 2026 | NDSS / DBLP | TEE boundary tooling | LLM-assisted code annotation for TEE boundaries. | Adjacent |
| Kumar2026InfrastructureSentinel | [InfrastructureSentinel: Policy Enforced Guardrails for Secure MCP-driven Infrastructure Agents](https://doi.org/10.1609/aaai.v40i47.41468) | 2026 | AAAI | MCP infrastructure agents | Guardrails for infrastructure agents using MCP. | Frontier |

## arXiv / Frontier Preprints

| Key | Paper | Year | Source | Area fit | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| 2606.06387 | [WebMCP Tool Surface Poisoning: Runtime Manipulation Attacks on LLM Agents](https://arxiv.org/abs/2606.06387) | 2026 | arXiv | WebMCP attack | Runtime manipulation attacks on web-exposed MCP tools. | Frontier |
| 2606.04769 | [Description-Code Inconsistency in Real-world MCP Servers: Measurement, Detection, and Security Implications](https://arxiv.org/abs/2606.04769) | 2026 | arXiv | MCP measurement | Measures mismatch between tool descriptions and code in MCP servers. | Frontier |
| 2603.21641 | [Auditing MCP Servers for Over-Privileged Tool Capabilities](https://arxiv.org/abs/2603.21641) | 2026 | arXiv | MCP permissions | Audits over-privileged tool capabilities in MCP servers. | Frontier |
| 2603.12614 | [ChainFuzzer: Greybox Fuzzing for Workflow-Level Multi-Tool Vulnerabilities in LLM Agents](https://arxiv.org/abs/2603.12614) | 2026 | arXiv | Agent workflow fuzzing | Fuzzes multi-tool workflow vulnerabilities in LLM agents. | Frontier |
| 2602.20717 | [PackMonitor: Enabling Zero Package Hallucinations Through Decoding-Time Monitoring](https://arxiv.org/abs/2602.20717) | 2026 | arXiv | Package hallucination defense | Monitors dependency suggestions during decoding. | Frontier |
| 2602.00667 | [zkCraft: Prompt-Guided LLM as a Zero-Shot Mutation Pattern Oracle for TCCT-Powered ZK Fuzzing](https://arxiv.org/abs/2602.00667) | 2026 | arXiv | Agent/tool-assisted fuzzing | Relevant as a prompt-guided domain-specific tool pipeline. | Frontier |
| 2606.03895 | [Agent libOS: A Library-OS-Inspired Runtime for Long-Running, Capability-Controlled LLM Agents](https://arxiv.org/abs/2606.03895) | 2026 | arXiv | Agent runtime | Runtime model for capability-controlled long-running agents. | Frontier |
| 2606.03024 | [SkillGuard: A Permission Framework for Agent Skills](https://arxiv.org/abs/2606.03024) | 2026 | arXiv | Skill permissions | Permission framework for reusable agent skills. | Frontier |
| 2606.04990 | [From Agent Traces to Trust: Evidence Tracing and Execution Provenance in LLM Agents](https://arxiv.org/abs/2606.04990) | 2026 | arXiv | Provenance | Evidence/provenance layer for LLM agents. | Frontier |
| 2606.04329 | [From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents](https://arxiv.org/abs/2606.04329) | 2026 | arXiv | Agent memory poisoning | Systematic study of memory poisoning in LLM agents. | Frontier |
| 2606.04425 | [What If Prompt Injection Never Left? Exploring Cross-Session Stored Prompt Injection in Agentic Systems](https://arxiv.org/abs/2606.04425) | 2026 | arXiv | Stored prompt injection | Cross-session stored prompt injection in stateful agents. | Frontier |
| 2606.04141 | [Caught in the Act(ivation): Toward Pre-Output and Multi-Turn Detection of Credential Exfiltration by LLM Agents](https://arxiv.org/abs/2606.04141) | 2026 | arXiv | Credential exfiltration | Detection approaches for agent credential exfiltration. | Frontier |
| 2606.06460 | [Will the Agent Recuse Itself? Measuring LLM-Agent Compliance with In-Band Access-Deny Signals](https://arxiv.org/abs/2606.06460) | 2026 | arXiv | Access control | Measures whether agents comply with access-deny signals. | Frontier |
| 2606.05647 | [Coding with "Enemy": Can Human Developers Detect AI Agent Sabotage?](https://arxiv.org/abs/2606.05647) | 2026 | arXiv | Coding-agent sabotage | Studies whether humans notice malicious/sabotaging code agents. | Frontier |

## Notes

- This area is now central, not peripheral: LLM-for-security tools create their own attack surfaces.
- MCP/security-tool orchestration is a fast-moving 2026 frontier; treat arXiv entries here as high-priority but not yet settled.
