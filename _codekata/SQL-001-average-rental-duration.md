---
title: "SQL 001 – Average Rental Duration of Cars"
date: 2025-01-02
---

# SQL Problem Explanation

## **Average Rental Duration of Cars**

The **CAR_RENTAL_COMPANY_RENTAL_HISTORY** table contains rental history records for a car rental company.  
The table structure is as follows, where **HISTORY_ID**, **CAR_ID**, **START_DATE**, and **END_DATE** represent the rental history ID, car ID, rental start date, and rental end date respectively.

| Column name | Type    | Nullable |
|------------|---------|----------|
| HISTORY_ID | INTEGER | FALSE    |
| CAR_ID     | INTEGER | FALSE    |
| START_DATE | DATE    | FALSE    |
| END_DATE   | DATE    | FALSE    |

---

## Task

Write an SQL query to retrieve a list of car IDs and their average rental durations (column name: `AVERAGE_DURATION`)  
from the `CAR_RENTAL_COMPANY_RENTAL_HISTORY` table for cars whose average rental duration is **7 days or more**.

- Round the average rental duration to **one decimal place**.  
- Sort the results by `AVERAGE_DURATION` in **descending** order.  
- If the average rental duration is the same, sort by `CAR_ID` in **descending** order.

---

## Example

Given the following `CAR_RENTAL_COMPANY_RENTAL_HISTORY` table:

| HISTORY_ID | CAR_ID | START_DATE  | END_DATE    |
|-----------:|-------:|-------------|-------------|
| 1          | 1      | 2022-09-27  | 2022-10-01  |
| 2          | 1      | 2022-10-03  | 2022-11-04  |
| 3          | 2      | 2022-09-05  | 2022-09-05  |
| 4          | 2      | 2022-09-08  | 2022-09-10  |
| 5          | 3      | 2022-09-16  | 2022-10-15  |
| 6          | 1      | 2022-11-07  | 2022-12-06  |

The average rental duration for each car is calculated as follows:

- Car ID 1: rental durations of 5 days, 33 days, and 30 days → **average 22.7 days**  
- Car ID 2: rental durations of 1 day and 3 days → **average 2 days**  
- Car ID 3: rental duration of 30 days → **average 30 days**

Cars with an average rental duration of at least 7 days are **Car ID 1** and **Car ID 3**.  
Sorted by average rental duration (descending) and then by car ID (descending), the result should be:

| CAR_ID | AVERAGE_DURATION |
|-------:|------------------|
| 3      | 30.0             |
| 1      | 22.7             |

---

## SQL Answer (Your Solution)

```sql
SELECT CAR_ID,
       ROUND(AVG(DATEDIFF(END_DATE, START_DATE) + 1), 1) AS AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
HAVING ROUND(AVG(DATEDIFF(END_DATE, START_DATE) + 1), 1) >= 7
ORDER BY ROUND(AVG(DATEDIFF(END_DATE, START_DATE) + 1), 1) DESC,
         CAR_ID DESC;
```
