---
ai-generated: true
---

# Benchmarks, Datasets, And Evaluation

Back: [Academic Status](Academic-Status.md)

Scope: benchmarks and evaluation platforms for code agents, vulnerability reasoning, secure code generation, CTF/cyber agents, reverse engineering, exploitability, and agent/tool security.

Sources/time: 2024-present, checked on 2026-06-06. Formal entries draw from top security (IEEE S&P, USENIX Security, ACM CCS, NDSS), SE (ICSE, ESEC/FSE and FSE/PACMSE, ASE, ISSTA), PL (POPL, PLDI, OOPSLA, ICFP, primarily through PACMPL and relevant DBLP venue pages), and AI (NeurIPS, ICML, ICLR, AAAI) venues, plus selected journal, DBLP, DOI, or official accepted-paper/program pages when noted. arXiv entries come from targeted frontier sweeps over `cs.CR`, `cs.SE`, `cs.PL`, `cs.AI`, `cs.LG`, and `cs.CL`.

## Formal Published / Accepted Papers

| Key | Benchmark / paper | Year | Source | Evaluates | Why it matters | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Jimenez2024SWEBench | [SWE-bench: Can Language Models Resolve Real-world GitHub Issues?](https://dblp.org/rec/conf/iclr/JimenezYWYPPN24) | 2024 | ICLR / DBLP | Repo-level issue resolution | Foundation baseline for realistic code agents. | Core |
| Mundler2024SWTBench | [SWT-Bench: Testing and Validating Real-World Bug-Fixes with Code Agents](https://dblp.org/rec/conf/nips/MundlerMHV24) | 2024 | NeurIPS / DBLP | Real-world bug fixes | Adds validation pressure to code-agent bug-fix tasks. | Core |
| Jain2025LiveCodeBench | [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://dblp.org/rec/conf/iclr/JainHGLYZWSSS25) | 2025 | ICLR / DBLP | Code generation | Reduces contamination risk for coding benchmarks. | Core |
| Du2024Mercury | [Mercury: A Code Efficiency Benchmark for Code Large Language Models](https://dblp.org/rec/conf/nips/DuLJLN24) | 2024 | NeurIPS / DBLP | Code efficiency | Evaluates efficiency, not only correctness. | Adjacent |
| Zhang2024NYUCTF | [NYU CTF Bench](https://dblp.org/rec/conf/nips/ShaoJUDxM0YGKKK24) | 2024 | NeurIPS / DBLP | Offensive-security CTF tasks | Open CTF benchmark for LLMs. | Core |
| Alam2024CTIBench | [CTIBench](https://dblp.org/rec/conf/nips/AlamBNR24) | 2024 | NeurIPS / DBLP | Cyber threat intelligence | Evaluates LLMs on CTI tasks. | Core |
| Xu2025SVTrustEvalC | [SV-TrustEval-C](https://dblp.org/rec/conf/sp/LiBHMKJJ25) | 2025 | IEEE S&P / DBLP | Source-code vulnerability reasoning | Tests structure/semantic reasoning under perturbation. | Negative/Evaluation |
| Chen2025CTFKnow | [CTFKnow / CTFAgent](https://arxiv.org/abs/2506.17644) | 2025 | ACM CCS / arXiv | CTF knowledge and solving | Separates knowledge from environment-grounded action. | Core |
| Wei2025JsDeObsBench | [JsDeObsBench](https://arxiv.org/abs/2506.20170) | 2025 | ACM CCS / arXiv | JavaScript deobfuscation | Reverse-engineering benchmark for LLMs. | Core |
| Jiang2026IRDecompilation | [Does Representation Matter? Evaluating IRs for LLM-based Binary Decompilation](https://www.ndss-symposium.org/ndss-paper/auto-draft-654/) | 2026 | NDSS BAR | LLM decompilation | Tests representation choices in decompilation. | Frontier |
| Nishizaka2026LLMResistantProtection | [Towards LLM-Resistant Software Protection](https://www.ndss-symposium.org/ndss-paper/auto-draft-657/) | 2026 | NDSS BAR | CTF reverse-engineering agents | Maps agent failure modes in reverse engineering. | Frontier |

## arXiv / Frontier Preprints

| Key | Benchmark / paper | Year | Source | Evaluates | Why it matters | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Bhatt2024CyberSecEval2 | [CyberSecEval 2](https://arxiv.org/abs/2404.13161) | 2024 | arXiv | Cybersecurity risks/capabilities | Broad model cyber-risk evaluation. | Negative/Evaluation |
| Bhatt2024CyberSecEval3 | [CyberSecEval 3](https://arxiv.org/abs/2408.01605) | 2024 | arXiv | Cybersecurity risks/capabilities | Expanded cyber evaluation suite. | Negative/Evaluation |
| Zhang2024Cybench | [Cybench](https://arxiv.org/abs/2408.08926) | 2024 | arXiv | Cybersecurity agents | Interactive cyber task benchmark. | Core |
| Wang2024SeCodePLT | [SeCodePLT](https://arxiv.org/abs/2410.11096) | 2024 | arXiv | Security of code GenAI | Unified platform for secure-code-generation evaluation. | Negative/Evaluation |
| Zhou2025SafeGenBench | [SafeGenBench](https://arxiv.org/abs/2506.05692) | 2025 | arXiv | Vulnerability detection in generated code | Tests security of LLM-generated code. | Negative/Evaluation |
| Ali2025SecureVibeBench | [SecureVibeBench](https://arxiv.org/abs/2509.22097) | 2025 | arXiv | Multi-file secure coding tasks | Evaluates code agents with security oracles. | Frontier |
| Shao2025CyberGym | [CyberGym](https://arxiv.org/abs/2506.02548) | 2025 | arXiv | Real vulnerabilities across codebases | Pushes evaluation toward large-codebase security tasks. | Frontier |
| Patel2026ExploitBench | [ExploitBench](https://arxiv.org/abs/2605.14153) | 2026 | arXiv | Exploit agents | Capability-ladder scoring for exploit-agent progress. | Frontier |
| 2603.10969 | [TOSSS: a CVE-based Software Security Benchmark for Large Language Models](https://arxiv.org/abs/2603.10969) | 2026 | arXiv | CVE-based software-security tasks | Adds CVE-oriented benchmark pressure. | Frontier |
| 2604.03750 | [CREBench: Evaluating Large Language Models in Cryptographic Binary Reverse Engineering](https://arxiv.org/abs/2604.03750) | 2026 | arXiv | Crypto binary RE | Domain-specific reverse-engineering benchmark. | Frontier |
| 2606.05920 | [Asuka-Bench](https://arxiv.org/abs/2606.05920) | 2026 | arXiv | Code-agent refinement | Underspecified intent and multi-round refinement. | Frontier |
| 2606.05249 | [SWE-InfraBench](https://arxiv.org/abs/2606.05249) | 2026 | arXiv | Cloud infrastructure code | IaC tasks where security/reliability are linked. | Frontier |
| 2606.05570 | [TensorBench](https://arxiv.org/abs/2606.05570) | 2026 | arXiv | Compiler-backed code-agent tasks | Reliable compiler-based validation. | Frontier |
| 2606.05574 | [SmellBench](https://arxiv.org/abs/2606.05574) | 2026 | arXiv | Refactoring/code-smell tasks | Fine-grained code-agent evaluation. | Frontier |
| 2606.05844 | [GenTI](https://arxiv.org/abs/2606.05844) | 2026 | arXiv | IDPS rule generation | Evaluates autonomous detection-rule generation. | Frontier |
| 2606.04769 | [Description-Code Inconsistency in Real-world MCP Servers](https://arxiv.org/abs/2606.04769) | 2026 | arXiv | MCP server security | Measurement dataset for MCP description/code mismatch. | Frontier |
| 2606.05493 | [REStack](https://arxiv.org/abs/2606.05493) | 2026 | arXiv | Reverse-engineering discussions | Dataset for reverse-engineering knowledge/workflows. | Frontier |

## Notes

- Strong benchmarks use dynamic oracles, real repositories, validated vulnerabilities, or reproducible environments.
- Weak benchmarks ask only for labels on small snippets or rely on LLM-as-judge without an independent oracle.
