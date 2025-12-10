---
layout: default
title: "SQL Study 002 – DB & Table Setup (EN)"
date: 2025-12-09
order: 2
---

# SQL Study 001 — DB & Table Setup (EN)

## 1. Create Database
```sql
-- 1-1. Drop the database if it already exists
--      (reset so we can recreate it with the same name)
DROP DATABASE IF EXISTS learn_sql;

-- 1-2. Create a new database named learn_sql
CREATE DATABASE learn_sql
  DEFAULT CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;

-- 1-3. Use learn_sql as the default database for all queries
USE learn_sql;
```

## 2. Create staff Table
```sql
-- 2-1. Drop staff table if it already exists
DROP TABLE IF EXISTS staff;

-- 2-2. Create staff table to store employee information
CREATE TABLE staff (
  staff_id     INT PRIMARY KEY,   -- employee id
  name_ko      VARCHAR(50),       -- local name (Korean)
  name_en      VARCHAR(100),      -- global/English name
  position     VARCHAR(50),       -- job title / position
  manager_id   INT,               -- direct manager id
  hired_at     DATE,              -- hire date
  salary       INT,               -- base salary
  bonus        INT,               -- bonus / incentive
  team_id      INT,               -- team id
  is_active    BOOLEAN            -- employment status (TRUE: active, FALSE: left)
);
```

## 3. Create team Table
```sql
-- 3-1. Drop team table if it already exists
--      (avoid errors and reset data when we re-run the script)
DROP TABLE IF EXISTS team;

-- 3-2. Create team table to store department information
CREATE TABLE team (
  team_id    INT PRIMARY KEY,   -- team id
  team_name  VARCHAR(100),      -- team name
  office     VARCHAR(100)       -- office location
);
```

## 4. Insert Data into staff
```sql
-- 4-1. Remove any existing rows in staff (reset)
DELETE FROM staff;

-- 4-2. Insert new employee records
INSERT INTO staff
(staff_id, name_ko, name_en, position, manager_id, hired_at, salary, bonus, team_id, is_active)
VALUES
(1000, '윤사령',  'Yoon Director',      'CEO',        NULL,  '1996-01-01', 82000, 0,     NULL, TRUE),
(7001, '백항해',  'Baek Executive',     'Executive',  1000,  '1998-07-01', 23000, 9000,  10,   TRUE),
(7002, '김운항',  'Kim Captain',        'Manager',    7001,  '2000-03-15', 16000, 3000,  11,   TRUE),
(4001, '정민호',  'Jung Manager',       'Manager',    1000,  '2003-08-19', 13500, 4000,  80,   TRUE),
(7003, '윤세진',  'Yoon Senior',        'Manager',    7001,  '2006-05-21', 12500, 6000,  12,   TRUE),
(7004, '한지우',  'Han Deputy',         'Deputy',     7003,  '2017-11-10', 10200, 2500,  12,   TRUE),
(7005, '고은채',  'Ko Manager',         'Lead',       7002,  '2000-03-15',  8100, 1800,  11,   FALSE),
(7006, '송도현',  'Song Manager',       'Lead',       7002,  '2015-04-03',  7200, 1500,  11,   TRUE),
(7007, '임하늘',  'Lim Assistant',      'Senior',     7002,  '2019-09-11',  6100,  0,    11,   TRUE),
(7008, '조민재',  'Cho Assistant',      'Senior',     7003,  '2020-06-08',  5600,  0,    12,   TRUE),
(4002, '백다은',  'Baek Assistant',     'Senior',     4001,  '2021-07-08',  5050,  0,    80,   TRUE),
(7009, '오지훈',  'Oh Staff',           'Junior',     7002,  '2022-01-03',  4850,  900,  11,   TRUE),
(7010, '류서연',  'Ryu Staff',          'Junior',     7003,  '2022-03-02',  4520,  900,  12,   TRUE),
(8001, '문건우',  'Moon FieldLeader',   'FieldLead',  NULL,  '2015-04-03',  6050, 1900,  40,   TRUE);
```

## 5. Insert Data into team
```sql
-- 5-1. Remove existing rows in team (reset)
DELETE FROM team;

-- 5-2. Insert new team records
INSERT INTO team (team_id, team_name, office) VALUES
  (10, 'Business HQ',      'Seoul'),
  (11, 'Domestic Sales 1', 'Seoul'),
  (12, 'Domestic Sales 2', 'Seoul'),
  (40, 'Production Center','Asan'),
  (80, 'HR Operations',    'Seoul');
```

## 6. Test Queries
```sql
-- 6-1. Check staff data
SELECT * FROM learn_sql.staff;

-- 6-2. Check team data
SELECT * FROM learn_sql.team;
```
