---
layout: default
title: "SQL Study 006 – 内置函数 (CN)"
date: 2025-12-10
order: 6
---

# SQL Study 006 – 内置函数 (CN)

本章以 `staff` 表为基础，系统整理 SQL 中最常用的 **内置函数**，  
并通过练习题学习其使用方法。

使用表：**staff**

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

# 1. 什么是内置函数？

函数接收输入、执行运算并返回结果。
SQL 函数主要分为两类：

## 1-1. 单行函数（Single-Row Function）
- 字符串函数
- 数值函数
- 日期函数
- 转换函数
- NULL 处理函数

## 1-2. 多行函数（Multi-Row Function）
- 聚合函数（SUM, AVG 等）
- 分组函数
- 窗口函数
→ 输入多行数据，返回 汇总结果。

---

# 2. 字符串函数

## 2-1. 常用字符串函数

| 函数            | 含义              | 示例                              |
| ------------- | --------------- | ------------------------------- |
| UPPER()       | 转为大写            | `UPPER(name_en)`                |
| LOWER()       | 转为小写            | `LOWER(name_en)`                |
| LENGTH()      | 字节长度            | `LENGTH(name_ko)`               |
| CHAR_LENGTH() | 字符长度（支持韩文）      | `CHAR_LENGTH(name_ko)`          |
| LEFT()        | 从左截取 N 字符       | `LEFT('BIGDATA', 3)`            |
| RIGHT()       | 从右截取 N 字符       | `RIGHT('BIGDATA', 4)`           |
| SUBSTRING()   | 截取部分字符串         | `SUBSTRING(name_ko, 2, 2)`      |
| REPLACE()     | 字符串替换           | `REPLACE(position, '经理', '理事')` |
| LTRIM()       | 去除左侧字符/空格       | `LTRIM(' ABC', ' ')`            |
| RTRIM()       | 去除右侧字符/空格       | `RTRIM('ABC ', ' ')`            |
| TRIM()        | 去除两侧空格          | `TRIM(name_en)`                 |
| CONCAT()      | 字符串拼接           | `CONCAT(name_ko, '님')`          |
| LPAD()        | 左侧填充字符至指定长度     | `LPAD(name_ko, 5, '*')`         |
| RPAD()        | 右侧填充字符至指定长度     | `RPAD(name_ko, 5, '*')`         |
| POSITION()    | 查找子串位置（不存在返回 0） | `POSITION('D' IN 'BIGDATA')`    |

→ 统计韩文的字符长度请使用 CHAR_LENGTH()。

---

## 2-2. 练习题

### 题目 1:  
将员工姓名以下列格式输出：
| 示例：윤사령 [대표이사]

<details markdown="1">
<summary>答案</summary>

```sql
SELECT CONCAT(name_ko, ' [', position, ']') AS '姓名 [职级]'
FROM staff;
```
</details>

### 题目 2:
按姓名字符长度统计员工人数。（韩文需用 CHAR_LENGTH）

<details markdown="1"> 
<summary>答案</summary>

```sql
SELECT CHAR_LENGTH(name_ko) AS '姓名长度',
       COUNT(*)             AS '人数'
FROM staff
GROUP BY 姓名长度;
```
</details>

### 题目 3:

查询 姓名最后一个字为“현” 的员工，
并将英文名转换为大写输出。

示例：
| 姓名  | 英文名         |
| --- | ----------- |
| 송도현 | SONG DOHYUN |

<details markdown="1"> 
<summary>答案</summary>

```sql
SELECT name_ko        AS '姓名',
       UPPER(name_en) AS '英文名'
FROM staff
WHERE RIGHT(name_ko, 1) = '현';
```
</details>

### 题目 4:

对于姓名为 “김운항” 的员工，
若其当前职级为“부장”，需将其晋升后的职级显示为“상무”。

<details markdown="1"> 
<summary>答案</summary>

```sql
SELECT name_ko                           AS '姓名',
       position                          AS '当前职级',
       REPLACE(position, '부장', '상무') AS '晋升职级'
FROM staff
WHERE name_ko = '김운항';
```
</details>

### 题目 5:

员工姓名需要匿名处理（仅保留姓氏，后面全用 ** 表示）。

<details markdown="1"> 
<summary>答案</summary>

```sql
SELECT position                       AS '职级',
       CONCAT(LEFT(name_ko, 1), '**') AS '姓名',
       salary                         AS '年薪',
       bonus                          AS '奖金'
FROM staff;
```
</details>

---

# 3. 数值函数

## 3-1. 常用数值函数

| 函数             | 含义               | 示例                   |
| -------------- | ---------------- | -------------------- |
| TRUNCATE(x, n) | 保留 n 位小数并 **截断** | TRUNCATE(3.14159, 2) |
| ROUND(x, n)    | 四舍五入             | ROUND(3.14159, 2)    |
| MOD(a, b)      | 取余数              | MOD(10, 3)           |
| CEIL(x)        | 向上取整             | CEIL(3.2)            |
| FLOOR(x)       | 向下取整             | FLOOR(3.8)           |
| ABS(x)         | 绝对值              | ABS(-10)             |
| SIGN(x)        | 符号（-1, 0, 1）     | SIGN(-5)             |
| POWER(a, b)    | a 的 b 次方         | POWER(2, 3)          |
| SQRT(x)        | 平方根              | SQRT(16)             |


---

## 3-2. 练习题

### 题目 1:

- 查询年薪 ≥ 6000 的员工，并输出：
- 姓名[职级]
- 年薪
- 月薪（年薪 ÷ 12，截断 0 位小数）
- 按月薪降序排序

<details markdown="1"> 
<summary>答案</summary>
  
