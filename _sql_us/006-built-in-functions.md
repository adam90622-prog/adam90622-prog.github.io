---
layout: default
title: "SQL Study 006 – Built-in Functions (EN)"
date: 2025-12-10
order: 6
---

# SQL Study 006 – Built-in Functions (EN)

This chapter explains commonly used **SQL built-in functions**  
based on the table structure of `staff`.

Table used: **staff**

```sql
CREATE TABLE staff (
  staff_id   INT PRIMARY KEY,
  name_ko    VARCHAR(50),
  name_en    VARCHAR(100),
  position   VARCHAR(50),
  manager_id INT,
  hired_at   DATE,
  salary     INT,
  bonus      INT,
  team_id    INT,
  is_active  BOOLEAN
);
```

---

# 1. What Are Built-in Functions?

A function takes input values, performs a calculation, and returns a result.
SQL functions are categorized as follows:

## 1-1. Single-Row Functions
- String functions  
- Numeric functions  
- Date/Time functions  
- Conversion functions  
- NULL-related functions  

→ Return **one result per row**

## 1-2. Multi-Row Functions
- Aggregate functions  
- Group functions  
- Window functions  
→ These functions receive multiple rows and return summary results.

---

# 2. String Functions

## 2-1. Common String Functions

| Function | Description | Example |
|---------|-------------|---------|
| UPPER() | Convert to uppercase | `UPPER(name_en)` |
| LOWER() | Convert to lowercase | `LOWER(name_en)` |
| LENGTH() | Byte length | `LENGTH(name_ko)` |
| CHAR_LENGTH() | Character length (correct for Korean) | `CHAR_LENGTH(name_ko)` |
| LEFT() | Extract characters from the left | `LEFT('BIGDATA', 3)` |
| RIGHT() | Extract characters from the right | `RIGHT('BIGDATA', 4)` |
| SUBSTRING() | Extract substring | `SUBSTRING(name_ko, 2, 2)` |
| REPLACE() | Replace substring | `REPLACE(position, 'Manager', 'Executive')` |
| LTRIM() | Remove leading characters/spaces | `LTRIM(' ABC')` |
| RTRIM() | Remove trailing characters/spaces | `RTRIM('ABC ')` |
| TRIM() | Remove spaces from both sides | `TRIM(name_en)` |
| CONCAT() | Concatenate values | `CONCAT(name_ko, '님')` |
| LPAD() | Left-pad to a fixed length | `LPAD(name_ko, 5, '*')` |
| RPAD() | Right-pad to a fixed length | `RPAD(name_ko, 5, '*')` |
| POSITION() | Find substring position | `POSITION('D' IN 'BIGDATA')` |

> For Korean characters, always use **CHAR_LENGTH()**, not LENGTH().

---

## 2-2. Practice Problems (String Functions)

### Problem 1  
Display employee names in this format:

**Example output:**  
`Yoon Director [CEO]`

<details markdown="1">
<summary>Answer</summary>

```sql
SELECT CONCAT(name_ko, ' [', position, ']') AS 'Name [Position]'
FROM staff;
```
</details>

### Problem 2:
Count how many employees have each name length (Korean).

<details markdown="1"> 
<summary>Answer</summary>

```sql
SELECT CHAR_LENGTH(name_ko) AS 'Name Length',
       COUNT(*)            AS 'Count'
FROM staff
GROUP BY Name Length;
```
</details>

### Problem 3:

Retrieve employees whose name **ends with ‘현’**,
and print the English name in uppercase.

Example:
| Name | English Name |
| ---- | ------------ |
| 송도현  | SONG DOHYUN  |

<details markdown="1"> 
<summary>Answer</summary>

```sql
SELECT name_ko        AS 'Name',
       UPPER(name_en) AS 'English Name'
FROM staff
WHERE RIGHT(name_ko, 1) = '현';
```
</details>

### Problem 4:

For employee '김운항', display current position and
promoted position (부장 → 상무).

<details markdown="1"> 
<summary>Answer</summary>

```sql
SELECT name_ko                             AS 'Name',
       position                            AS 'Current Position',
       REPLACE(position, '부장', '상무')   AS 'Promoted Position'
FROM staff
WHERE name_ko = '김운항';
```
</details>

### Problem 5:

Mask names so that only the first character remains and the rest becomes **.

<details markdown="1"> 
<summary>Answer</summary>

```sql
SELECT position                       AS 'Position',
       CONCAT(LEFT(name_ko, 1), '**') AS 'Name',
       salary                         AS 'Salary',
       bonus                          AS 'Bonus'
FROM staff;
```
</details>

---

# 3. Numeric Functions

## 3-1. Main Numeric Functions

| Function      | Meaning             | Example              |
| ------------- | ------------------- | -------------------- |
| TRUNCATE(x,n) | Truncate decimals   | TRUNCATE(3.14159, 2) |
| ROUND(x,n)    | Round to n decimals | ROUND(3.14159, 2)    |
| MOD(a,b)      | Remainder           | MOD(10, 3)           |
| CEIL(x)       | Ceiling (round up)  | CEIL(3.2)            |
| FLOOR(x)      | Floor (round down)  | FLOOR(3.8)           |
| ABS(x)        | Absolute value      | ABS(-10)             |
| SIGN(x)       | Sign (-1, 0, 1)     | SIGN(-5)             |
| POWER(a,b)    | Exponent            | POWER(2, 3)          |
| SQRT(x)       | Square root         | SQRT(16)             |


---

## 3-2. Practice Problems

### Problem 1:

For employees with salary ≥ 6000, display:
- Name[Position]
- Salary
- Monthly salary (salary / 12, truncated)
- Sort by monthly salary DESC

