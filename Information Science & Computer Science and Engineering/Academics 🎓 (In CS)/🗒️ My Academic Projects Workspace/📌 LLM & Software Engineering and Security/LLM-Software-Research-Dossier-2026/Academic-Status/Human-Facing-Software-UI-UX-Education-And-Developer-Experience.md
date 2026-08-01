---
ai-generated: true
last-reviewed: 2026-07-30
---

# Human-Facing Software, UI/UX, Education, and Developer Experience

Back: [Academic Status](Academic-Status.md)

Scope: multimodal and visual software engineering, UI-to-code, usability analysis, video-grounded bug work, software-engineering education, and empirical evidence about how people frame, learn, review, and collaborate with LLM-assisted software systems. The cross-dossier synthesis remains in the [shared Human Factor](../../LLM-Software-Security-Research-Dossier-2026/Human-Factor.md).

## Status

Human-facing software is not reducible to token-level code generation. A model must connect screenshots, layout, interaction state, video, accessibility, task intent, and user expectations to executable behavior. At the same time, developer studies show that useful assistance depends on clarification, team norms, expertise, review, and learning—not only model accuracy.

## UI, UX, and Multimodal Software

| Key | Paper | Year | Venue / evidence | Contribution | Label |
| --- | --- | ---: | --- | --- | --- |
| Wu2025UI2Code | [MLLM-Based UI2Code Automation Guided by UI Layout Information](https://conf.researchr.org/track/issta-2025/issta-2025-papers) | 2025 | ISSTA Research Papers / official program | Uses inferred layout structure to guide code generation from webpage images. | Official program |
| He2026ReFLAIR | [ReFLAIR: Detecting Responsive Layout Reflow Issues using Multimodal Generative AI](https://conf.researchr.org/track/fse-2026/fse-2026-research-papers) | 2026 | FSE Research Papers / official program | Detects responsive-layout and reflow failures with multimodal evidence. | Official program |
| Lubos2026Usability | [Recommending Usability Improvements with Multimodal Large Language Models](https://conf.researchr.org/track/fse-2026/fse-2026-research-papers) | 2026 | FSE Research Papers / official program | Studies multimodal recommendations for concrete usability improvements. | Official program |
| Feng2026ViBR | [ViBR: Automated Bug Replay from Video-based Reports Using Vision-Language Models](https://conf.researchr.org/track/fse-2026/fse-2026-research-papers) | 2026 | FSE Research Papers / official program | Converts video bug reports into replayable interaction evidence. | Official program |
| Peng2026PlayCoder | [PlayCoder: Making LLM-Generated GUI Code Playable](https://conf.researchr.org/track/fse-2026/fse-2026-research-papers) | 2026 | FSE Research Papers / official program | Targets executable, interactive behavior rather than screenshot similarity alone. | Official program |
| Aggarwal2026ProgrammingPixels | [Programming with Pixels: Can Computer-Use Agents do Software Engineering?](https://iclr.cc/virtual/2026/poster/10011120) | 2026 | ICLR Poster / official record | Evaluates agents that visually operate an IDE and compares visual interaction with direct software-tool APIs. | Published / Evaluation |

## Education, Collaboration, and Developer Experience

| Key | Paper | Year | Venue / evidence | Human question | Label |
| --- | --- | ---: | --- | --- | --- |
| Vijayvargiya2026Underspecificity | [Interactive Agents to Overcome Underspecificity in Software Engineering](https://iclr.cc/virtual/2026/poster/10009007) | 2026 | ICLR Poster / official record | Can an agent detect missing information, ask a targeted question, and use the answer? | Published / Evaluation |
| Kumar2025DeveloperAgentCollaboration | [Why AI Agents Still Need You: Findings from Developer-Agent Collaborations in the Wild](https://conf.researchr.org/track/ase-2025/ase-2025-papers) | 2025 | ASE Research Papers / official program | Where and why do deployed coding agents still require developer intervention? | Official program / Evaluation |
| Welter2025PairProgrammingTransfer | [An Empirical Study of Knowledge Transfer in AI Pair Programming](https://conf.researchr.org/track/ase-2025/ase-2025-papers) | 2025 | ASE Research Papers / official program | Does working with an AI partner transfer knowledge to the developer? | Official program / Evaluation |
| Miller2026TeamDrivers | [“Maybe We Need Some More Examples:” Individual and Team Drivers of Developer GenAI Tool Use](https://conf.researchr.org/track/icse-2026/icse-2026-research-track) | 2026 | ICSE Research Track / official program; Distinguished Paper | How do individual and team conditions shape adoption and use? | Official program / Evaluation |
| Sergeyuk2026DeveloperLogs | [Evolving with AI: A Longitudinal Analysis of Developer Logs](https://conf.researchr.org/track/icse-2026/icse-2026-research-track) | 2026 | ICSE Research Track / official program | How does developer behavior change over time rather than in a one-session study? | Official program / Evaluation |
| Yang2026TestingEducation | [Large Language Models for Software Testing Education: an Experience Report](https://conf.researchr.org/track/fse-2026/fse-2026-research-papers) | 2026 | FSE Software Engineering Education / official program | What changes when LLM assistance is integrated into software-testing instruction? | Official program / Experience |
| Wang2026GenAICourse | [From Specifications to Implementation in the Gen-AI Era: Lessons from a Project-based Software Engineering Course](https://conf.researchr.org/track/fse-2026/fse-2026-research-papers) | 2026 | FSE Research Papers / official program | How should project-based courses preserve specification, design, and implementation learning? | Official program / Education |

## Evaluation Checklist

- evaluate interaction state and behavior, not only screenshot or text similarity;
- preserve viewport, platform, accessibility, and device context for UI claims;
- record whether agents receive visual-only access or direct file, shell, and IDE APIs;
- measure clarification quality and downstream benefit, including unnecessary questions;
- report participant experience, team setting, prior tool use, and task authenticity;
- measure learning retention, review cost, maintainability, and future task performance;
- separate a completed deliverable from demonstrated understanding.

## Boundary Notes

This page owns human-facing software and use of LLMs in software-engineering work or education. It does not own attacks on visual agents, privacy leakage, deceptive interfaces, or other security-first claims; those remain in the [security dossier](../../LLM-Software-Security-Research-Dossier-2026/LLM-Software-Security-Research-Dossier-2026.md).

## Research Gaps

- executable and accessibility-aware UI oracles beyond pixel similarity;
- multimodal requirements that preserve interaction state across long workflows;
- longitudinal evidence on skill formation, deskilling, and knowledge transfer;
- team-level studies that include review, ownership, and coordination costs;
- inclusive evaluation across disability, language, geography, and experience;
- principled autonomy settings that adapt to task ambiguity and developer expertise.

<!-- BEGIN GENERATED CANONICAL CORPUS ROWS -->
## Generated Canonical Corpus Rows

The builder maintains this block from the shared screening and mapping ledgers. Hand-written rows and analysis above remain authoritative where present.

### Formal Venue Papers

| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |
| --- | --- | ---: | --- | --- | --- | --- |
| 00022024SelfpicoSelfGuided | [SelfPiCo: Self-Guided Partial Code Execution with LLMs.](<https://doi.org/10.1145/3650212.3680368>) | 2024 | ISSTA / proceedings | Human Facing Software UI UX Education And Developer Experience | Introduces or evaluates selfPiCo: Self-Guided Partial Code Execution with LLMs; abstract-level contribution review remains pending. | formal-venue |
| 03532024RocksCodingNot | [Rocks Coding, Not Development: A Human-Centric, Experimental Evaluation of LLM-Supported SE Tasks.](<https://doi.org/10.1145/3643758>) | 2024 | FSE/PACMSE / proceedings | Human Facing Software UI UX Education And Developer Experience | Benchmarks or evaluates rocks Coding, Not Development: A Human-Centric, Experimental Evaluation of LLM-Supported SE Tasks; abstract-level contribution review remains pending. | formal-venue |
| Barke2024HysynthContextFree | [HYSYNTH: Context-Free LLM Approximation for Guiding Program Synthesis.](<http://papers.nips.cc/paper_files/paper/2024/hash/1c9c85bae6161d52182d0fe2f3640512-Abstract-Conference.html>) | 2024 | NeurIPS / proceedings | Human Facing Software UI UX Education And Developer Experience | Introduces or evaluates hYSYNTH: Context-Free LLM Approximation for Guiding Program Synthesis; abstract-level contribution review remains pending. | formal-venue |
| Eom2024FuzzingJavascriptInterpreters | [Fuzzing JavaScript Interpreters with Coverage-Guided Reinforcement Learning for LLM-Based Mutation.](<https://doi.org/10.1145/3650212.3680389>) | 2024 | ISSTA / proceedings | Human Facing Software UI UX Education And Developer Experience | Introduces or evaluates fuzzing JavaScript Interpreters with Coverage-Guided Reinforcement Learning for LLM-Based Mutation; abstract-level contribution review remains pending. | formal-venue |
| Fan2024OracleGuidedProgram | [Oracle-Guided Program Selection from Large Language Models.](<https://doi.org/10.1145/3650212.3680308>) | 2024 | ISSTA / proceedings | Human Facing Software UI UX Education And Developer Experience | Introduces or evaluates oracle-Guided Program Selection from Large Language Models; abstract-level contribution review remains pending. | formal-venue |
| Imran2024UncoveringCausesEmotions | [Uncovering the Causes of Emotions in Software Developer Communication Using Zero-shot LLMs.](<https://doi.org/10.1145/3597503.3639223>) | 2024 | ICSE / proceedings | Human Facing Software UI UX Education And Developer Experience | Introduces or evaluates uncovering the Causes of Emotions in Software Developer Communication Using Zero-shot LLMs; abstract-level contribution review remains pending. | formal-venue |
| Oh2024PoisonedChatgptFinds | [Poisoned ChatGPT Finds Work for Idle Hands: Exploring Developers' Coding Practices with Insecure Suggestions from Poisoned AI Models.](<https://doi.org/10.1109/SP54263.2024.00046>) | 2024 | IEEE S&P / proceedings | Human Facing Software UI UX Education And Developer Experience | Introduces or evaluates poisoned ChatGPT Finds Work for Idle Hands: Exploring Developers' Coding Practices with Insecure Suggestions from Poisoned AI Models; abstract-level contribution review remains pending. | formal-venue |
| Liu2025ExplainableFaultLocalization | [Explainable Fault Localization for Programming Assignments via LLM-Guided Annotation](<https://conf.researchr.org/track/ase-2025/ase-2025-papers#event-e7f8f843-e549-4634-8174-d2c50fae8545>) | 2025 | ASE / accepted-program | Human Facing Software UI UX Education And Developer Experience | Introduces or evaluates explainable Fault Localization for Programming Assignments via LLM-Guided Annotation; abstract-level contribution review remains pending. | formal-venue |
| Wang2025CanLlmsReplace | [Can LLMs Replace Human Evaluators? An Empirical Study of LLM-as-a-Judge in Software Engineering.](<https://doi.org/10.1145/3728963>) | 2025 | ISSTA / proceedings | Human Facing Software UI UX Education And Developer Experience | Benchmarks or evaluates can LLMs Replace Human Evaluators? An Empirical Study of LLM-as-a-Judge in Software Engineering; abstract-level contribution review remains pending. | formal-venue |
| Abdelsalam2026AreHumansLlms | [Are Humans and LLMs Confused by the Same Code? An Empirical Study on Fixation-Related Potentials and LLM Perplexity](<https://conf.researchr.org/track/icse-2026/icse-2026-research-track#event-13dd9926-7650-46b4-bfe0-64d557387fe8>) | 2026 | ICSE / accepted-program | Human Facing Software UI UX Education And Developer Experience | Benchmarks or evaluates are Humans and LLMs Confused by the Same Code? An Empirical Study on Fixation-Related Potentials and LLM Perplexity; abstract-level contribution review remains pending. | formal-venue |
| Deng2026SasftSparseAutoencoder | [SASFT: Sparse Autoencoder-guided Supervised Finetuning to Mitigate Unexpected Code-Switching in LLMs](<https://openreview.net/forum?id=BQOFU9qO5j>) | 2026 | ICLR / accepted-program | Human Facing Software UI UX Education And Developer Experience | Introduces or evaluates sASFT: Sparse Autoencoder-guided Supervised Finetuning to Mitigate Unexpected Code-Switching in LLMs; abstract-level contribution review remains pending. | formal-venue |
| Pan2026HiddenCostReadability | [The Hidden Cost of Readability: How Code Formatting Silently Consumes Your LLM Budget Distinguished Paper Award](<https://conf.researchr.org/track/icse-2026/icse-2026-research-track#event-4b32730c-92e2-4748-8117-e3758057f7ad>) | 2026 | ICSE / accepted-program | Human Facing Software UI UX Education And Developer Experience | Introduces or evaluates the Hidden Cost of Readability: How Code Formatting Silently Consumes Your LLM Budget Distinguished Paper Award; abstract-level contribution review remains pending. | formal-venue |
| Rong2026DoLargeLanguage | [Do Large Language Models Understand Code like Humans?](<https://conf.researchr.org/track/issta-2026/issta-2026-research-papers#event-679075fd-bd28-45b8-a005-5b5bf03fc44e>) | 2026 | ISSTA / accepted-program | Human Facing Software UI UX Education And Developer Experience | Introduces or evaluates do Large Language Models Understand Code like Humans?; abstract-level contribution review remains pending. | formal-venue |
| Yin2026NeuronGuidedInterpretation | [Neuron-Guided Interpretation of Code LLMs: Where, Why, and How?](<https://conf.researchr.org/track/fse-2026/fse-2026-research-papers#event-36a24289-61ee-4ecb-918c-062cdce43b8f>) | 2026 | FSE/PACMSE / accepted-program | Human Facing Software UI UX Education And Developer Experience | Introduces or evaluates neuron-Guided Interpretation of Code LLMs: Where, Why, and How?; abstract-level contribution review remains pending. | formal-venue |
| Yuan2026RedTeamingLlms | [Red Teaming LLMs via Linguistic-Aware Fuzzing](<https://conf.researchr.org/track/fse-2026/fse-2026-research-papers#event-43dbf1d3-f25b-4415-a82e-33f82f1ffa01>) | 2026 | FSE/PACMSE / accepted-program | Human Facing Software UI UX Education And Developer Experience | Introduces or evaluates red Teaming LLMs via Linguistic-Aware Fuzzing; abstract-level contribution review remains pending. | formal-venue |
| Zhang2026ScancoderLeveragingHuman | [ScanCoder: Leveraging Human Attention Patterns to Enhance LLMs for Code](<https://conf.researchr.org/track/fse-2026/fse-2026-research-papers#event-f0c88584-6789-4394-9996-a87b4b42058d>) | 2026 | FSE/PACMSE / accepted-program | Human Facing Software UI UX Education And Developer Experience | Introduces or evaluates scanCoder: Leveraging Human Attention Patterns to Enhance LLMs for Code; abstract-level contribution review remains pending. | formal-venue |
| normalization2026AutorpaEfficientGui | [AutoRPA: Efficient GUI Automation through LLM-Driven Code Synthesis from Interactions](<https://icml.cc/virtual/2026/poster/64026>) | 2026 | ICML / accepted-program | Human Facing Software UI UX Education And Developer Experience | Introduces or evaluates autoRPA: Efficient GUI Automation through LLM-Driven Code Synthesis from Interactions; abstract-level contribution review remains pending. | formal-venue |
| yang2026HowDoSemantically | [How Do Semantically Equivalent Code Transformations Impact Membership Inference on LLMs for Code?](<https://conf.researchr.org/track/icse-2026/icse-2026-research-track#event-f0c53d33-4203-4b00-954e-f5cfa939503c>) | 2026 | ICSE / accepted-program | Human Facing Software UI UX Education And Developer Experience | Introduces or evaluates how Do Semantically Equivalent Code Transformations Impact Membership Inference on LLMs for Code?; abstract-level contribution review remains pending. | formal-venue |

### Frontier Preprints

| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |
| --- | --- | ---: | --- | --- | --- | --- |
| Jha2026HalfExpertsAll | [Half the Experts, All the Code: One-Shot Domain Pruning of Mixture-of-Experts LLMs for Coding](<https://arxiv.org/abs/2607.16721>) | 2026 | arXiv / frontier-preprint | Human Facing Software UI UX Education And Developer Experience | The strongest open-weight coding models are mixture-of-experts (MoE) networks: most of their size comes from large pools of "expert" subnetworks, of which only a…. | frontier-preprint |
| Jost2026ImpactAiAssisted | [The Impact of AI-Assisted Development on Software Security: A Study of Gemini and Developer Experience](<https://arxiv.org/abs/2603.15298>) | 2026 | arXiv / frontier-preprint | Human Facing Software UI UX Education And Developer Experience | The ongoing shortage of skilled developers, particularly in security-critical software development, has led organizations to increasingly adopt AI-powered development tools to boost productivity and…. | frontier-preprint |
| Wang2026ContextSourceChannel | [In-Context Source and Channel Coding](<https://arxiv.org/abs/2601.10267>) | 2026 | arXiv / frontier-preprint | Human Facing Software UI UX Education And Developer Experience | This paper proposes a receiver-side In-Context Decoding (ICD) framework that enhances SSCC robustness without modifying the transmitter. | frontier-preprint |

<!-- END GENERATED CANONICAL CORPUS ROWS -->
