# Database Environment

[TOC]


## Overview
![](../../../../Assets/Pics/Screenshot%202023-03-06%20at%204.44.56%20PM.png)

### View - Schema - Model
View: A view is essentially some subset of the database
Schema: A schema is a unique structured view. 
Model: A model is the schema of a set of schemas. 



## ANSI-SPARC Three-Level Architecture
#TODO (i didn't understand this part ....)

![](../../../../Assets/Pics/Screenshot%202023-03-06%20at%204.34.58%20PM.png)

![](../../../../Assets/Pics/Screenshot%202023-03-06%20at%204.38.41%20PM.png)

### 1️⃣ Internal Level
Internal Level
- Physical representation of the database on the computer
- Describes how the data is stored in the database

1. Storage space allocation for data and indexes
2. Record description for storage (with stored sizes for data items)  
3. Record placement(安放)  
4. Data compression(压缩) and encryption techniques

#### Internal Schema ---- Internal View

### C-I Mapping
Conceptual Schema-Internal Schema Mapping


### 2️⃣ Conceptual Level
Conceptual Level
- Community view of the database  
- Describes what data is stored in database and relationships among the data

1. All entities, their attributes and their relationships
2. The constraints on the data  
3. Semantic information about the data  
4. Security and integrity information

#### (Conceptual) Schema ---- Conceptual View

### E-C Mapping
External Schema-Conceptual Schema Mapping


### 3️⃣ External Level
External Level
- Users’ view of the database
- Describes that part of database that is relevant to a particular user

The view is the ‘real world’ represented in a form that is familiar for users

#### External Schema ---- (External) View


## Models
### Conceptual Models


### Data Models
Object-Based Data Models
- Entity-Relationship
- Semantic  
- Functional  
- Object-Oriented

Record-Based Data Models
- Relational Data Model  
- Network Data Model (Mesh Data Model)
- Hierarchical Data Model

Physical Data Models

## Record-Based Data Models
### Hierarchical Data Models
#TODO 

### Network Data Models


### Relational Data Models

Relational databse maps many sheets 📈 together to store & orgnize data. 
List of several popular relational databse: 

1. 商用数据库，例如：[Oracle](https://www.oracle.com/)，[SQL Server](https://www.microsoft.com/sql-server/)，[DB2](https://www.ibm.com/db2/)等；
2. 开源数据库，例如：[MySQL](https://www.mysql.com/)，[PostgreSQL](https://www.postgresql.org/)等；
3. 桌面数据库，以微软[Access](https://products.office.com/access)为代表，适合桌面应用程序使用；
4. 嵌入式数据库，以[Sqlite](https://sqlite.org/)为代表，适合手机应用和桌面程序。


## Ref
