# Relational Data Languages

[TOC]



## Res
↗ [Database System Languages](../📌%20Database%20System%20Basics/Database%20System%20Languages.md)



## Overview


## 🏟️ Relation in Math
> ❗❗ Foundation of Relational DML

Both Relational Algebra and Relational Calculus are **formal query languages**. 

### Relational Algebra（关系代数）
Relational Algebra is a **procedural language**. In Relational Algebra, The order is specified in which the operations have to be performed. In [Relational Algebra](https://www.geeksforgeeks.org/introduction-of-relational-algebra-in-dbms/), frameworks are created to implement the queries. The basic operation included in relational algebra are: 

1. Select (σ)
2. Project (Π)
3. Union (U)
4. Set Difference (-)
5. Cartesian product (X)
6. Rename (ρ) 


### Relational Calculus（关系演算）
Relational Calculus is the formal query language. It is also known as **Declarative language**. In Relational Calculus, the order is not specified in which the operation has to be performed. Relational Calculus means what result we have to obtain.   
Relational Calculus has two variations: 

1.  [Tuple Relational Calculus (TRC)](https://www.geeksforgeeks.org/dbms-tupple-relational-calculus/)
2.  [Domain Relational Calculus (DRC)](https://www.geeksforgeeks.org/dbms-domain-relational-calculus/)

Relational Calculus is denoted as:
```
{ t | P(t) }

Where,
t: the set of tuples
p: is the condition which is true for the given set of tuples.
```



### Difference between Relational Algebra and Relational Calculus
| NO |      Basis of Comparison      |                      Relational Algebra                      |                     Relational Calculus                      |
| :--: | :---------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|  1.  |       **Language Type**       |                 It is a Procedural language.                 | Relational Calculus is a Declarative (non-procedural) language. |
|  2.  |         **Procedure**         |      Relational Algebra means how to obtain the result.      |   Relational Calculus means what result we have to obtain.   |
|  3.  |           **Order**           | In Relational Algebra, the order is specified in which the operations have to be performed. |     In Relational Calculus, the order is not specified.      |
|  4.  |          **Domain**           |       Relational Algebra is independent of the domain.       | Relation Calculus can be domain-dependent because of domain relational calculus. |
|  5.  |   **Programming language**    |   Relational Algebra is nearer to a programming language.    | Relational Calculus is not nearer to programming language but to natural language. |
|  6.  |     **Inclusion in SQL**      | The SQL includes only some features from the relational algebra. | SQL is based to a greater extent on the tuple relational calculus. |
|  7.  | **Relationally completeness** | Relational Algebra is one of the languages in which queries can be expressed but the queries should also be expressed in relational calculus to be relationally complete. | For a database language to be relationally complete, the query written in it must be expressible in relational calculus. |
|  8.  |     **Query Evaluation**      | The evaluation of the query relies on the order specification in which the operations must be performed. | The order of operations does not matter in relational calculus for the evaluation of queries. |
|  9.  |      **Database access**      | For accessing the database, relational algebra provides a solution in terms of what is required and how to get that information by following a step-by-step description. | For accessing the database, relational calculus provides a solution in terms as simple as what is required and lets the system find the solution for that. |
| 10.  |      **Expressiveness**       | The expressiveness of any given language is judged using relational algebra operations as a standard. | The completeness of a language is measured in the manner that it is least as powerful as calculus. That implies relation defined using some expression of the calculus is also definable by some other expression, the language is in question. |



## Relational DDL


## Relational DML
### 🦆 Relational DQL
↗ [Appendix](🩼%20SQL/Appendix.md)



## Relational DCL



## Ref
[关系代数(Relational Algebra)概览]: https://blog.csdn.net/zsi386/article/details/79091307
[数据库复习9——关系代数和关系演算]: https://www.cnblogs.com/claireyuancy/p/7217371.html