```sql
SELECT CONCAT(name_ko, ' [', position, ']') AS '姓名[职级]',
       salary                               AS '年薪',
       TRUNCATE(salary / 12, 0)             AS '月薪'
FROM staff
WHERE salary >= 6000
ORDER BY 月薪 DESC;
```
</details>

### 题目 2:

计算奖金比例：
| 奖金比例(%) = bonus / salary × 100

要求：
- bonus ≠ 0
- 四舍五入保留 2 位
- 显示为字符串 “33.33%”
- 按奖金比例降序

<details markdown="1"> 
<summary>答案</summary>

```sql
SELECT name_ko AS '姓名',
       salary  AS '年薪',
       bonus   AS '奖金',
       CONCAT(ROUND(bonus / salary * 100, 2), '%') AS '奖金比例'
FROM staff
WHERE bonus != 0
ORDER BY 奖金比例 DESC;
```
</details>

---

# 4. 日期函数

## 4-1. 常用日期函数

| 函数            | 含义      |
| ------------- | ------- |
| NOW()         | 当前日期+时间 |
| CURDATE()     | 当前日期    |
| DATE()        | 提取日期部分  |
| YEAR()        | 年       |
| MONTH()       | 月       |
| DAY()         | 日       |
| HOUR()        | 时       |
| MINUTE()      | 分       |
| SECOND()      | 秒       |
| DATEDIFF()    | 日期差     |
| ADDDATE()     | 日期增加    |
| SUBDATE()     | 日期减少    |
| LAST_DAY()    | 当月最后一天  |
| DATE_FORMAT() | 日期格式化   |

---

## 4-2. 练习题

### 题目 1:

以 YY.MM.DD 格式显示今天的日期。

<details markdown="1"> 
<summary>答案</summary>

```sql
SELECT DATE_FORMAT(CURDATE(), '%y.%m.%d') AS 'Today';
```
</details>

### 题目 2:

查询 2010–2019 年入职的员工，按入职日期升序。

<details markdown="1"> 
<summary>答案</summary>

```sql
SELECT name_ko AS '姓名',
       position AS '职级',
       DATE_FORMAT(hired_at, '%m/%d/%y') AS '入职日'
FROM staff
WHERE hired_at >= '2010-01-01'
  AND hired_at < '2020-01-01'
ORDER BY hired_at;
```
</details>

### 题目 3:

根据入职日期计算 工龄：
| 工龄 = 当前年份 − 入职年份 + 1

<details markdown="1"> 
<summary>答案</summary>

```sql
SELECT name_ko AS '姓名',
       YEAR(CURDATE()) - YEAR(hired_at) + 1 AS '工龄'
FROM staff
ORDER BY 工龄 DESC;
```
</details>

### 题目 4:

查询 工作天数（今天 − 入职日）在 2500〜7500 之间的员工。

<details markdown="1"> 
<summary>答案</summary>

```sql
SELECT name_ko AS '姓名',
       DATEDIFF(CURDATE(), hired_at) AS '工作天数'
FROM staff
WHERE DATEDIFF(CURDATE(), hired_at) BETWEEN 2500 AND 7500
ORDER BY 工作天数 DESC;
```
</details>

### 题目 5:

按入职星期几统计员工人数。

<details markdown="1"> 
<summary>答案</summary>

```sql
SELECT DAYOFWEEK(hired_at) AS '星期',
       COUNT(*)            AS '人数'
FROM staff
GROUP BY 1
ORDER BY 1;
```
</details>

---

# 5. 转换函数

## 5-1. 常用转换函数

| 函数            | 含义          | 示例                                    |
| ------------- | ----------- | ------------------------------------- |
| CAST()        | 类型转换        | CAST(100 AS CHAR)                     |
| FORMAT()      | 数字格式（含千位逗号） | FORMAT(9999.9,1)                      |
| DATE_FORMAT() | 日期 → 字符串    | DATE_FORMAT(NOW(),'%Y%m%d')           |
| STR_TO_DATE() | 字符串 → 日期    | STR_TO_DATE('20230301','%Y%m%d')      |
| CONVERT_TZ()  | 时区转换        | CONVERT_TZ(NOW(), '+00:00', '+09:00') |

---

## 5-2. 练习题

### 题目 1:

计算总薪资（salary + bonus），单位为 “万元”，并按总薪资降序。

<details markdown="1"> 
<summary>答案</summary>

```sql
SELECT name_ko AS '姓名',
       CONCAT(FORMAT(salary + bonus, 0), '万元') AS '总薪资'
FROM staff
WHERE is_active = 1
ORDER BY salary + bonus DESC;
```
</details>

### 题目 2:

将 UTC 时间转换为韩国标准时间（KST，+09:00）。

<details markdown="1"> 
<summary>答案</summary>

```sql
SELECT NOW() AS 'utc_time',
       CONVERT_TZ(NOW(), '+00:00', '+09:00') AS 'kst_time';
```
</details>

---

# 6. NULL 处理函数

## 6-1. 常用 NULL 函数

| 函数         | 含义             | 示例                         |
| ---------- | -------------- | -------------------------- |
| IFNULL()   | NULL → 指定值     | IFNULL(bonus, 0)           |
| COALESCE() | 返回第一个非 NULL 的值 | COALESCE(bonus, salary, 0) |

---

## 6-2. 练习题

### 题目:

若 manager_id 为 NULL，则输出员工自己的 staff_id。

<details markdown="1"> 
<summary>答案</summary>

```sql
SELECT staff_id AS '员工编号',
       IFNULL(manager_id, staff_id) AS '经理编号'
FROM staff;
```
</details>
