# Church–Turing Thesis (Computability Thesis)

[TOC]



## Res
### Related Topics
↗ [Algorithm & Data Structure](../../../../🔑%20CS%20Core/🧙‍♂️%20Algorithm%20&%20Data%20Structure/Algorithm%20&%20Data%20Structure.md)



## Intro
> 🔗 https://en.wikipedia.org/wiki/Church–Turing_thesis

In [computability theory](https://en.wikipedia.org/wiki/Computability_theory_(computation) "Computability theory (computation)"), the **Church–Turing thesis** (also known as **computability thesis**, the **Turing–Church thesis**, the **Church–Turing conjecture**, **Church's thesis**, **Church's conjecture**, and **Turing's thesis**) is a [thesis](https://en.wiktionary.org/wiki/thesis "wiktionary:thesis") about the nature of [computable functions](https://en.wikipedia.org/wiki/Computable_function "Computable function"). It states that a [function](https://en.wikipedia.org/wiki/Function_(mathematics) "Function (mathematics)") on the [natural numbers](https://en.wikipedia.org/wiki/Natural_numbers "Natural numbers") can be calculated by an [effective method](https://en.wikipedia.org/wiki/Effective_method "Effective method") if and only if it is computable by a [Turing machine](https://en.wikipedia.org/wiki/Turing_machine "Turing machine"). The thesis is named after American mathematician [Alonzo Church](https://en.wikipedia.org/wiki/Alonzo_Church "Alonzo Church") and the British mathematician [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing "Alan Turing"). Before the precise definition of computable function, mathematicians often used the informal term [effectively calculable](https://en.wikipedia.org/wiki/Effectively_calculable "Effectively calculable") to describe functions that are computable by paper-and-pencil methods. In the 1930s, several independent attempts were made to [formalize](https://en.wikipedia.org/wiki/Formal_system "Formal system") the notion of [computability](https://en.wikipedia.org/wiki/Computability "Computability"):

- In 1933, [Kurt Gödel](https://en.wikipedia.org/wiki/Kurt_G%C3%B6del "Kurt Gödel"), with [Jacques Herbrand](https://en.wikipedia.org/wiki/Jacques_Herbrand "Jacques Herbrand"), formalized the definition of the class of [general recursive functions](https://en.wikipedia.org/wiki/General_recursive_function "General recursive function"): the smallest class of functions (with arbitrarily many arguments) that is closed under [composition](https://en.wikipedia.org/wiki/Function_composition "Function composition"), [recursion](https://en.wikipedia.org/wiki/Recursion "Recursion"), and [minimization](https://en.wikipedia.org/wiki/%CE%9C_operator "Μ operator"), and includes [zero](https://en.wikipedia.org/wiki/Zero_function "Zero function"), [successor](https://en.wikipedia.org/wiki/Successor_function "Successor function"), and all [projections](https://en.wikipedia.org/wiki/Projection_function "Projection function").
- In 1936, [Alonzo Church](https://en.wikipedia.org/wiki/Alonzo_Church "Alonzo Church") created a method for defining functions called the [λ-calculus](https://en.wikipedia.org/wiki/Lambda_calculus "Lambda calculus"). Within λ-calculus, he defined an encoding of the natural numbers called the [Church numerals](https://en.wikipedia.org/wiki/Church_numerals "Church numerals"). A function on the natural numbers is called [λ-computable](https://en.wikipedia.org/wiki/Lambda-recursive_function "Lambda-recursive function") if the corresponding function on the Church numerals can be represented by a term of the λ-calculus.
- Also in 1936, before learning of Church's work, [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing "Alan Turing") created a theoretical model for machines, now called Turing machines, that could carry out calculations from inputs by manipulating symbols on a tape. Given a suitable encoding of the natural numbers as sequences of symbols, a function on the natural numbers is called [Turing computable](https://en.wikipedia.org/wiki/Computable_function "Computable function") if some Turing machine computes the corresponding function on encoded natural numbers.

Church, [Kleene](https://en.wikipedia.org/wiki/Stephen_Cole_Kleene "Stephen Cole Kleene"), and Turing proved that these three formally defined classes of computable functions coincide: a function is λ-computable if and only if it is Turing computable, and if and only if it is _general recursive_. This has led mathematicians and computer scientists to believe that the concept of computability is accurately characterized by these three equivalent processes. Other formal attempts to characterize computability have subsequently strengthened this belief.

On the other hand, the Church–Turing thesis states that the above three formally-defined classes of computable functions coincide with the _informal_ notion of an effectively calculable function. Although the thesis has near-universal acceptance, it cannot be formally proven, as the concept of effective calculability is only informally defined.

Since its inception, variations on the original thesis have arisen, including statements about what can physically be realized by a computer in our universe ([physical Church-Turing thesis](https://en.wikipedia.org/wiki/Physical_Church-Turing_thesis "Physical Church-Turing thesis")) and what can be efficiently computed ([Church–Turing thesis (complexity theory)](https://en.wikipedia.org/wiki/Church%E2%80%93Turing_thesis#complexity-theoretic_Church%E2%80%93Turing_thesis)). These variations are not due to Church or Turing, but arise from later work in [complexity theory](https://en.wikipedia.org/wiki/Computational_complexity_theory "Computational complexity theory") and [digital physics](https://en.wikipedia.org/wiki/Digital_physics "Digital physics"). The thesis also has implications for the [philosophy of mind](https://en.wikipedia.org/wiki/Philosophy_of_mind "Philosophy of mind")



## Ref
