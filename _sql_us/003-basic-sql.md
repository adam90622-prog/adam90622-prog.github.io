---
layout: default
title: "SQL Study 003 – Basic SQL (EN)"
date: 2025-12-10
order: 3
---

# SQL Study 003 – Basic SQL (EN)

This chapter covers the basic SELECT statement  
and explains how SQL retrieves data from a table.

---

## 1. Writing Order vs Execution Order

### 1-1. Writing Order (human perspective)
SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY

### 1-2. Execution Order (database perspective)
FROM → ON → JOIN → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY

---

## 2. Basics of SELECT ~ FROM

### 2-1. Definition  
SELECT is the most fundamental SQL command used to query data.

### 2-2. Basic Syntax

```sql
-- Select all columns
SELECT * FROM staff;

-- Select specific columns (alias)
SELECT name_ko AS 'Name', position AS 'Position'
FROM staff;
```

### 2-3. Key Elements

SELECT : choose columns
FROM : specify table

* : select all columns
AS : temporary alias for display

---
## 3. DISTINCT
DISTINCT removes duplicated values and returns unique results.
```sql
SELECT DISTINCT position
FROM staff;
```

---

## 4. Practice Problems

### Problem 1:
Retrieve all rows from the staff table.

<details> 
<summary>Answer</summary>

```sql
SELECT * FROM staff;
</details>
```

### Problem 2:
Retrieve staff ID, Korean name, and position as shown below:

| Staff ID | Name (KR) | Position  |
| ---- | --- | --------- |
| 1000     | 윤사령       | CEO       |
| 7001     | 백항해       | Executive |
| 7002     | 김운항       | Manager   |
| 4001     | 정민호       | Manager   |
| 7003     | 윤세진       | Manager   |
| 7004     | 한지우       | Deputy    |
| 7005     | 고은채       | Lead      |
| 7006     | 송도현       | Lead      |
| 7007     | 임하늘       | Senior    |
| 7008     | 조민재       | Senior    |
| 4002     | 백다은       | Senior    |
| 7009     | 오지훈       | Junior    |
| 7010     | 류서연       | Junior    |
| 8001     | 문건우       | FieldLead |

<details> <summary>Answer</summary>

```sql
SELECT  staff_id AS 'Staff ID'
       ,name_ko  AS 'Name (KR)'
       ,position AS 'Position'
FROM staff;
</details>
```

### Problem 3:
Retrieve the list of unique positions from the staff table.

<details> <summary>Answer</summary>

```sql
SELECT DISTINCT position
FROM staff;
</details>
```
