# Markov Chains (MC) & Markov Process

[TOC]



## Res
### Related Topics
↗ [Theory of Computation](../../../../🤼‍♀️%20Mathematical%20Logic%20(Foundations%20of%20Mathematics)/😶‍🌫️%20Theory%20of%20Computation/Theory%20of%20Computation.md)
↗ [(Formal) Model Checking](../../../../../CyberSecurity/🏰%20Cybersecurity%20Basics%20&%20InfoSec/🍦%20Software%20Security/🪆%20Software%20(Program)%20Analysis%20&%20Binary%20Engineering/📌%20Software%20(Program)%20Analysis%20Basics/🙇‍♂️%20Formal%20Methods%20&%20Formal%20Verification%20(FV)/(Formal)%20Model%20Checking/(Formal)%20Model%20Checking.md)

↗ [PRISM](../../../../../CyberSecurity/☠️%20Kill%20Chain%20&%20Security%20Tool%20Box/🔞%20Software%20Analysis%20Tools/⛰️%20Static%20Code%20Analysis%20Tools%20(SCAT)/🤼%20Model%20Checker/PRISM.md)


### Other Resources
🎬 https://youtube.com/playlist?list=PLM8wYQRetTxBkdvBtz-gw8b9lcVkdXQKV&si=pzMOKOIPUO6bQ4J2 
👍 Markov Chains Clearly Explained! | by Normalized Nerd, Youtube

📂 https://www.prismmodelchecker.org/tutorial/
This tutorial will introduce you to the PRISM tool using a selection of example models.
The tutorial comprises several parts. If you are new to the tool, we recommend that you start by working through the first part (Knuth's die algorithm) to see the basics. After that, you should be able to look at the remaining parts in any order, depending in which models or applications you are interested in. If anything is unclear, the best place to look for answers is the [PRISM manual](https://www.prismmodelchecker.org/manual/).
- **[Knuth's die algorithm](https://www.prismmodelchecker.org/tutorial/die.php)**: This uses a simple **discrete-time Markov chain (DTMC)** example - a randomised algorithm for modelling a 6-sided die with a fair coin due to Don Knuth. It introduces the basics of the PRISM modelling language and the PRISM tool.  
- **[Herman's self-stabilisation algorithm](https://www.prismmodelchecker.org/tutorial/herman.php)**: This uses another simple randomised algorithm: a self-stabilisation algorithm due to Herman. This is also modelled as a **DTMC** and introduces some additional features of the **PRISM modelling** and property languages.  
- **[Robot navigation](https://www.prismmodelchecker.org/tutorial/robot.php)**: This introduces the use of **Markov decision processes (MDPs)** for generating control policies based on temporal logic specifications, via a simple example of a robot navigating through an uncertain environment.  
- **[Autonomous drone](https://www.prismmodelchecker.org/tutorial/drone.php)**: This shows how to use **interval Markov decision processes (IMDPs)** to incorporate **epistemic uncertainty** into probabilistic model checking of MDPs, specifically regarding the precise value of transition probabilities. It uses an example of an autonomous drone.  
- **[Dynamic power management](https://www.prismmodelchecker.org/tutorial/power.php)**: This introduces a **multi-component system** modelled as a **continuous-time Markov chain (CTMC)**: a controller for a dynamic power management system.  
- **[Circadian clock](https://www.prismmodelchecker.org/tutorial/circadian.php)**: This demonstrates the use of PRISM to study a **biological system**, modelled as a **CTMC**: a circadian clock.  
- **[EGL contract signing protocol](https://www.prismmodelchecker.org/tutorial/egl.php)**: This uses a case study from the field of **computer security**, modelled as a **DTMC**: the EGL contract signing protocol.  
- **[Dining philosophers problem](https://www.prismmodelchecker.org/tutorial/phil.php)**: This introduces the use of a **MDP** to verify a simple **distributed randomised algorithm**: the dining philosophers problem.



## Intro
![](../../../../../../Assets/Pics/Screenshot%202025-09-06%20at%2000.17.29.png)
<small><a>https://youtu.be/i3AkTO9HLXo?si=xHI2YFg1ZGp85ALo</a></small>

> 🔗 https://en.wikipedia.org/wiki/Markov_chain

==In probability theory and statistics, a **Markov chain** or **Markov process** is a [stochastic process](https://en.wikipedia.org/wiki/Stochastic_process "Stochastic process") describing a [sequence](https://en.wikipedia.org/wiki/Sequence "Sequence") of possible events in which the [probability](https://en.wikipedia.org/wiki/Probability "Probability") of each event depends only on the state attained in the previous event. Informally, this may be thought of as, "What happens next depends only on the state of affairs _now_."== 

A [countably infinite](https://en.wikipedia.org/wiki/Countably_infinite "Countably infinite") sequence, in which the chain moves state at discrete time steps, gives a [discrete-time Markov chain](https://en.wikipedia.org/wiki/Discrete-time_Markov_chain "Discrete-time Markov chain") (DTMC). A [continuous-time](https://en.wikipedia.org/wiki/Continuous-time "Continuous-time") process is called a [continuous-time Markov chain](https://en.wikipedia.org/wiki/Continuous-time_Markov_chain "Continuous-time Markov chain") (CTMC). Markov processes are named in honor of the [Russian](https://en.wikipedia.org/wiki/Russia "Russia") mathematician [Andrey Markov](https://en.wikipedia.org/wiki/Andrey_Markov "Andrey Markov").

Markov chains have many applications as [statistical models](https://en.wikipedia.org/wiki/Statistical_model "Statistical model") of real-world processes. They provide the basis for general stochastic simulation methods known as [Markov chain Monte Carlo](https://en.wikipedia.org/wiki/Markov_chain_Monte_Carlo "Markov chain Monte Carlo"), which are used for simulating sampling from complex [probability distributions](https://en.wikipedia.org/wiki/Probability_distribution "Probability distribution"), and have found application in areas including [Bayesian statistics](https://en.wikipedia.org/wiki/Bayesian_statistics "Bayesian statistics"), [biology](https://en.wikipedia.org/wiki/Biology "Biology"), [chemistry](https://en.wikipedia.org/wiki/Chemistry "Chemistry"), [economics](https://en.wikipedia.org/wiki/Economics "Economics"), [finance](https://en.wikipedia.org/wiki/Finance "Finance"), [information theory](https://en.wikipedia.org/wiki/Information_theory "Information theory"), [physics](https://en.wikipedia.org/wiki/Physics "Physics"), [signal processing](https://en.wikipedia.org/wiki/Signal_processing "Signal processing"), and [speech processing](https://en.wikipedia.org/wiki/Speech_processing "Speech processing").

**The adjectives _Markovian_ and _Markov_ are used to describe something that is related to a Markov process.**



## Ref
[The Strange Math That Predicts (Almost) Anything | Veritasium]: https://youtu.be/KZeIEiBrT_w?si=pkrdzcBgEBEO7LcE
