# Normalization

[TOC]



## Res


## Intro
Normalization is a database design technique that begins by examining the relationships (called **functional dependencies**) between **attributes**. Attributes describe some property of the data or of the relationships between the data that is important to the enterprise. Normalization uses a series of tests (described as **normal forms**) to help identify the optimal grouping for these attributes to ultimately identify a set of suitable relations that supports the data requirements of the enterprise.


### Purpose of Normalization
Normalization is a technique for producing a set of relations with desirable properties, given the data requirements of an enterprise.

Characteristics of a suitable set of relations include:
- the **minimal number of attributes** necessary to support the data requirements of the enterprise
- **attributes with a close logical relationship** are found in the same relation
- ⭐ **minimal redundancy** with each attribute represented only once with the important exception of attributes that form all or part of foreign keys.

The benefits of using a database that has a suitable set of relations is that the database will be:
- easier for the user to access and maintain the data
* take up minimal storage space on the computer


### How Normalization Supports Database Design
1. Used as a bottom-up standalone technique
2. Used as a validation technique to check the structure of relations, which may have been created using a top-down approach such as ER modeling

![](../../../../../../../../Assets/Pics/Screenshot%202023-04-22%20at%208.19.41%20PM.png)



## Data Redundancy & Update Anomalies
### Benifits of Minimal Data Redundancy
If this aim is achieved, potential benefits for implemented database include:
- Updates to the data stored in the database are achieved with a minimal number of operations thus reducing the opportunities for **data inconsistencies**.
- Reduction in the **file storage space** required by the base relations thus minimizing costs.


### Update Anomalies with Redundant Data
#### Insertion Anomalies

#### Deletion Anomalies


#### Modification Anomalies


### Principles of Decomposing
We can avoid these update anomalies by decomposing the original relation into the Staff and Branch relations. There are two important properties associated with decompo- sition of a larger relation into smaller relations:
- The **lossless-join** property ensures that any instance of the original relation can be identified from corresponding instances in the smaller relations.
- The **dependency preservation** property ensures that a constraint on the original relation can be maintained by simply enforcing some constraint on each of the smaller relations. In other words, we do not need to perform joins on the smaller relations to check whether a constraint on the original relation is violated.



## 👩‍❤️‍👨 Functional Dependencies
### Characteristics of Functional Dependencies
![](../../../../../../../../Assets/Pics/Screenshot%202023-04-22%20at%209.06.11%20PM.png)

**Functional dependency** is a property of the meaning or semantics of the attrib- utes in a relation. The semantics indicate how attributes relate to one another, and specify the functional dependencies between attributes. When a functional dependency is present, the dependency is specified as a **constraint** between the attributes.

When a functional dependency exists, the attribute or group of attributes on the left-hand side of the arrow is called the **determinant**. For example, in Figure above, A is the determinant of B. We demonstrate the identification of a functional dependency in the following example.

![](../../../../../../../../Assets/Pics/Screenshot%202023-04-22%20at%209.07.04%20PM.png)

#### Full Functional Dependency
An additional characteristic of functional dependencies that is useful for normalization is that their determinants should have the minimal number of attributes necessary to maintain the functional dependency with the attribute(s) on the righthand side. This requirement is called **full functional dependency**.

#### Transitive Dependency
**Transitive Dependency**: A condition where a, B, and C are attributes of a relation such that if a ® B and B ® C, then C is transitively dependent on a via B (provided that a is not functionally dependent on B or C).


### Identifying Functional Dependency
![](../../../../../../../../Assets/Pics/Screenshot%202023-04-22%20at%209.13.19%20PM.png)


### Identifying the Primary Key for a Relation Using Functional Dependencies
skip


### 🧭 Inference Rules for Functional Dependencies

How do we begin to identify useful functional dependencies on a relation? Normally, the database designer starts by specifying functional dependencies that are semantically obvious; however, there are usually numerous other functional dependencies. In fact, the task of specifying all possible functional dependencies for “real” database projects is more often than not impractical. However, in this section we do consider an approach that helps identify the complete set of func- tional dependencies for a relation and then discuss how to achieve a minimal set of functional dependencies that can represent the complete set.

#### Closure of Functional Dependencies
The set of all functional dependencies that are implied by a given set of functional dependencies X is called the **closure** of X, written X+. We clearly need a set of rules to help compute X+ from X. 

#### Armstrong's Axioms
A set of inference rules, called Armstrong’s axioms, specifies how new functional dependencies can be inferred from given ones (Armstrong, 1974). For our discussion, let A, B, and C be subsets of the attributes of the relation R. Armstrong’s axioms are as follows:
1. **Reflexivity**: If B is a subset of a, then a ® B
2. **Augmentation**: If a ® B, then a,C ® B,C  
3. **Transitivity**: If a ® B and B ® C, then a ® C

