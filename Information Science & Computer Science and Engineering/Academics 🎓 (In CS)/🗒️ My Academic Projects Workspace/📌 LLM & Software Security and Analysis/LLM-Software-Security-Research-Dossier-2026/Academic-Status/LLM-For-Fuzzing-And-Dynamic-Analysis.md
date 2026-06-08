---
ai-generated: true
---

# LLM For Fuzzing And Dynamic Analysis

Back: [Academic Status](Academic-Status.md)

Scope: LLM-guided fuzzing, fuzz harness generation, structured input synthesis, protocol/device fuzzing, dynamic validation, and execution-feedback loops.

Sources/time: 2024-present, checked on 2026-06-06. Formal entries draw from top security (IEEE S&P, USENIX Security, ACM CCS, NDSS), SE (ICSE, ESEC/FSE and FSE/PACMSE, ASE, ISSTA), PL (POPL, PLDI, OOPSLA, ICFP, primarily through PACMPL and relevant DBLP venue pages), and AI (NeurIPS, ICML, ICLR, AAAI) venues, plus selected journal, DBLP, DOI, or official accepted-paper/program pages when noted. arXiv entries come from targeted frontier sweeps over `cs.CR`, `cs.SE`, `cs.PL`, `cs.AI`, `cs.LG`, and `cs.CL`.

## Formal Published / Accepted Papers

