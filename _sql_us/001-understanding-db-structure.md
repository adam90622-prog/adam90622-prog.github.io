---
layout: default
title: "SQL Study 001 – Understanding Database Structure (EN)"
date: 2025-12-08
order: 1
---

# SQL Study 001 – Understanding Database Structure (EN)

This chapter explains how MySQL organizes and stores data, following the structure used in our SQL practice environment.

---

# 1. Instance → Database → Table

<img width="2000" height="1400" alt="3" src="https://github.com/user-attachments/assets/5619e191-3f99-44d8-95a2-374c2e9f7fab" />


## 1-1. Instance  
The MySQL **instance** is the database server program currently running and occupying memory.

---

## 1-2. Database (Schema)  
In MySQL, **Database = Schema** (same meaning).

Characteristics:

- Databases are **completely isolated**
- **JOIN between different DBs is impossible**
- Used for separating environments (prod/dev/test)

---

## 1-3. Table  
A table is where actual data is stored.

Table = Excel sheet  
- Rows = records  
- Columns = attributes  

---

## 1-4. Column  
Defines attributes of the data.

Example (staff table):

| Column      | Meaning |
|-------------|---------|
| staff_id    | Unique employee ID |
| name_ko     | Korean name |
| name_en     | English name |
| position    | Job title |

---

## 1-5. Row  
Represents 1 complete data entry.

Example:

staff_id name_ko position team_id is_active
7001 백항해 Executive 10 TRUE


---

# 2. ERD (Entity Relationship Diagram)

<!-- IMAGE_2_HERE -->

Describes table structure used in this SQL course.

---

## 2-1. staff Table Description

| No | Column     | Type         | Description |
|----|------------|--------------|-------------|
| 1  | staff_id   | INT (PK)     | Unique employee ID |
| 2  | name_ko    | VARCHAR(50)  | Korean name |
| 3  | name_en    | VARCHAR(100) | English name |
| 4  | position   | VARCHAR(50)  | Job title |
| 5  | manager_id | INT          | Direct manager (staff_id) |
| 6  | hired_at   | DATE         | Hire date |
| 7  | salary     | INT          | Base salary |
| 8  | bonus      | INT          | Incentive |
| 9  | team_id    | INT (FK)     | Foreign key to team table |
|10  | is_active  | BOOLEAN      | Employment status |

---

## 2-2. team Table Description

| No | Column     | Type         | Description |
|----|------------|--------------|-------------|
| 1  | team_id    | INT (PK)     | Unique team ID |
| 2  | team_name  | VARCHAR(100) | Team name |
| 3  | office     | VARCHAR(100) | Office location |

---
