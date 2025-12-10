---
layout: default
title: "SQL Study 001 – 数据库结构理解 (CN)"
date: 2025-12-8
order: 1
---

# SQL Study 001 – 数据库结构理解 (CN)

本章节介绍 MySQL 如何组织与存储数据。  
内容基于我们即将使用的 SQL 实训环境。

---

# 1. 实例 → 数据库 → 表

<img width="2000" height="1400" alt="이미지 크기 A안  B안  C안 폰트 스타일 Sans-serif  Bold Sans-serif  Monospace 혹시 전체 배경도 흰색 유지 아니면 아주 은은한 연한 회색(#f5f5f5)" src="https://github.com/user-attachments/assets/6b3c3f4d-0d06-4e5f-bd4d-58ba787241f8" />



## 1-1. 实例(Instance)

实例指 **当前正在运行的 MySQL 服务器程序**。  
即占用内存、正在工作的数据库引擎。


---

## 1-2. 数据库(Database, Schema)

在 MySQL 中：  
**Database = Schema（完全相同的概念）**

特点：

- 数据库之间 **完全隔离**
- 不同数据库之间 **不能 JOIN**
- 常用于区分生产/开发/测试环境

---

## 1-3. 表(Table)

实际数据存放的结构。

表 = Excel 工作表  
- 行(Row) = 一条数据  
- 列(Column) = 属性

---

## 1-4. 列(Column)

定义数据的属性。

示例（staff 表）：

| 列名        | 含义 |
|-------------|------|
| staff_id    | 员工唯一编号 |
| name_ko     | 韩文姓名 |
| name_en     | 英文姓名 |
| position    | 职位/职称 |

---

## 1-5. 行(Row)

表示一个完整的数据记录。

示例：

staff_id name_ko position team_id is_active
7001 白航海 Executive 10 TRUE


---

# 2. ERD（实体关系图）

<img width="2000" height="1400" alt="Staff (2)" src="https://github.com/user-attachments/assets/e979c654-4177-440e-85d3-13b55fadcc5a" />


此结构用于本 SQL 实训课程。

---

## 2-1. staff 表说明

| 序号 | 列名        | 类型           | 说明 |
|------|--------------|----------------|------|
| 1  | staff_id   | INT (PK)     | 员工唯一编号 |
| 2  | name_ko    | VARCHAR(50)  | 韩文姓名 |
| 3  | name_en    | VARCHAR(100) | 英文姓名 |
| 4  | position   | VARCHAR(50)  | 职位 |
| 5  | manager_id | INT          | 直属上级（staff_id） |
| 6  | hired_at   | DATE         | 入职日期 |
| 7  | salary     | INT          | 基本工资 |
| 8  | bonus      | INT          | 奖金/激励 |
| 9  | team_id    | INT (FK)     | 外键，对应 team 表 |
|10 | is_active  | BOOLEAN      | 在职状态 |

---

## 2-2. team 表说明

| 序号 | 列名        | 类型           | 说明 |
|------|--------------|----------------|------|
| 1 | team_id     | INT (PK)     | 团队唯一编号 |
| 2 | team_name   | VARCHAR(100) | 团队名称 |
| 3 | office      | VARCHAR(100) | 办公地点 |

---
