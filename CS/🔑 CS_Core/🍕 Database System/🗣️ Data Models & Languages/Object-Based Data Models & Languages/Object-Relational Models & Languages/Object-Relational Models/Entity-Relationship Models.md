# ER (Entity-Relationship) Models

[TOC]



## Res
↗ [SE /Design & Modeling & Docs /UML](../../../../../../Software%20Engineering/CASE%20Tools/Upper%20CASE%20Tools/Design%20&%20Visualization%20Tools/Modeling%20Tools/UML/UML.md)

↗ [SE /Design & Modeling & Docs /ERD](../../../../../../Software%20Engineering/CASE%20Tools/Upper%20CASE%20Tools/Design%20&%20Visualization%20Tools/Database%20Logical%20Design%20Tools/ERD.md)



## Intro
![](../../../../../../../Assets/Pics/Screenshot%202023-04-23%20at%209.08.56%20PM.png)


### Entity Types

#### Strong and Weak Entity Types
Strong entity type: An entity type that is not existence-dependent on some other entity type.

Week entity tyep: An entity type that is existence-dependent on some other entity type.


![](../../../../../../../Assets/Pics/Screenshot%202023-04-23%20at%209.17.44%20PM.png)



### Relationship Types
A set of meaningful associations among entity types.


A uniquely identifiable association that includes one occurrence from each participating entity type.

#### Semantic Net


#### Diagrammatic Representation of Relationship Types


#### Degree of Relationship Type
![](../../../../../../../Assets/Pics/Screenshot%202023-04-23%20at%209.10.45%20PM.png)

![](../../../../../../../Assets/Pics/Screenshot%202023-04-23%20at%209.10.54%20PM.png)

![](../../../../../../../Assets/Pics/Screenshot%202023-04-23%20at%209.11.55%20PM.png)

Diagrammatic representation of complex relationships


#### Recursive Relationship
![](../../../../../../../Assets/Pics/Screenshot%202023-04-23%20at%209.12.22%20PM.png)


### Attributes
Simple attributes: An attribute composed of a single component with an independent existence.

Composite attributes: An attribute composed of multiple components, each with an inde- pendent existence.


Single-valuted attributes: An attribute that holds a single value for each occurrence of an entity type.


Multi-valuted attributes: An attribute that holds multiple values for each occurrence of an entity type.


Derived attributes: An attribute that represents a value that is derivable from the value of a related attribute or set of attributes, not necessarily in the same entity type.


![](../../../../../../../Assets/Pics/Screenshot%202023-04-23%20at%209.16.30%20PM.png)

![](../../../../../../../Assets/Pics/Screenshot%202023-04-23%20at%209.19.50%20PM.png)


### Keys
Candidate keys: The minimal set of attributes that uniquely identifies each occur- rence of an entity type.

Primary keys: The candidate key that is selected to uniquely identify each occur- rence of an entity type.

Composite keys: A candidate key that consists of two or more at


### Structural Constraints
#### Multiplicity
Multiplicity: The number (or range) of possible occurrences of an entity type that may relate to a single occurrence of an associated entity type through a particular relationship.


#### Multiplicity for Complex Relationships
Multiplicity (complex relationship): The number (or range) of possible occurrences of an entity type in an n-ary relationship when the other (n–1) values are fixed.

![](../../../../../../../Assets/Pics/Screenshot%202023-04-23%20at%209.26.09%20PM.png)



#### Cardinality and Participation Constraints
Cardinality: Describes the maximum number of possible relationship occur- rences for an entity participating in a given relationship type.

Participation: Determines whether all or only some entity occurrences partici- pate in a relationship.

![](../../../../../../../Assets/Pics/Screenshot%202023-04-23%20at%209.26.47%20PM.png)



## Problems with ER Models
### Fan Traps


### Chasm Traps



## EER (Enhanced Entity-Relationship)
### Specialization /Generalization (特殊化/泛化)
#### Superclasses /Subclasses & Relationships


#### Attribute Inheritance


#### Specialization / Generalization Process

#### Constraints on Specialization/Generalization
##### Participation Constraints

##### Disjoint Constraints

![](../../../../../../../Assets/Pics/Screenshot%202023-04-23%20at%209.35.34%20PM.png)


![](../../../../../../../Assets/Pics/Screenshot%202023-04-23%20at%209.36.32%20PM.png)


### Aggregation
Aggregation: Represents a “has-a” or “is-part-of” relationship between entity types, where one represents the “whole” and the other the “part.”

A relationship represents an association between two entity types that are con- ceptually at the same level. Sometimes we want to model a “has-a” or “is-part-of” relationship, in which one entity represents a larger entity (the “whole”), consist- ing of smaller entities (the “parts”). This special kind of relationship is called an aggregation (Booch et al., 1998). Aggregation does not change the meaning of navigation across the relationship between the whole and its parts, or link the lifetimes of the whole and its parts. An example of an aggregation is the Has relationship, which relates the Branch entity (the “whole”) to the Staff entity (the “part”).

![](../../../../../../../Assets/Pics/Screenshot%202023-04-23%20at%209.38.04%20PM.png)



### Composition
Composition: A specific form of aggregation that represents an association between entities, where there is a strong ownership and coinciden- tal lifetime between the “whole” and the “part.”

Aggregation is entirely conceptual and does nothing more than distinguish a “whole” from a “part.” However, there is a variation of aggregation called composition that represents a strong ownership and coincidental lifetime between the “whole” and the “part” (Booch et al., 1998). In a composite, the “whole” is responsible for the disposi- tion of the “parts,” which means that the composition must manage the creation and destruction of its “parts.” In other words, an object may be part of only one composite at a time. There are no examples of composition in Figure 13.8. For the purposes of discussion, consider an example of a composition, namely the Displays relationship, which relates the Newspaper entity to the Advert entity. As a composition, this emphasizes the fact that an Advert entity (the “part”) belongs to exactly one Newspaper entity (the “whole”). This is in contrast to aggregation, in which a part may be shared by many wholes. For example, a Staff entity may be “a part of” one or more Branches entities.

UML represents composition by placing a filled-in diamond shape at one end of the relationship line next to the entity that represents the “whole” in the relation- ship. For example, to represent the Newspaper Displays Advert composition, the filled- in diamond shape is placed next to the Newspaper entity, which is the “whole” in this relationship, as shown in Figure 13.10.

![](../../../../../../../Assets/Pics/Screenshot%202023-04-23%20at%209.38.15%20PM.png)



## Ref


