---
layout: default
title: "SQL Study 004 – Filtering Data with WHERE (EN)"
date: 2025-12-10
order: 4
---

# SQL Study 004 – Filtering Data with WHERE (EN)

This chapter explains how to filter data using the WHERE clause  
and how to apply conditions when querying the `staff` table.

---

## 1. Concept of the WHERE Clause

### 1-1. Definition
- WHERE specifies the **filter conditions** for rows to be returned.
- It is used to **extract only the rows that meet certain criteria** from the full dataset.

---

## 2. Basic Syntax

```sql
SELECT column_list
FROM table_name
WHERE condition;
```

Example:

```sql
SELECT name_ko, position
FROM staff
WHERE team_id = 11;
```

---

## 3. Common Operators Used in WHERE

### 3-1. Arithmetic Operators

| Operator | Meaning     | Example |
| -------- | ----------- | ------- |
| +        | addition    | 10 + 3  |
| -        | subtraction | 10 - 3  |
| *        | multiply    | 10 * 3  |
| /        | divide      | 10 / 3  |
| %        | remainder   | 10 % 3  |


### 3-2. Comparison Operators

| Operator | Meaning          | Example        |
| -------- | ---------------- | -------------- |
| =        | equal            | salary = 3000  |
| != , <>  | not equal        | team_id != 10  |
| >        | greater than     | salary > 3000  |
| <        | less than        | salary < 3000  |
| >=       | greater or equal | salary >= 3000 |
| <=       | less or equal    | salary <= 3000 |


---

## 4. WHERE + AND / OR (Multiple Conditions)

### 4-1. AND: All conditions must be true

```sql
SELECT *
FROM staff
WHERE team_id = 11
  AND salary >= 7000;
```
→ Returns employees who belong to team 11 AND have salary ≥ 7000.


### 4-2. OR: At least one condition is true

```sql
SELECT *
FROM staff
WHERE team_id = 11
   OR team_id = 12;
```
→ Returns employees whose team_id is 11 or 12.

---

## 5. WHERE + BETWEEN (Range Conditions)

```sql
SELECT name_ko, salary
FROM staff
WHERE salary BETWEEN 5000 AND 8000;
```
→ Returns employees whose salary is between 5000 and 8000 (inclusive).


Using BETWEEN with dates:
```sql
SELECT name_ko, hired_at
FROM staff
WHERE hired_at BETWEEN '2018-01-01' AND '2020-12-31';
```

### 5-1. Caution with DATETIME / TIMESTAMP

You can also use BETWEEN with dates.
```sql
WHERE hired_at BETWEEN '2023-01-01' AND '2023-12-31'
```

BETWEEN '2023-01-01' AND '2023-12-31' is actually interpreted as:
Start: 2023-01-01 00:00:00
End: 2023-12-31 00:00:00

So:
✅ 2023-12-31 00:00:00 → included
❌ 2023-12-31 13:00:00 → not included
❌ 2023-12-31 23:59:59 → not included

---

## 6. WHERE + IN (List Conditions)

```sql
SELECT *
FROM staff
WHERE team_id IN (10, 11, 12);
```
→ Returns employees whose team_id is 10, 11, or 12.

This is more readable than writing multiple OR conditions:
```sql
WHERE team_id = 10
   OR team_id = 11
   OR team_id = 12;
```

---

## 7. WHERE + LIKE (Pattern Matching)

| Pattern | Meaning                              |
| ------- | ------------------------------------ |
| %A%     | contains A                           |
| A%      | starts with A                        |
| %A      | ends with A                          |
| _A      | second character is A                |
| A_      | two-character string starting with A |

Example:
```sql
SELECT *
FROM staff
WHERE name_ko LIKE '윤%';
```
→ Returns employees whose Korean name starts with '윤'.

---

## 8. WHERE + IS NULL / IS NOT NULL

### 8-1. Syntax
| Expression  | Meaning                 |
| ----------- | ----------------------- |
| IS NULL     | value is missing (NULL) |
| IS NOT NULL | value exists (not NULL) |

Example: employees who have a bonus

```sql
SELECT *
FROM staff
WHERE bonus IS NOT NULL;
```

Employees with no bonus:
```sql
SELECT *
FROM staff
WHERE bonus IS NULL;
```

### 8-2. What is NULL?

NULL means “no value / unknown / not set yet”.
It is different from 0 or an empty string ''.
That’s why we must use IS NULL instead of = NULL.

---

## 9. Practice Problems

### Problem 1:
Retrieve all rows from staff where the position is 'Deputy'.

<details markdown="1"> 
<summary>Answer</summary>

```sql
SELECT *
FROM staff
WHERE position = 'Deputy';
```
</details>

### Problem 2:
Retrieve employees whose team_id is not 11.

<details markdown="1">
<summary>Answer</summary>

```sql  
SELECT *
FROM staff
WHERE team_id != 11;
```

or

```sql
SELECT *
FROM staff
WHERE team_id <> 11;
```
</details>

### Problem 3:
Retrieve employees who belong to team 11
and whose position is either 'Lead' or 'Senior'.

<details markdown="1">
<summary>Answer</summary>

```sql  
SELECT *
FROM staff
WHERE team_id = 11
  AND position IN ('Lead', 'Senior');
```

or

```sql
SELECT *
FROM staff
WHERE team_id = 11
  AND (position = 'Lead' OR position = 'Senior');
```
</details>

### Problem 4:
Retrieve employees whose bonus is NULL.

<details markdown="1"> 
<summary>Answer</summary>

```sql
SELECT *
FROM staff
WHERE bonus IS NULL;
```
</details>

### Problem 5:
Retrieve employees whose second character of name_ko is '운'
(e.g., 김운항).

<details markdown="1"> 
<summary>Answer</summary>

```sql  
SELECT *
FROM staff
WHERE name_ko LIKE '_운%';
```
</details> 
