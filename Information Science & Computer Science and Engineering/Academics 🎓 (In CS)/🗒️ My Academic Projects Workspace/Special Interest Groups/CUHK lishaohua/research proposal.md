# research proposal

[TOC]



## Res
### Related Topics


### Other Resources



## Phe Proposal
### Recommended PhD proposal #1 (gpt-sol)

#### Working title

**ContractWorld: Continually Learned Semantic Contracts for Trustworthy Compiler Agents**

#### One-sentence thesis

Build a continuously updated “world model” of compiler transformations—combining explicit semantic obligations, historical developer knowledge, and generated counterexamples—so that agents can review, repair, and optimize compilers while producing machine-checkable evidence about both correctness and generalization scope.

#### Why this proposal fits the group

This proposal is the smallest natural unification of the group’s newest work:

- `llvm-autofix` provides the agent harness and bug benchmark.
- The missed-optimization paper exposes scope generalization as the missing repair criterion.
- Archer introduces obligation-guided review and deterministic validation.
- Creal and LegoFuzz provide expressive test-generation substrates.
- CompDiff and UBfuzz provide relational oracles and adversarial semantic cases.
- Dynamic benchmarking provides continual mutation against contamination/staleness.
- The GPU-kernel paper shows that local equality checks can miss downstream behavioral risk.
- QuTuner shows how transformation-response representations can guide optimization.

It also connects naturally to the applicant’s demonstrated interest in structured world models and knowledge organization: the “world model” here is not a vague neural metaphor, but an inspectable, versioned representation of which transformations are valid over which program regions and under which assumptions.

#### Core research questions

1. **How should the intended scope of a compiler transformation be represented?**  
   Candidate representation: a contract containing preconditions, affected IR patterns, semantic equivalence obligations, profitability conditions, poison/UB assumptions, target constraints, and known counterexamples.

2. **Can contracts be induced from heterogeneous evidence?**  
   Sources include the issue reproducer, developer patch, review discussion, optimization remarks, tests, historical similar PRs, Alive2-compatible rules, and agent-generated examples.

3. **How can an agent actively refine an uncertain contract?**  
   The agent should choose queries—generate a program, mutate IR, invoke a solver, inspect a pass trace, retrieve a historical patch—that maximally separate competing scope hypotheses.

4. **How should correctness confidence compose across transformations?**  
   Local proofs or tolerance checks may fail under pass interaction, floating-point accumulation, target lowering, or downstream model behavior. The system should track proof/evidence boundaries and escalate weak compositions to differential or end-to-end testing.

5. **Can the learned contract memory remain useful as LLVM evolves?**  
   Contracts need versioning, invalidation, regression generation, and continual refresh when passes, IR semantics, or targets change.

#### Proposed system

```text
Issue / PR / optimization opportunity
            |
            v
   Evidence extraction
   - reproducer and tests
   - IR/pass traces
   - discussion and patch
   - similar historical PRs
            |
            v
   Contract hypothesis memory
   - preconditions
   - semantic obligation
   - intended scope
   - profitability
   - uncertainty
            |
            v
   Active evidence generation
   - real-code synthesis (Creal/LegoFuzz style)
   - semantics-preserving mutation
   - solver/Alive2 queries
   - differential execution
            |
            v
   Agent review or patch
            |
            v
   Evidence bundle
   - proof where supported
   - minimized counterexamples
   - regression tests
   - scope/uncertainty report
```

#### Research plan

##### Phase 1 — Scope-aware benchmark

- Start with LLVM missed optimizations and semantic-bug PRs already used by the group.
- For each issue, construct a versioned evidence record: reproducer, developer patch, tests, discussion, affected passes, and nearby historical changes.
- Develop a taxonomy of transformation scope errors: under-generalization, unintended overlap, unsafe over-generalization, target-specific failure, and pass-interaction failure.
- Add held-out generated families rather than judging only on the original reproducer.

**Deliverable:** an open benchmark where success requires a correct patch **and** an empirically/provably characterized scope.

##### Phase 2 — Contract induction and active counterexample search

- Parse patches and review text into candidate structured contracts.
- Retrieve similar historical transformations, but represent disagreement rather than blindly merging retrieved knowledge.
- Generate discriminating IR/program families using grammar rules, real-code components, and semantics-preserving mutations.
- Use Alive2 or another translation-validation layer where supported; fall back to differential execution and metamorphic relations outside solver coverage.
- Let the agent select the next evidence-producing action based on contract uncertainty.

**Deliverable:** a contract learner that finds hidden under-/over-generalization cases more efficiently than unguided fuzzing or fixed test suites.

##### Phase 3 — Evidence-gated review and repair agent

- Integrate the contracts into Archer/`llvm-autofix`-style workflows.
- Require every claim to reference a reproducible test, proof result, code location, or explicitly labeled heuristic.
- Generate regression tests and a scope report alongside each patch.
- Study whether a smaller model with a better semantic harness beats a larger general model, following the group’s harness-first hypothesis.

**Deliverable:** a deployable LLVM bot that can review or propose patches with evidence bundles suitable for human maintainers.

##### Phase 4 — Composition and broader stacks