Note that each of these three rules can be directly proved from the definition of functional dependency.
- The rules are **complete** (完备的) in that given a set X of functional dependencies, all functional dependencies implied by X can be derived from X using these rules. 
- The rules are also **sound**（有效的）in that no additional functional depend- encies can be derived that are not implied by X. In other words, the rules can be used to derive the closure of X+.

#### Further Derived Rules
Several further rules can be derived from the three given previously that simplify the practical task of computing X+. In the following rules, let D be another subset of the attributes of relation r. Then:
4. **Self-determination**: a®a
5. **Decomposition**: f a ® B,C, then a ® B and a ® C
6. **Union**: If a ® B and a ® C, then a ® B,C
7. **Composition**: If a®B and C®D then a,C®B,D


### Minimal Sets of Functional Dependencies
In this section we introduce what is referred to as **equivalence** of sets of functional dependencies. A set of functional dependencies Y is covered by a set of functional dependencies X, if every functional dependency in Y is also in X+; that is, every dependency in Y can be inferred from X. A set of functional dependencies X is minimal if it satisfies the following conditions:
- Every dependency in X has a single attribute on its right-hand side.
- We cannot replace any dependency a ® B in X with dependency C ® B, where C is a proper subset of a, and still have a set of dependencies that is equivalent to X.
- We cannot remove any dependency from X and still have a set of dependencies that is equivalent to X.

A minimal set of dependencies should be in a standard form with no redundancies. A minimal cover of a set of functional dependencies X is a minimal set of dependencies Xmin that is equivalent to X. Unfortunately, there can be several minimal covers for a set of functional dependencies.



## The Process of Normalization
Normalization is a formal technique for analyzing relations based on their **primary key** (or candidate keys) and **functional dependencies** (Codd, 1972b). The technique involves a series of rules that can be used to test individual relations so that a database can be normalized to any degree. When a requirement is not met, the relation violating the requirement must be decomposed into relations that individually meet the requirements of normalization.


### Normal Forms
Three normal forms were initially proposed called First Normal Form (1NF), Second Normal Form (2NF), and Third Normal Form (3NF). Subsequently, R. Boyce and E. F. Codd introduced a stronger definition of third normal form called Boyce–Codd Normal Form (BCNF) (Codd, 1974). With the exception of 1NF, all these normal forms are based on functional dependencies among the attributes of a relation (Maier, 1983). Higher normal forms that go beyond BCNF were introduced later such as Fourth Normal Form (4NF) and Fifth Normal Form (5NF) (Fagin, 1977, 1979). However, these later normal forms deal with situations that are very rare.

![](../../../../../../../../Assets/Pics/Screenshot%202023-04-22%20at%209.17.51%20PM.png)

Normalization is often executed as a series of steps. Each step corresponds to a specific normal form that has known properties. As normalization proceeds, the relations become progressively more restricted (stronger) in format and also less vulnerable to update anomalies.

For the relational data model, it is important to recognize that it is only First Normal Form (1NF) that is critical in creating relations; all subsequent normal forms are optional. However, to avoid the update anomalies it is generally recommended that we proceed to at least Third Normal Form (3NF)


### ⭐️ Process of Normalization
![](../../../../../../../../Assets/Pics/Screenshot%202023-04-22%20at%209.17.42%20PM.png)


#### Unnormalizaed Form (UNF)
A table that contains one or more repeating groups.

#### 1NF
A relation in which the intersection of each row and column contains one and only one value.

#### 2NF
A relation that is in first normal form and every non-primary-key attribute is fully functionally dependent on the primary key.

🤔 General Definition: A relation that is in first normal form and every non- candidate-key attribute is fully functionally dependent on any candidate key.


#### 3NF
A relation that is in first and second normal form and in which no non-primary-key attribute is transitively dependent on the primary key.

🤔 General Definition: A relation that is in first and second normal form and in which no non-candidate-key attribute is transitively dependent on any candidate key.

![](../../../../../../../../Assets/Pics/Screenshot%202023-04-22%20at%209.27.37%20PM.png)


> 💡 **General Definitions of 2NF and 3NF**
> 
> When using the general definitions of 2NF and 3NF, we must be aware of partial and transitive dependencies on all candidate keys and not just the primary key. This can make the process of normalization more complex; however, the general definitions place additional constraints on the relations and may identify hidden redundancy in relations that could be missed.
> 
> The trade-off is whether it is better to keep the process of normalization simpler by examining dependencies on primary keys only, which allows the identification of the most problematic and obvious redundancy in relations, or to use the general definitions and increase the opportunity to identify missed redundancy. In fact, it is often the case that whether we use the definitions based on primary keys or the general definitions of 2NF and 3NF, the decomposition of relations is the same.

