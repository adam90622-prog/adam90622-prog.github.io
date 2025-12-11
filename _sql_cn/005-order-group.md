---
layout: default
title: "SQL Study 005 – ORDER BY, LIMIT, GROUP BY, HAVING (CN)"
date: 2025-12-10
order: 5
---

# SQL Study 005 – ORDER BY, LIMIT, GROUP BY, HAVING (CN)

本章节介绍如何：

- 使用 **ORDER BY** 对查询结果排序
- 使用 **LIMIT** 限制返回行数
- 使用 **GROUP BY** 对数据分组
- 使用 **HAVING** 对分组结果设置条件

示例均基于 `staff` 表。

---

## 1. ORDER BY 的概念

- ORDER BY 用于**对查询结果进行排序**。
- 可以按数字、字符串、日期进行 **升序(ASC)** 或 **降序(DESC)** 排序。
- 它只会改变**结果的显示顺序**，不会修改表中实际存储的数据。

---

## 2. ORDER BY 基本语法

```sql
SELECT 列名
FROM 表名
ORDER BY 列名 [ASC | DESC];
```
ASC：升序（默认，可省略）
DESC：降序

### 2-1. 在 ORDER BY 中使用别名

```sql
SELECT salary * 12 AS annual_salary
FROM staff
ORDER BY annual_salary DESC;
```

在 SELECT 中定义的别名（annual_salary）可以在 ORDER BY 中使用。
但在 WHERE 中 不能 使用别名。

---

## 3. LIMIT 的概念

LIMIT 用于限制返回行数。
常用于“取前 N 条记录”或分页处理。

--- 

## 4. LIMIT 基本语法

```sql
SELECT 列名
FROM 表名
LIMIT 条数;
```

示例：

```sql
SELECT name_ko, salary
FROM staff
ORDER BY salary DESC
LIMIT 5;
```
→ 查询 薪资最高的前 5 名员工。

### 4-1. LIMIT + OFFSET（分页）

```sql
SELECT *
FROM staff
ORDER BY staff_id
LIMIT 5 OFFSET 5;
```
→ 按 staff_id 排序后，从第 6 行开始，取 5 行。

---

## 5. GROUP BY 的概念

GROUP BY 用于按某一列将多行记录分组。
通常与 COUNT、SUM、AVG、MAX、MIN 等聚合函数一起使用。

例如：“按团队统计人数”、“按职级统计平均薪资”等。

---

## 6. GROUP BY 基本语法

```sql
SELECT 分组列, 聚合函数(列)
FROM 表名
GROUP BY 分组列;
```

### 6-1. Aggregate Functions

| 函数      | 含义 | 示例用途 |
| ------- | -- | ---- |
| COUNT() | 个数 | 统计人数 |
| SUM()   | 合计 | 总薪资  |
| AVG()   | 平均 | 平均薪资 |
| MAX()   | 最大 | 最高薪资 |
| MIN()   | 最小 | 最低薪资 |

---

## 7. HAVING 的概念

HAVING 用于对 已经分组后的结果 进行筛选。
WHERE 是对单行记录进行过滤。
HAVING 是对分组后的聚合结果进行过滤，例如“只保留平均工资 ≥ 7000 的职级”。

---

## 8. HAVING 基本语法

```sql
SELECT 分组列, 聚合函数(列)
FROM 表名
GROUP BY 分组列
HAVING 分组条件;
```

## 9. 练习题

### 练习 1：
从 staff 表中查询薪资（salary）大于等于 5000 的员工，
按薪资从高到低排序，只取前 3 条记录。

<details markdown="1"> 
<summary>答案</summary>

```sql
SELECT *
FROM staff
WHERE salary >= 5000
ORDER BY salary DESC
LIMIT 3;
```
</details>

### 练习 2：

从 staff 表中查询薪资（salary）大于等于 5000 的员工，
按薪资从高到低排序，跳过前 3 条记录，再取 5 条。

<details markdown="1"> 
<summary>答案</summary>

```sql
SELECT *
FROM staff
WHERE salary >= 5000
ORDER BY salary DESC
LIMIT 5 OFFSET 3;
```
</details>

### 练习 3：

统计 staff 表中每个团队的员工人数。

示例结果：

| team_id | 人数 |
| ------: | -: |
|    NULL |  1 |
|      10 |  1 |
|      11 |  6 |
|      12 |  3 |
|      40 |  1 |
|      80 |  2 |


<details markdown="1"> 
<summary>答案</summary>

```sql
SELECT team_id, COUNT(*) AS '人数'
FROM staff
GROUP BY team_id;
```
</details>

### 练习 4：

查询 staff 表中，平均薪资不低于 7000 的职级(position)。

示例结果：

| 职级        |       平均薪资 |
| --------- | ---------: |
| CEO       | 82000.0000 |
| Executive | 23000.0000 |
| Manager   | 14000.0000 |
| Deputy    | 10200.0000 |
| Lead      |  7650.0000 |

<details markdown="1"> 
<summary>答案</summary>

```sql
SELECT position, AVG(salary) AS '平均薪资'
FROM staff
GROUP BY position
HAVING AVG(salary) >= 7000;
```
</details>

### 练习 5：

按团队统计 staff 表中最高薪资、最低薪资以及平均薪资。

示例结果：

| team_id |  最高薪资 |  最低薪资 |       平均薪资 |
| ------: | ----: | ----: | ---------: |
|    NULL | 82000 | 82000 | 82000.0000 |
|      10 | 23000 | 23000 | 23000.0000 |
|      11 | 16000 |  4850 |  8450.0000 |
|      12 | 12500 |  4520 |  8205.0000 |
|      40 |  6050 |  6050 |  6050.0000 |
|      80 | 13500 |  5050 |  9275.0000 |

<details markdown="1"> 
<summary>答案</summary>

```sql
SELECT  team_id AS 'team_id'
       ,MAX(salary) AS '最高薪资'
       ,MIN(salary) AS '最低薪资'
       ,AVG(salary) AS '平均薪资'
FROM staff
GROUP BY team_id;
```
</details> 
