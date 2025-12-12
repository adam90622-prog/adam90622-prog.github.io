---
title: "SQL 001 – Average Rental Duration of Cars"
date: 2025-12-10
language: sql
order: 2
---

# SQL Problem Explanation

## Places Owned by Heavy Users

The **PLACES** table contains information about spaces registered on a space-rental service.  
The table structure is:

| NAME | TYPE    |
|------|---------|
| ID   | INT     |
| NAME | VARCHAR |
| HOST_ID | INT  |

---

## Task

A user who has registered **two or more spaces** is considered a **heavy user**.  
Write an SQL query that retrieves all spaces registered by heavy users, ordered by `ID` in ascending order.

---

## Example

Given the following `PLACES` table:

| ID       | NAME                                                          | HOST_ID  |
|----------|---------------------------------------------------------------|----------|
| 4431977  | BOUTIQUE STAYS - Somerset Terrace, Pet Friendly              | 760849   |
| 5194998  | BOUTIQUE STAYS - Elwood Beaches 3, Pet Friendly             | 760849   |
| 16045624 | Urban Jungle in the Heart of Melbourne                       | 30900122 |
| 17810814 | Stylish Bayside Retreat with a Luscious Garden               | 760849   |
| 22740286 | FREE PARKING - The Velvet Lux in Melbourne CBD               | 30900122 |
| 22868779 | ★ Fresh Fitzroy Pad with City Views! ★                       | 21058208 |

- User **760849** → 3 spaces → heavy user  
- User **30900122** → 2 spaces → heavy user  
- User **21058208** → 1 space → not a heavy user  

Expected output:

| ID       | NAME                                                          | HOST_ID  |
|----------|---------------------------------------------------------------|----------|
| 4431977  | BOUTIQUE STAYS - Somerset Terrace, Pet Friendly              | 760849   |
| 5194998  | BOUTIQUE STAYS - Elwood Beaches 3, Pet Friendly             | 760849   |
| 16045624 | Urban Jungle in the Heart of Melbourne                       | 30900122 |
| 17810814 | Stylish Bayside Retreat with a Luscious Garden               | 760849   |
| 22740286 | FREE PARKING - The Velvet Lux in Melbourne CBD               | 30900122 |

---

## SQL Answer (Your Solution)

```sql
SELECT P1.ID, P1.NAME, P1.HOST_ID
FROM PLACES AS P1
WHERE P1.HOST_ID IN (
    SELECT HOST_ID
    FROM (
        SELECT HOST_ID, COUNT(*)
        FROM PLACES AS P2
        GROUP BY HOST_ID
        HAVING COUNT(*) >= 2
    ) AS a
);
```
