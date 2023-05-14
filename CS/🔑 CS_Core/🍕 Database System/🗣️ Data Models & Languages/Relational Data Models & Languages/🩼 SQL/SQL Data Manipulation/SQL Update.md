# SQL Update

[TOC]



## Res


## `INSERT` Statement
There are two forms of the INSERT statement. The first allows a single row to be inserted into a named table and has the following format:
```sql
INSERT INTO TableName [(columnList)]
VALUES (dataValueList)
```
TableName may be either a base table or an updatable view (see Section 7.4), and columnList represents a list of one or more column names separated by commas. The columnList is optional; if omitted, SQL assumes a list of all columns in their origi- nal CREATE TABLE order. If specified, then any columns that are omitted from the list must have been declared as NULL columns when the table was created,unless the DEFAULT option was used when creating the column (see Section 7.3.2).

The dataValueList must match the columnList as follows:
- The number of items in each list must be the same.
- There must be a direct correspondence in the position of items in the two lists, so that the first item in dataValueList applies to the first item in columnList, the second item in dataValueList applies to the second item in columnList, and so on.
- The data type of each item in dataValueList must be compatible with the data type of the corresponding column.


## Modifying data in the database (`UPDATE`)
The UPDATE statement allows the contents of existing rows in a named table to be changed. The format of the command is:
```sql
UPDATE TableName  
SET columnName1 = dataValue1 [, columnName2 = dataValue2 . . .]
[WHERE searchCondition]
```

TableName can be the name of a base table or an updatable view (see Section 7.4). The SET clause specifies the names of one or more columns that are to be updated. The WHERE clause is optional; if omitted, the named columns are updated for all rows in the table. If a WHERE clause is specified, only those rows that satisfy the searchCondition are updated. The new dataValue(s) must be compatible with the data type(s) for the corresponding column(s).



## `DELETE` Statement

```sql
DELETE FROM TableName
[WHERE searchCondition]
```



## Ref