| Key | Paper | Year | Source | Area fit | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Zhou2024LLMIF | [LLMIF: Augmented Large Language Model for Fuzzing IoT Devices](https://dblp.org/rec/conf/sp/WangYL24) | 2024 | IEEE S&P / DBLP | IoT fuzzing | Early top-venue signal that LLMs can add semantic guidance to IoT fuzzing. | Core |
| Meng2024ProtocolFuzzing | [Large Language Model Guided Protocol Fuzzing](https://dblp.org/rec/conf/ndss/MengMBR24) | 2024 | NDSS / DBLP | Protocol fuzzing | Uses LLMs to infer protocol structure and guide fuzzing. | Core |
| Xia2024Fuzz4All | [Fuzz4All: Universal Fuzzing with Large Language Models](https://dblp.org/rec/conf/icse/XiaPTP024) | 2024 | ICSE / DBLP | Universal fuzzing | Generates structured inputs across compilers, solvers, runtimes, and libraries. | Core |
| Deng2024FuzzGPT | [Large Language Models are Edge-Case Generators: Crafting Unusual Programs for Fuzzing Deep Learning Libraries](https://dblp.org/rec/conf/icse/DengXYZY024) | 2024 | ICSE / DBLP | DL-library fuzzing | Uses historical bug knowledge to generate unusual programs. | Core |
| Feng2024AndroidBugReplay | [Prompting Is All You Need: Automated Android Bug Replay with Large Language Models](https://dblp.org/rec/conf/icse/FengC24) | 2024 | ICSE / DBLP | Dynamic replay | Uses LLMs to replay Android bugs. | Adjacent |
| Su2024ExploratoryTesting | [Enhancing Exploratory Testing by Large Language Model and Knowledge Graph](https://dblp.org/rec/conf/icse/SuLXHX0024) | 2024 | ICSE / DBLP | Exploratory testing | Combines LLM and KG for exploratory testing. | Adjacent |
| Zhang2024FuzzDrivers | [How Effective Are They? Exploring Large Language Model Based Fuzz Driver Generation](https://dblp.org/rec/conf/issta/ZhangZBL0XLS24) | 2024 | ISSTA / DBLP | Harness evaluation | Evaluates limits of LLM-generated fuzz drivers. | Negative/Evaluation |
| Wang2024ProphetFuzz | [ProphetFuzz: Fully Automated Prediction and Fuzzing of High-Risk Option Combinations with Only Documentation via Large Language Model](https://dblp.org/rec/conf/ccs/WangZ00M24) | 2024 | ACM CCS / DBLP | Documentation-guided fuzzing | Mines docs for risky option combinations. | Core |
| Lyu2024PromptFuzzing | [Prompt Fuzzing for Fuzz Driver Generation](https://dblp.org/rec/conf/ccs/LyuXCC24) | 2024 | ACM CCS / DBLP | Harness generation | Uses prompt strategies to generate fuzz drivers. | Core |
| Lyu2024LiftFuzz | [LiftFuzz: Validating Binary Lifters through Context-aware Fuzzing with GPT](https://dblp.org/rec/conf/ccs/ZhouYSZCZ24) | 2024 | ACM CCS / DBLP | Binary-lifter fuzzing | Uses GPT context to validate binary lifters. | Core |
| Asmita2024BusyBox | [Fuzzing BusyBox: Leveraging LLM and Crash Reuse for Embedded Bug Unearthing](https://dblp.org/rec/conf/uss/AsmitaOSTFH24) | 2024 | USENIX Security / DBLP | Embedded fuzzing | Combines LLM guidance and crash reuse for BusyBox. | Core |
| Ma2024MatterFuzzing | [From One Thousand Pages of Specification to Unveiling Hidden Bugs: Large Language Model Assisted Fuzzing of Matter IoT Devices](https://dblp.org/rec/conf/uss/MaL024) | 2024 | USENIX Security / DBLP | Spec-guided IoT fuzzing | Turns large protocol specs into fuzzing guidance. | Core |
| Yang2024WhiteFox | [WhiteFox: White-Box Compiler Fuzzing Empowered by Large Language Models](https://dblp.org/rec/journals/pacmpl/YangDLY0J024) | 2024 | PACMPL / DBLP | Compiler fuzzing | Uses LLMs inside white-box compiler fuzzing. | Core |
| Zhang2025PromeFuzz | [PromeFuzz: A Knowledge-Driven Approach to Fuzzing Harness Generation with Large Language Models](https://dblp.org/rec/conf/ccs/LiuDJWWHWS25) | 2025 | ACM CCS / DBLP | Harness generation | Knowledge-driven harness generation with LLMs. | Core |
| Yang2025HyLLFuzz | [Hybrid Language Processor Fuzzing via LLM-Based Constraint Solving](https://dblp.org/rec/conf/uss/YangYCL25) | 2025 | USENIX Security / DBLP | Constraint solving | Uses LLMs to solve constraints for language-processor fuzzing. | Core |
| Chen2025ELFuzz | [ELFuzz: Efficient Input Generation via LLM-driven Synthesis Over Fuzzer Space](https://dblp.org/rec/conf/uss/ChenDC25) | 2025 | USENIX Security / DBLP | Input generation | Synthesizes over fuzzer space to improve input generation. | Core |
| Zhang2025NonTextualFuzzing | [Low-Cost and Comprehensive Non-textual Input Fuzzing with LLM-Synthesized Input Generators](https://dblp.org/rec/conf/uss/ZhangLW0025) | 2025 | USENIX Security / DBLP | Non-textual fuzzing | Generates input generators for non-textual fuzzing. | Core |
| Gao2025Clozemaster | [Clozemaster: Fuzzing Rust Compiler by Harnessing LLMs for Infilling Masked Real Programs](https://dblp.org/rec/conf/icse/GaoYSWZX25) | 2025 | ICSE / DBLP | Rust compiler fuzzing | Uses infilling of real programs to fuzz the Rust compiler. | Core |
| Shree2025ReFuzzer | [ReFuzzer: Feedback-Driven Approach to Enhance Validity of LLM-Generated Test Programs](https://dblp.org/rec/conf/kbse/ShreeER25) | 2025 | ASE / DBLP | Test-program validity | Improves generated test-program validity using feedback. | Core |
| Kim2025LlamaRestTest | [LlamaRestTest: Effective REST API Testing with Small Language Models](https://dblp.org/rec/journals/pacmse/KimSO25) | 2025 | FSE/PACMSE / DBLP | REST API testing | Uses smaller language models for REST API testing. | Adjacent |
| Zhang2025KernelRAG | [Unlocking Low Frequency Syscalls in Kernel Fuzzing with Dependency-Based RAG](https://dblp.org/rec/journals/pacmse/ZhangLLC25) | 2025 | FSE/PACMSE / DBLP | Kernel fuzzing | Uses dependency-based RAG to unlock low-frequency syscalls. | Core |
| Ma2025OpDiffer | [OpDiffer: LLM-Assisted Opcode-Level Differential Testing of Ethereum Virtual Machine](https://dblp.org/rec/journals/pacmse/MaHXXWGY25) | 2025 | FSE/PACMSE / DBLP | Differential testing | LLM-assisted opcode-level testing for EVM. | Core |
| Shiraishi2026PILOT | [PILOT: Command-line Interface Fuzzing via Path-Guided, Iterative Large Language Model Prompting](https://sp2026.ieee-security.org/accepted-papers.html) | 2026 | IEEE S&P | CLI fuzzing | Generates option/input combinations using path feedback. | Core |
| Li2026DeepSURF | [deepSURF: Detecting Memory Safety Vulnerabilities in Rust Through Fuzzing LLM-Augmented Harnesses](https://arxiv.org/abs/2506.15648) | 2026 | IEEE S&P / arXiv | Rust harness generation | Targets Rust-specific harness complexity around unsafe code. | Core |
| Jia2026PANGOLIN | [PANGOLIN: Fuzzing Multilingual IoT Firmware with LLM-Driven Code Analysis](https://www.usenix.org/conference/usenixsecurity26/cycle1-accepted-papers) | 2026 | USENIX Security | Firmware fuzzing | Bridges C and scripting-language firmware logic. | Core |
| Ji2026FirmAgent | [FirmAgent: Leveraging Fuzzing to Assist LLM Agents with IoT Firmware Vulnerability Discovery](https://dblp.org/rec/conf/ndss/JiZGJLLZJ26) | 2026 | NDSS / DBLP | Firmware fuzzing | Uses fuzzing to ground LLM-agent firmware analysis. | Core |
| Yang2026BSFuzzer | [BSFuzzer: Context-Aware Semantic Fuzzing for BLE Logic Flaw Detection](https://www.ndss-symposium.org/ndss-paper/bsfuzzer-context-aware-semantic-fuzzing-for-ble-logic-flaw-detection/) | 2026 | NDSS | BLE fuzzing | LLM agent parses BLE spec and validates device responses. | Core |
| Liu2026IoTBec | [IoTBec: Firmware- and Source-Code-Independent Recurring Vulnerability Detection with LLM-Driven Fuzzing](https://www.ndss-symposium.org/ndss-program/symposium-2026/) | 2026 | NDSS | Black-box IoT fuzzing | Detects recurring vulnerabilities without firmware/source access. | Core |
| Zhang2026LogicFuzz | [LogicFuzz: An LLM-Driven Fuzzing Framework for Detecting Logic Instruction Bugs in PLCs](https://dblp.org/rec/conf/ndss/ChengZWCWQS26) | 2026 | NDSS / DBLP | PLC fuzzing | LLM-guided fuzzing for industrial-control logic bugs. | Core |

## arXiv / Frontier Preprints

| Key | Paper | Year | Source | Area fit | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| 2603.08616 | [Coverage-Guided Multi-Agent Harness Generation for Java Library Fuzzing](https://arxiv.org/abs/2603.08616) | 2026 | arXiv | Harness generation | Multi-agent harness generation with coverage feedback. | Frontier |
| 2602.19490 | [FuzzySQL: Uncovering Hidden Vulnerabilities in DBMS Special Features with LLM-Driven Fuzzing](https://arxiv.org/abs/2602.19490) | 2026 | arXiv | DBMS fuzzing | LLM-driven fuzzing for obscure DBMS features. | Frontier |
| 2602.11209 | [SAFuzz: Semantic-Guided Adaptive Fuzzing for LLM-Generated Code](https://arxiv.org/abs/2602.11209) | 2026 | arXiv | Generated-code fuzzing | Tests LLM-generated code with semantic-guided adaptive fuzzing. | Frontier |
| 2602.23065 | [LLM-Powered Silent Bug Fuzzing in Deep Learning Libraries via Versatile and Controlled Bug Transfer](https://arxiv.org/abs/2602.23065) | 2026 | arXiv | DL-library fuzzing | Targets silent bugs rather than only crashes. | Frontier |
| 2602.00667 | [zkCraft: Prompt-Guided LLM as a Zero-Shot Mutation Pattern Oracle for TCCT-Powered ZK Fuzzing](https://arxiv.org/abs/2602.00667) | 2026 | arXiv | ZK fuzzing | Uses an LLM as mutation-pattern oracle for zero-knowledge circuit fuzzing. | Frontier |
| 2604.01442 | [Fuzzing with Agents? Generators Are All You Need](https://arxiv.org/abs/2604.01442) | 2026 | arXiv | Agentic fuzzing critique | Compares agentic fuzzing with generator-based approaches. | Frontier |

## Notes

- Strong work here keeps execution as the oracle: LLMs propose harnesses, inputs, states, and constraints; fuzzers validate.
- The most useful 2026 preprints are those with reproducible targets, coverage/crash evidence, and false-positive controls.