- Test pass interactions and downstream composition, inspired by the GPU-kernel correctness study.
- Extend from LLVM IR to one complementary domain: rustc MIR, MLIR/GPU kernels, or quantum compiler passes.
- Compare which contract components transfer and which are domain-specific.

**Deliverable:** evidence about whether semantic contract memory is a compiler-general abstraction rather than LLVM-only engineering.

#### Evaluation

The proposal should avoid a single “patch resolved” score. Recommended metrics:

- **Patch correctness:** builds, original tests, hidden tests, translation validation, differential runs.
- **Scope alignment:** precision/recall over generated valid transformation families; under- and over-generalization rates.
- **Bug discovery:** new counterexamples, confirmed compiler defects, and accepted regression tests.
- **Evidence quality:** reproducibility, minimization, proof coverage, false-alarm rate, and reviewer agreement.
- **Efficiency:** agent cost, compiler executions, solver time, and evidence gained per action.
- **Longitudinal robustness:** survival of contracts across compiler revisions and unseen passes/targets.
- **Real-world impact:** LLVM review feedback, merged patches/tests, or tool adoption.

Baselines should include a general coding agent, the same model with the compiler harness only, retrieval-augmented agents, fixed fuzzing/test generation, and the full contract-guided system. Ablations should separately remove historical memory, active query selection, proof tools, real-code generation, and contract versioning.

#### Main risks and how to bound them

- **Contracts may be too expensive to author or infer.** Start with optimization patterns supported by LLVM IR and translation validation; treat natural-language obligations as uncertain hypotheses, not truth.
- **Developer patches are not complete specifications.** Evaluate against generated semantic families and independent oracles, and permit the system to flag the reference patch itself.
- **Solver coverage is limited.** Use a tiered evidence model: proof, bounded exhaustive checking, differential testing, and heuristic evidence must remain visibly distinct.
- **Agent results may be contaminated by public LLVM history.** Use post-cutoff issues, dynamic program transformations, and temporally split evaluation.
- **A large infrastructure project may delay publications.** Stage the work so the scope-aware benchmark, active contract testing, agent integration, and cross-domain composition are independently publishable.

#### Expected contributions

1. A formal/practical representation of compiler-transformation scope and uncertainty.
2. A benchmark that evaluates semantic generalization rather than single-reproducer success.
3. An active evidence-generation method combining real code, mutation, retrieval, and solver feedback.
4. An evidence-gated agent for compiler review and repair.
5. A longitudinal study of semantic memory under compiler evolution.

#### Two narrower fallback proposals

##### Fallback A — Composition-aware correctness for AI-generated GPU kernels

Develop operator-role-aware contracts that combine local numerical error, precision policy, downstream sensitivity, repeated-layer accumulation, and speedup. Build adversarial kernel tests and an evidence-gated optimization agent. This is timely and directly extends paper 24, but it is narrower and more dependent on rapidly changing GPU-agent ecosystems.

##### Fallback B — Continually refreshed dynamic benchmarks for code and compiler agents

Generalize paper 10 from semantics-preserving code mutations to interactive, versioned compiler tasks. Each evaluation instance would be generated after the model cutoff, include a reproducible tool environment, and score the evidence trajectory as well as the final patch. This is lower risk and likely faster to execute, but may be perceived as benchmark work unless paired with a strong method for active task generation.

### Application positioning

A concise application narrative could be:

> I am interested in trustworthy intelligent systems at the boundary between AI and programming languages. Your group’s work shows a consistent methodology that I strongly identify with: use program semantics and real executions to make automation both practical and accountable. I would like to study compiler agents whose internal knowledge is not only retrieved text, but a continually updated model of transformation scope, assumptions, and counterexamples. My proposed direction builds directly on Archer, `llvm-autofix`, the missed-optimization study, LegoFuzz/Creal, and compiler-driven differential testing. The intended outcome is an open LLVM tool that produces patches or reviews together with reproducible semantic evidence.

Before emailing, the proposal should be customized with concrete evidence of the applicant’s compiler/systems experience. A strong pre-application artifact would be one of:

- reproduce one missed-optimization case and extend it with a generated family revealing scope;
- add a small LLVM tool that extracts optimization/pass evidence for an agent;
- evaluate an existing compiler agent on newly reported post-cutoff LLVM issues;
- build a semantics-preserving mutation module and show that it changes agent rankings;
- contribute a confirmed bug, regression test, or documentation improvement to one of the group’s open-source tools.

The email should follow the required subject format from Li’s openings page, attach CV and transcripts, and link the artifact. The proposal should be framed as a starting hypothesis open to refinement, not as a fixed four-year commitment.

### Bottom line

The best-fitting proposal is not “use an LLM to fix compiler bugs.” The group is already beyond that. The more defensible frontier is:

> **How can a compiler agent know—and demonstrate—the semantic region over which its review, repair, or optimization is valid?**

That question joins nearly every mature strand in the group: differential oracles, expressive test generation, cheap execution proxies, compiler-specific harnesses, agentic review, patch generalization, dynamic benchmarks, and composition-aware correctness. It is technically deep enough for a PhD, divisible into publishable stages, and aligned with the group’s preference for real-world, open-source impact.



## Ref
