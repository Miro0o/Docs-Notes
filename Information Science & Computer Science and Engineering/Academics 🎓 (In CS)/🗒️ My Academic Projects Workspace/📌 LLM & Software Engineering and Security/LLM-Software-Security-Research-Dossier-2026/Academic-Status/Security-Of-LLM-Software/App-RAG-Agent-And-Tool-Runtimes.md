---
ai-generated: true
last-reviewed: 2026-07-30
---

# Security Of LLM Software: Apps, RAG, Agents, MCP, And Tool Runtimes

Back: [Academic Status](../Academic-Status.md)

Scope: prompt and retrieval attacks, LLM-integrated application vulnerabilities, agent permissions and memory, MCP/tool ecosystems, action provenance, runtime resource abuse, and defenses for tool-using agents.

Checked: 2026-07-30. Execution isolation and TEE/runtime architecture papers whose main contribution is a systems boundary live in [Systems And OS Security](../Systems-And-OS-Security/Systems-And-OS-Security.md).

## Applications And Retrieval

| Key | Paper | Year | Source | Security role | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Liu2024LLMSmith | [Demystifying RCE Vulnerabilities in LLM-Integrated Apps](https://dblp.org/rec/conf/ccs/LiuDML024) | 2024 | ACM CCS / DBLP | LLM-app RCE | Shows how conventional file and command vulnerabilities surface in LLM-integrated apps. | Core |
| Hui2024PLeak | [PLeak: Prompt Leaking Attacks against Large Language Model Applications](https://dblp.org/rec/conf/ccs/0002Y0BC24) | 2024 | ACM CCS / DBLP | Prompt leakage | Extracts hidden prompts from deployed LLM applications. | Core |
| Shafran2025RAGJamming | [Machine Against the RAG: Jamming Retrieval-Augmented Generation with Blocker Documents](https://dblp.org/rec/conf/uss/ShafranSS25) | 2025 | USENIX Security / DBLP | Retrieval attack | Manipulates retrieval using adversarial blocker documents. | Core |
| Zou2025PoisonedRAG | [PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models](https://dblp.org/rec/conf/uss/ZouGW025) | 2025 | USENIX Security / DBLP | Retrieval poisoning | Corrupts knowledge bases to control downstream answers. | Core |
| Hou2025LLMAppStores | [On the (In)Security of LLM App Stores](https://dblp.org/rec/conf/sp/HouZW25) | 2025 | IEEE S&P / DBLP | Ecosystem security | Measures risks in LLM application marketplaces. | Core |

## Agent Policy, Memory, And Runtime Attacks

| Key | Paper | Year | Source | Security role | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Hu2025AgentSentinel | [AgentSentinel: An End-to-End and Real-Time Security Defense Framework for Computer-Use Agents](https://dblp.org/rec/conf/ccs/HuCZ025) | 2025 | ACM CCS / DBLP | Computer-use defense | Adds an end-to-end runtime defense for computer-use agents. | Core |
| Chen2025SecAlign | [SecAlign: Defending Against Prompt Injection with Preference Optimization](https://dblp.org/rec/conf/ccs/ChenZMC0025) | 2025 | ACM CCS / DBLP | Prompt-injection defense | Trains agent behavior against prompt-injection attacks. | Core |
| Liu2025AgentTaint | [Make Agent Defeat Agent: Automatic Detection of Taint-Style Vulnerabilities in LLM-based Agents](https://dblp.org/rec/conf/uss/Liu0LDCYYSLZ0025) | 2025 | USENIX Security / DBLP | Agent taint | Detects untrusted-data flows through agent workflows. | Core |
| Luo2026AgentDoS | [Autonomy Comes with Costs: Detecting DoS Vulnerabilities in LLM-based Agents](https://www.usenix.org/conference/usenixsecurity26/cycle1-accepted-papers) | 2026 | USENIX Security | Agent availability | Detects resource-lifecycle denial-of-service flaws. | Accepted/program record |
| Wu2026AgentPermissions | [Towards Automating Data Access Permissions in AI Agents](https://sp2026.ieee-security.org/accepted-papers.html) | 2026 | IEEE S&P | Access control | Treats agent data access as an explicit policy-synthesis problem. | Accepted/program record |
| Li2026WebCloak | [WebCloak: Characterizing and Mitigating Threats from LLM-Driven Web Agents as Intelligent Scrapers](https://sp2026.ieee-security.org/accepted-papers.html) | 2026 | IEEE S&P | Web-agent security | Characterizes and mitigates threats from intelligent scraping agents. | Accepted/program record |
| Li2026ACE | [ACE: A Security Architecture for LLM-Integrated App Systems](https://dblp.org/rec/conf/ndss/LiMRRON26) | 2026 | NDSS / DBLP | App architecture | Defines security boundaries for LLM-integrated applications. | Core |
| Syros2026SAGA | [SAGA: A Security Architecture for Governing AI Agentic Systems](https://dblp.org/rec/conf/ndss/SyrosSGNO26) | 2026 | NDSS / DBLP | Agent governance | Provides architecture-level governance for agentic systems. | Core |
| Wu2026LLMServingCache | [Cache Me, Catch You: Cache Related Security Threats in LLM Serving Frameworks](https://dblp.org/rec/conf/ndss/WuYCGQ26) | 2026 | NDSS / DBLP | Serving security | Identifies cache-related threats in LLM serving software. | Core |
| ThinkTrap2026 | [ThinkTrap: Denial-of-Service Attacks against Black-box LLM Services via Infinite Thinking](https://doi.org/10.14722/ndss.2026.240639) | 2026 | NDSS | Agent availability | Studies resource-amplification attacks against model/agent reasoning. | Core |
| Rao2026FragFuse | [FragFuse: Bypassing Access Control of Large Language Model Agents via Memory-Based Query Fragmentation and Fusion](https://www.usenix.org/conference/usenixsecurity26/presentation/rao) | 2026 | USENIX Security | Agent memory/access control | Fragments prohibited intent across memory and later fuses it to bypass policy. | Accepted/program record |
| Jiang2026MATE | [MATE: Policy-Aware Security Auditing for Mobile Agents via Synthesis-Driven Trajectory Learning](https://www.usenix.org/conference/usenixsecurity26/technical-sessions) | 2026 | USENIX Security | Mobile-agent auditing | Audits trajectories against editable natural-language security policies. | Accepted/program record |
| 2606.04329 | [From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents](https://arxiv.org/abs/2606.04329) | 2026 | arXiv | Memory poisoning | Systematically evaluates untrusted input persisted as agent memory. | Frontier |
| 2606.04425 | [What If Prompt Injection Never Left? Exploring Cross-Session Stored Prompt Injection in Agentic Systems](https://arxiv.org/abs/2606.04425) | 2026 | arXiv | Stored injection | Measures prompt injection that survives across sessions. | Frontier |
| 2606.04141 | [Caught in the Act(ivation): Toward Pre-Output and Multi-Turn Detection of Credential Exfiltration by LLM Agents](https://arxiv.org/abs/2606.04141) | 2026 | arXiv | Credential exfiltration | Detects exfiltration before output across multi-turn workflows. | Frontier |
| 2606.06460 | [Will the Agent Recuse Itself? Measuring LLM-Agent Compliance with In-Band Access-Deny Signals](https://arxiv.org/abs/2606.06460) | 2026 | arXiv | Access control | Tests whether agents honor in-band denial signals. | Frontier |

## MCP And Tool Ecosystems

| Key | Paper | Year | Source | Security role | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Kumar2026InfrastructureSentinel | [InfrastructureSentinel: Policy Enforced Guardrails for Secure MCP-driven Infrastructure Agents](https://doi.org/10.1609/aaai.v40i47.41468) | 2026 | AAAI | Infrastructure agents | Enforces policy guardrails around MCP-driven infrastructure actions. | Frontier |
| Zhao2026MCPToolchain | [Parasites in the Toolchain: A Large-Scale Analysis of Attacks on the MCP Ecosystem](https://sp2026.ieee-security.org/accepted-papers.html) | 2026 | IEEE S&P | MCP ecosystem | Measures malicious and vulnerable components across the MCP toolchain. | Accepted/program record |
| 2606.06387 | [WebMCP Tool Surface Poisoning: Runtime Manipulation Attacks on LLM Agents](https://arxiv.org/abs/2606.06387) | 2026 | arXiv | Tool poisoning | Manipulates web-exposed tool surfaces at runtime. | Frontier |
| 2606.04769 | [Description-Code Inconsistency in Real-world MCP Servers: Measurement, Detection, and Security Implications](https://arxiv.org/abs/2606.04769) | 2026 | arXiv | MCP measurement | Measures mismatches between tool descriptions and implementations. | Frontier |
| 2603.21641 | [Auditing MCP Servers for Over-Privileged Tool Capabilities](https://arxiv.org/abs/2603.21641) | 2026 | arXiv | Tool permissions | Audits excessive capabilities exposed by MCP servers. | Frontier |
| 2603.12614 | [ChainFuzzer: Greybox Fuzzing for Workflow-Level Multi-Tool Vulnerabilities in LLM Agents](https://arxiv.org/abs/2603.12614) | 2026 | arXiv | Workflow fuzzing | Fuzzes multi-tool sequences and cross-tool state. | Frontier |
| 2606.03024 | [SkillGuard: A Permission Framework for Agent Skills](https://arxiv.org/abs/2606.03024) | 2026 | arXiv | Skill permissions | Adds explicit permissions to reusable agent skills. | Frontier |
| 2606.04990 | [From Agent Traces to Trust: Evidence Tracing and Execution Provenance in LLM Agents](https://arxiv.org/abs/2606.04990) | 2026 | arXiv | Provenance | Records evidence and execution provenance across tool calls. | Frontier |

## Boundary

- Code generation and package selection: [Coding, Dependency, And Supply Chain](Coding-Dependency-And-Supply-Chain.md).
- OS/runtime isolation and TEE boundaries: [Systems And OS Security](../Systems-And-OS-Security/Systems-And-OS-Security.md).
- Agent-security surveys and benchmark views: [Cross-Cutting](../Cross-Cutting/Surveys-And-Systematization.md).