<details markdown="1"> 
<summary>Answer</summary>
  
```sql
SELECT CONCAT(name_ko, ' [', position, ']') AS 'Name[Position]',
       salary                               AS 'Salary',
       TRUNCATE(salary / 12, 0)             AS 'Monthly Salary'
FROM staff
WHERE salary >= 6000
ORDER BY `Monthly Salary` DESC;
```
</details>

### Problem 2:

Compute bonus ratio:
| bonus ratio (%) = bonus / salary × 100

Conditions:
- Exclude bonus = 0
- Round to 2 decimals
- Show as “33.33%”
- Sort by ratio DESC

<details markdown="1"> 
<summary>Answer</summary>

```sql
SELECT name_ko AS 'Name',
       salary  AS 'Salary',
       bonus   AS 'Bonus',
       CONCAT(ROUND(bonus / salary * 100, 2), '%') AS 'Bonus Ratio'
FROM staff
WHERE bonus != 0
ORDER BY `Bonus Ratio` DESC;
```
</details>

---

# 4. Date Functions

## 4-1. Main Date Functions

| Function      | Meaning               |
| ------------- | --------------------- |
| NOW()         | Current date + time   |
| CURDATE()     | Current date          |
| DATE()        | Extract date part     |
| YEAR()        | Year                  |
| MONTH()       | Month                 |
| DAY()         | Day                   |
| HOUR()        | Hour                  |
| MINUTE()      | Minute                |
| SECOND()      | Second                |
| DATEDIFF()    | Date difference       |
| ADDDATE()     | Add days              |
| SUBDATE()     | Subtract days         |
| LAST_DAY()    | Last day of month     |
| DATE_FORMAT() | Date → formatted text |

---

## 4-2. Practice Problems

### Problem 1:

Display today's date in YY.MM.DD format.

<details markdown="1"> 
<summary>Answer</summary>

```sql
SELECT DATE_FORMAT(CURDATE(), '%y.%m.%d') AS 'Today';
```
</details>

### Problem 2:

List employees hired in the 2010s (2010–2019), sorted by hire date.

<details markdown="1"> 
<summary>Answer</summary>

```sql
SELECT name_ko AS 'Name',
       position AS 'Position',
       DATE_FORMAT(hired_at, '%m/%d/%y') AS 'Hire Date'
FROM staff
WHERE hired_at >= '2010-01-01'
  AND hired_at < '2020-01-01'
ORDER BY hired_at;
```
</details>

### Problem 3:

Compute years of service:
| years = current year − hire year + 1

<details markdown="1"> 
<summary>Answer</summary>

```sql
SELECT name_ko AS 'Name',
       YEAR(CURDATE()) - YEAR(hired_at) + 1 AS 'Years of Service'
FROM staff
ORDER BY 'Years of Service' DESC;
```
</details>

### Problem 4:

Employees whose working days (today − hired_at) are between 2500 and 7500.

<details markdown="1"> 
<summary>Answer</summary>

```sql
SELECT name_ko AS 'Name',
       DATEDIFF(CURDATE(), hired_at) AS 'Days Worked'
FROM staff
WHERE DATEDIFF(CURDATE(), hired_at) BETWEEN 2500 AND 7500
ORDER BY `Days Worked` DESC;
```
</details>

### Problem 5:

Count employees grouped by the day of week of hire date.

<details markdown="1"> 
<summary>Answer</summary>

```sql
SELECT DAYOFWEEK(hired_at) AS 'Day of Week',
       COUNT(*)            AS 'Employees'
FROM staff
GROUP BY 1
ORDER BY 1;
```
</details>

---

# 5. Conversion Functions

## 5-1. Main Conversion Functions

| Function      | Meaning              | Example                               |
| ------------- | -------------------- | ------------------------------------- |
| CAST()        | Type conversion      | CAST(100 AS CHAR)                     |
| FORMAT()      | Number formatting    | FORMAT(9999.9, 1)                     |
| DATE_FORMAT() | Date → string        | DATE_FORMAT(NOW(), '%Y%m%d')          |
| STR_TO_DATE() | String → date        | STR_TO_DATE('20230301','%Y%m%d')      |
| CONVERT_TZ()  | Time zone conversion | CONVERT_TZ(NOW(), '+00:00', '+09:00') |

---

## 5-2. Practice Problems

### Problem 1:

Calculate total pay (salary + bonus) in 만원 and sort by total pay.

<details markdown="1"> 
<summary>Answer</summary>

```sql
SELECT name_ko AS 'Name',
       CONCAT(FORMAT(salary + bonus, 0), '만원') AS 'Total Pay'
FROM staff
WHERE is_active = 1
ORDER BY salary + bonus DESC;
```
</details>

### Problem 2:

Convert UTC time to Korea Standard Time (KST, +09:00).

<details markdown="1"> 
<summary>Answer</summary>

```sql
SELECT NOW() AS 'utc_time',
       CONVERT_TZ(NOW(), '+00:00', '+09:00') AS 'kst_time';
```
</details>

---

# 6. NULL Functions

## 6-1. Main NULL-Handling Functions

| Function   | Meaning                     | Example                    |
| ---------- | --------------------------- | -------------------------- |
| IFNULL()   | Replace NULL with value     | IFNULL(bonus, 0)           |
| COALESCE() | Return first non-NULL value | COALESCE(bonus, salary, 0) |

---

## 6-2. Practice Problem

### Problem:

If a manager_id is NULL, output the employee's own staff_id instead.

<details markdown="1"> 
<summary>Answer</summary>

```sql
SELECT staff_id AS 'Staff ID',
       IFNULL(manager_id, staff_id) AS 'Manager ID'
FROM staff;
```
</details>
