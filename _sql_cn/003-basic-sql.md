---
layout: default
title: "SQL Study 003 – Basic SQL (CN)"
date: 2025-12-10
order: 3
---

# SQL Study 003 – Basic SQL (CN)

本章节介绍最基础的 SELECT 查询语句  
以及数据库在读取数据时的基本处理流程。

---

## 1. SQL 的书写顺序与执行顺序

### 1-1. 书写顺序（人类书写方式）
SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY

### 1-2. 执行顺序（数据库内部处理方式）
FROM → ON → JOIN → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY

---

## 2. SELECT ~ FROM 的基本概念

### 2-1. 定义  
SELECT 是用来查询数据的最基本 SQL 语句。

### 2-2. 基本语法

```sql
-- 查询全部字段
SELECT * FROM staff;

-- 查询指定字段（带别名）
SELECT name_ko AS '姓名', position AS '职级'
FROM staff;
```

### 2-3. 关键要点

SELECT : 查询字段
FROM : 查询数据来源的表

* : 查询所有字段
AS : 查询结果中显示的临时别名

---

## 3. DISTINCT

DISTINCT 用于去除重复值，仅返回唯一结果。

```sql
SELECT DISTINCT position
FROM staff;
```

---

## 4. 练习题
### 练习 1:
查询 staff 表的所有数据。

<details> <summary>答案</summary>

```sql
SELECT * FROM staff;
```

</details>

### 练习 2:
查询编号、韩文姓名、职级，结果如下：

| 编号   | 姓名  | 职级        |
| ---- | --- | --------- |
| 1000 | 윤사령 | CEO       |
| 7001 | 백항해 | Executive |
| 7002 | 김운항 | Manager   |
| 4001 | 정민호 | Manager   |
| 7003 | 윤세진 | Manager   |
| 7004 | 한지우 | Deputy    |
| 7005 | 고은채 | Lead      |
| 7006 | 송도현 | Lead      |
| 7007 | 임하늘 | Senior    |
| 7008 | 조민재 | Senior    |
| 4002 | 백다은 | Senior    |
| 7009 | 오지훈 | Junior    |
| 7010 | 류서연 | Junior    |
| 8001 | 文建宇 | FieldLead |

<details> <summary>答案</summary>

```sql
SELECT  staff_id AS '编号'
       ,name_ko  AS '姓名'
       ,position AS '职级'
FROM staff;
```

</details>

### 练习 3:
查询 staff 表中的唯一职级列表。

<details> <summary>答案</summary>

```sql
SELECT DISTINCT position
FROM staff;
```

</details> 
