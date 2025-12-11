---
layout: default
title: "SQL Study 005 – ORDER BY, LIMIT, GROUP BY, HAVING (EN)"
date: 2025-12-10
order: 5
---

# SQL Study 005 – ORDER BY, LIMIT, GROUP BY, HAVING (EN)

This chapter explains how to:

- sort query results with **ORDER BY**
- limit the number of rows with **LIMIT**
- aggregate data with **GROUP BY**
- filter aggregated results with **HAVING**

using the `staff` table.

---

## 1. Concept of ORDER BY

- ORDER BY is used to **sort the rows in the result set**.
- You can sort by numbers, strings, or dates in **ascending (ASC)** or **descending (DESC)** order.
- It only changes **the display order of results**, not the actual stored data.

---

## 2. Basic ORDER BY Syntax

```sql
SELECT column_list
FROM table_name
ORDER BY column_name [ASC | DESC];
```
ASC : ascending (default)
DESC : descending

### 2-1. Using Aliases in ORDER BY

```sql
SELECT salary * 12 AS annual_salary
FROM staff
ORDER BY annual_salary DESC;
```

An alias defined in SELECT (annual_salary) can be used in ORDER BY.
But aliases cannot be used in the WHERE clause.

---

## 3. Concept of LIMIT

LIMIT restricts the number of rows returned by a query.
It is useful for “top N” queries or pagination.

--- 

## 4. Basic LIMIT Syntax

```sql
SELECT column_list
FROM table_name
LIMIT n;
```

Example:

```sql
SELECT name_ko, salary
FROM staff
ORDER BY salary DESC
LIMIT 5;
```
→ Returns the top 5 employees with the highest salary.

### 4-1. LIMIT + OFFSET (Pagination)

```sql
SELECT *
FROM staff
ORDER BY staff_id
LIMIT 5 OFFSET 5;
```
→ Returns 5 rows starting from the 6th row (after sorting by staff_id).

---

## 5. Concept of GROUP BY

GROUP BY groups rows that have the same value in one or more columns.
It is commonly used with aggregate functions like COUNT, SUM, AVG, MAX, MIN.
<aside>
Typical use cases: “headcount by team”, “average salary by position”, etc.

---

## 6. Basic GROUP BY Syntax

```sql
SELECT 그룹기준컬럼, 집계함수(컬럼)
FROM 테이블명
GROUP BY 그룹기준컬럼;
```

### 6-1. Aggregate Functions

| Function | Meaning | Example use      |
| -------- | ------- | ---------------- |
| COUNT()  | count   | number of people |
| SUM()    | sum     | total salary     |
| AVG()    | average | average salary   |
| MAX()    | maximum | highest salary   |
| MIN()    | minimum | lowest salary    |

---

## 7. Concept of HAVING

HAVING is used to filter grouped results after GROUP BY.
WHERE filters individual rows.
HAVING filters aggregated groups (e.g., only groups whose average salary ≥ 7000).

---

## 8. Basic HAVING Syntax

```sql
SELECT group_column, aggregate_function(column)
FROM table_name
GROUP BY group_column
HAVING group_condition;
```

## 9. Practice Problems

### Problem 1:
From the staff table, retrieve employees whose salary is at least 5000,
and return only the top 3 rows with the highest salary.

<details markdown="1"> 
<summary>Answer</summary>

```sql
SELECT *
FROM staff
WHERE salary >= 5000
ORDER BY salary DESC
LIMIT 3;
```
</details>

### Problem 2:

From the staff table, retrieve employees whose salary is at least 5000,
sorted by salary in descending order, but skip the top 3 rows and return the next 5 rows.

<details markdown="1"> 
<summary>Answer</summary>

```sql
SELECT *
FROM staff
WHERE salary >= 5000
ORDER BY salary DESC
LIMIT 5 OFFSET 3;
```
</details>

### Problem 3:

Calculate the headcount for each team in the staff table.

Example result:

| Team ID | Headcount |
| ------: | --------: |
|    NULL |         1 |
|      10 |         1 |
|      11 |         6 |
|      12 |         3 |
|      40 |         1 |
|      80 |         2 |


<details markdown="1"> 
<summary>Answer</summary>

```sql
SELECT team_id, COUNT(*) AS 'Headcount'
FROM staff
GROUP BY team_id;
```
</details>

### Problem 4:

Retrieve only those positions whose average salary is at least 7000.

Example result:

| Position  | AvgSalary  |
| --------- | ---------- |
| CEO       | 82000.0000 |
| Executive | 23000.0000 |
| Manager   | 14000.0000 |
| Deputy    | 10200.0000 |
| Lead      | 7650.0000  |

<details markdown="1"> 
<summary>Answer</summary>

```sql
SELECT position, AVG(salary) AS 'AvgSalary'
FROM staff
GROUP BY position
HAVING AVG(salary) >= 7000;
```
</details>

### Problem 5:

For each team, compute the maximum, minimum, and average salary.

Example result:

| Team ID | MaxSalary | MinSalary |  AvgSalary |
| ------: | --------: | --------: | ---------: |
|    NULL |     82000 |     82000 | 82000.0000 |
|      10 |     23000 |     23000 | 23000.0000 |
|      11 |     16000 |      4850 |  8450.0000 |
|      12 |     12500 |      4520 |  8205.0000 |
|      40 |      6050 |      6050 |  6050.0000 |
|      80 |     13500 |      5050 |  9275.0000 |

<details markdown="1"> 
<summary>Answer</summary>

```sql
SELECT  team_id AS 'Team ID'
       ,MAX(salary) AS 'MaxSalary'
       ,MIN(salary) AS 'MinSalary'
       ,AVG(salary) AS 'AvgSalary'
FROM staff
GROUP BY team_id;
```
</details> 