#### BCNF
A relation is in BCNF if and only if every determinant is a candidate key.

The potential to violate BCNF may occur when:
• the relation contains two (or more) composite candidate keys or  
• the candidate keys overlap, that is having at least one attribute in common.

---
**范式应用**
🔗 https://www.cnblogs.com/coky/p/7220363.html


我们来逐步搞定一个论坛的数据库，有如下信息：
> （1） 用户：用户名，email，主页，电话，联系地址
> （2） 帖子：发帖标题，发帖内容，回复标题，回复内容


1️⃣ 第一次我们将数据库设计为仅仅存在表：
> 用户名 email 主页 电话 联系地址 发帖标题 发帖内容 回复标题 回复内容

这个数据库表符合第一范式，但是没有任何一组候选关键字能决定数据库表的整行，唯一的关键字段用户名也不能完全决定整个元组。我们需要增加"发帖ID"、"回复ID"字段，即将表修改为：
> 用户名 email 主页 电话 联系地址 发帖ID 发帖标题 发帖内容 回复ID 回复标题 回复内容

这样数据表中的关键字(用户名，发帖ID，回复ID)能决定整行：
> (用户名,发帖ID,回复ID) → (email,主页,电话,联系地址,发帖标题,发帖内容,回复标题,回复内容)


2️⃣ 但是，这样的设计不符合第二范式，因为存在如下决定关系:
> (用户名) → (email,主页,电话,联系地址)
> (发帖ID) → (发帖标题,发帖内容)
> (回复ID) → (回复标题,回复内容)   

即非关键字段部分函数依赖于候选关键字段，很明显，这个设计会导致大量的数据冗余和操作异常。

我们将数据库表分解为（带下划线的为关键字）:
>（1）用户信息：用户名，email，主页，电话，联系地址
>（2）帖子信息：发帖ID，标题，内容
>（3）回复信息：回复ID，标题，内容
>（4）发贴：用户名，发帖ID
>（5）回复：发帖ID，回复ID   

这样的设计是满足第1、2、3范式和BCNF范式要求的，但是这样的设计是不是最好的呢？   
不一定。   


3️⃣ 观察可知，第4项"发帖"中的"用户名"和"发帖ID"之间是1：N的关系，因此我们可以把"发帖"合并到第2项的"帖子信息"中；第5项"回复"中的"发帖ID"和"回复ID"之间也是1：N的关系，因此我们可以把"回复"合并到第3项的"回复信息"中。这样可以一定量地减少数据冗余，新的设计为：   
（1）用户信息：用户名，email，主页，电话，联系地址   
（2）帖子信息：用户名，发帖ID，标题，内容   
（3）回复信息：发帖ID，回复ID，标题，内容   

对上述新的设计进行分析：
- 数据库表1显然满足所有范式的要求：
- 数据库表2中存在非关键字“标题”、“内容”对关键字段“发帖ID”的部分函数依赖，即不满足第二范式的要求，但是这一设计并不会导致数据冗余和操作异常；
- 数据库表3中也存在非关键字段"标题"、"内容"对关键字段"回复ID"的部分函数依赖，也不满足第二范式的要求，但是与数据库表2相似，这一设计也不会导致数据冗余和操作异常；


🤔 由此可以看出，并不一定要强行满足范式的要求，
- **对于1：N关系**，当1的一边合并到N的那边后，N的那边就不再满足第二范式了，但是这种设计反而比较好！
- **对于M：N的关系**，不能将M一边或N一边合并到另一边去，这样会导致不符合范式要求，同时导致操作异常和数据冗余。
- **对于1：1的关系**，我们可以将左边的1或者右边的1合并到另一边去，设计导致不符合范式要求，但是并不会导致操作异常和数据冗余。 


**结论**
满足范式要求的数据库设计是结构清晰的，同时可避免数据冗余和操作异常。这并不意味着不符合范式要求的设计一定是错误的，在数据库表中存在1：1或1：N关系这种较特殊的情况下，合并导致的不符合范式要求反而是合理的。在我们设计数据库的时候，一定要时刻考虑范式的要求。

---


#### 4NF


#### 5NF




## Ref
[BNCF 示例]: https://blog.kazge.com/数据库/2011/10/21/bcnf-e7-a4-ba-e4-be-8b/
[数据库范式1NF 2NF 3NF BCNF(实例）通俗易懂的讲解]: https://www.cnblogs.com/coky/p/7220363.html

