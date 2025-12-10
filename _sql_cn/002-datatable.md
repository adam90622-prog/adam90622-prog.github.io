---
layout: default
title: "SQL Study 002 – DB & Table Setup (CN)"
date: 2025-12-09
order: 2
---

# SQL Study 002 — DB & Table Setup (ZH)

## 1. 创建数据库
```sql
-- 1-1. 如果已经存在 learn_sql 数据库，则先删除
--      （为了重新创建同名数据库，先做初始化）
DROP DATABASE IF EXISTS learn_sql;

-- 1-2. 创建名为 learn_sql 的新数据库
CREATE DATABASE learn_sql
  DEFAULT CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;

-- 1-3. 之后执行的所有 SQL 都以 learn_sql 数据库为默认
USE learn_sql;
```

## 2. 创建 staff 表（员工信息）
```sql
-- 2-1. 如果 staff 表已经存在，先删除
DROP TABLE IF EXISTS staff;

-- 2-2. 创建 staff 表，用于保存员工信息
CREATE TABLE staff (
  staff_id     INT PRIMARY KEY,   -- 员工编号
  name_ko      VARCHAR(50),       -- 本地姓名（韩文）
  name_en      VARCHAR(100),      -- 英文姓名
  position     VARCHAR(50),       -- 职位/职级
  manager_id   INT,               -- 直属上级编号
  hired_at     DATE,              -- 入职日期
  salary       INT,               -- 基本工资
  bonus        INT,               -- 奖金
  team_id      INT,               -- 所属团队编号
  is_active    BOOLEAN            -- 在职状态（TRUE: 在职，FALSE: 离职）
);
```

## 3. 创建 team 表（部门/团队信息）
```sql
-- 3-1. 如果 team 表已经存在，先删除
--      （防止重复执行脚本时报错，并清空旧数据）
DROP TABLE IF EXISTS team;

-- 3-2. 创建 team 表，用于保存部门/团队信息
CREATE TABLE team (
  team_id    INT PRIMARY KEY,   -- 团队编号
  team_name  VARCHAR(100),      -- 团队名称
  office     VARCHAR(100)       -- 办公地点
);
```

## 4. 向 staff 表插入数据
```sql
-- 4-1. 先清空 staff 表中的旧数据
DELETE FROM staff;

-- 4-2. 插入新的员工数据
INSERT INTO staff
(staff_id, name_ko, name_en, position, manager_id, hired_at, salary, bonus, team_id, is_active)
VALUES
(1000, '윤사령',  'Yoon Director',      '总经理',   NULL,  '1996-01-01', 82000, 0,     NULL, TRUE),
(7001, '백항해',  'Baek Executive',     '执行董事', 1000,  '1998-07-01', 23000, 9000,  10,   TRUE),
(7002, '김운항',  'Kim Captain',        '部门经理', 7001,  '2000-03-15', 16000, 3000,  11,   TRUE),
(4001, '정민호',  'Jung Manager',       '部门经理', 1000,  '2003-08-19', 13500, 4000,  80,   TRUE),
(7003, '윤세진',  'Yoon Senior',        '部门经理', 7001,  '2006-05-21', 12500, 6000,  12,   TRUE),
(7004, '한지우',  'Han Deputy',         '副经理',   7003,  '2017-11-10', 10200, 2500,  12,   TRUE),
(7005, '고은채',  'Ko Manager',         '科长',     7002,  '2000-03-15',  8100, 1800,  11,   FALSE),
(7006, '송도현',  'Song Manager',       '科长',     7002,  '2015-04-03',  7200, 1500,  11,   TRUE),
(7007, '임하늘',  'Lim Assistant',      '代理',     7002,  '2019-09-11',  6100,  0,    11,   TRUE),
(7008, '조민재',  'Cho Assistant',      '代理',     7003,  '2020-06-08',  5600,  0,    12,   TRUE),
(4002, '백다은',  'Baek Assistant',     '代理',     4001,  '2021-07-08',  5050,  0,    80,   TRUE),
(7009, '오지훈',  'Oh Staff',           '职员',     7002,  '2022-01-03',  4850,  900,  11,   TRUE),
(7010, '류서연',  'Ryu Staff',          '职员',     7003,  '2022-03-02',  4520,  900,  12,   TRUE),
(8001, '문건우',  'Moon FieldLeader',   '现场班长', NULL,  '2015-04-03',  6050, 1900,  40,   TRUE);
```

## 5. 向 team 表插入数据
```sql
-- 5-1. 清空 team 表中的旧数据
DELETE FROM team;

-- 5-2. 插入新的团队数据
INSERT INTO team (team_id, team_name, office) VALUES
  (10, '业务本部',      '首尔'),
  (11, '国内营业一组', '首尔'),
  (12, '国内营业二组', '首尔'),
  (40, '生产中心',      '牙山'),
  (80, '人事运营组',    '首尔');
```

## 6. 查询确认数据
```sql
-- 6-1. 查看 staff 表数据
SELECT * FROM learn_sql.staff;

-- 6-2. 查看 team 表数据
SELECT * FROM learn_sql.team;
```
