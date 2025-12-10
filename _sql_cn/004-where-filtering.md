---
layout: default
title: "SQL Study 004 – Filtering Data with WHERE (CN)"
date: 2025-12-10
order: 4
---

# SQL Study 004 – Filtering Data with WHERE (CN)

本章节讲解如何使用 WHERE 子句过滤数据，  
以及在 `staff` 表中应用各种查询条件的方法。

---

## 1. WHERE 子句的概念

### 1-1. 定义
- WHERE 用于指定**查询结果中要保留的行的条件**。
- 也就是说，在所有数据中，**只筛选出满足条件的记录**。

---

## 2. 基本语法结构

```sql
SELECT 列名
FROM 表名
WHERE 条件;
```

示例：
```sql
SELECT name_ko, position
FROM staff
WHERE team_id = 11;
```

---

## 3. WHERE 中常用的运算符

### 3-1. 算术运算符

| 运算符 | 含义 | 示例     |
| --- | -- | ------ |
| +   | 加法 | 10 + 3 |
| -   | 减法 | 10 - 3 |
| *   | 乘法 | 10 * 3 |
| /   | 除法 | 10 / 3 |
| %   | 取余 | 10 % 3 |


### 3-2. 比较运算符

| 运算符     | 含义   | 示例             |
| ------- | ---- | -------------- |
| =       | 等于   | salary = 3000  |
| != , <> | 不等于  | team_id != 10  |
| >       | 大于   | salary > 3000  |
| <       | 小于   | salary < 3000  |
| >=      | 大于等于 | salary >= 3000 |
| <=      | 小于等于 | salary <= 3000 |

---

## 4. WHERE + AND / OR（复合条件）

### 4-1. AND：所有条件都必须满足
```sql
SELECT *
FROM staff
WHERE team_id = 11
  AND salary >= 7000;
```
→ 查询团队编号为 11 且薪资不少于 7000 的员工。


### 4-2. OR：任一条件满足即可

```sql
SELECT *
FROM staff
WHERE team_id = 11
   OR team_id = 12;
```
→ 查询 team_id 为 11 或 12 的员工。

---

## 5. WHERE + BETWEEN（范围条件）

```sql
SELECT name_ko, salary
FROM staff
WHERE salary BETWEEN 5000 AND 8000;
```
→ 查询 薪资在 5000 到 8000（含边界）之间 的员工。


### 5-1. DATETIME / TIMESTAMP 注意事项
当写成：
```sql
SELECT name_ko, hired_at
FROM staff
WHERE hired_at BETWEEN '2018-01-01' AND '2020-12-31';
```

实际上相当于：
起始：2023-01-01 00:00:00
截止：2023-12-31 00:00:00

因此：
✅ 2023-12-31 00:00:00 → 包含
❌ 2023-12-31 13:00:00 → 不包含
❌ 2023-12-31 23:59:59 → 不包含

---

## 6. WHERE + IN（列表条件）

```sql
SELECT *
FROM staff
WHERE team_id IN (10, 11, 12);
```
→ 查询 team_id 为 10、11 或 12 的员工。

与多次 OR 写法相比：
```sql
WHERE team_id = 10
   OR team_id = 11
   OR team_id = 12;
```
IN 语句更加简洁、易读。

---

## 7. WHERE + LIKE（字符串匹配）

| 模式  | 含义         |
| --- | ---------- |
| %A% | 包含 A       |
| A%  | 以 A 开头     |
| %A  | 以 A 结尾     |
| _A  | 第二个字符是 A   |
| A_  | 以 A 开头的两字符 |

示例：

```sql
SELECT *
FROM staff
WHERE name_ko LIKE '윤%';
```
→ 查询 韩文姓名以“윤”开头 的员工。

---

## 8. WHERE + IS NULL / IS NOT NULL

### 8-1. 语法
| 表达式         | 含义      |
| ----------- | ------- |
| IS NULL     | 值为空（无值） |
| IS NOT NULL | 值不为空    |


示例：查询有奖金的员工
```sql
SELECT *
FROM staff
WHERE bonus IS NOT NULL;
```

查询没有奖金的员工：
```sql
SELECT *
FROM staff
WHERE bonus IS NULL;
```

### 8-2. NULL 的含义

NULL 表示 “没有值 / 未知 / 尚未填写”。
与 0 或空字符串 '' 不同。
因此比较时必须使用 IS NULL，不能用 = NULL。

---

## 9. 练习题
### 练习 1：

查询 staff 表中职级（position）为 'Deputy' 的员工信息。

<details markdown="1"> 
<summary>答案</summary>

```sql
SELECT *
FROM staff
WHERE position = 'Deputy';
```
</details>

### 练习 2：

查询 staff 表中团队编号（team_id）不等于 11 的员工信息。

<details markdown="1">
<summary>答案</summary>

```sql  
SELECT *
FROM staff
WHERE team_id != 11;
```

或者

```sql
SELECT *
FROM staff
WHERE team_id <> 11;
```
</details>

### 练习 3:

查询 staff 表中，团队编号为 11，
且职级（position）为 'Lead' 或 'Senior' 的员工信息。

<details markdown="1">
<summary>答案</summary>

```sql  
SELECT *
FROM staff
WHERE team_id = 11
  AND position IN ('Lead', 'Senior');
```

或者

```sql
SELECT *
FROM staff
WHERE team_id = 11
  AND (position = 'Lead' OR position = 'Senior');
```
</details>

### 练习 4:

查询 staff 表中奖金（bonus）字段为空的员工信息。

<details markdown="1"> 
<summary>答案</summary>

```sql
SELECT *
FROM staff
WHERE bonus IS NULL;
```
</details>

### 练习 5:

查询 staff 表中，韩文姓名第二个字符为“운” 的员工信息。
（例如：김운항）

<details markdown="1"> 
<summary>答案</summary>

```sql  
SELECT *
FROM staff
WHERE name_ko LIKE '_운%';
```
</details> 
