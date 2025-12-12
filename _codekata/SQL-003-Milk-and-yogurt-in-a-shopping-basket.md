---
title: "SQL 001 – Average Rental Duration of Cars"
date: 2025-12-09
language: sql
order: 3
---

# SQL Problem Explanation

## Carts with Both Milk and Yogurt

The **CART_PRODUCTS** table contains information about products placed in shopping carts.  
The table structure is:

| NAME    | TYPE    |
|--------|---------|
| ID     | INT     |
| CART_ID| INT     |
| NAME   | VARCHAR |
| PRICE  | INT     |

---

## Task

The data analysis team wants to find out whether there are any shopping carts that purchased **both Milk and Yogurt**.

Write an SQL query that retrieves the **IDs of carts that contain both `Milk` and `Yogurt`**.  
The result must be returned in **ascending order of `CART_ID`**.

---

## Example

Given the following `CART_PRODUCTS` table:

| ID    | CART_ID | NAME                  | PRICE |
|-------|---------|-----------------------|-------|
| 1630  | 83      | Cereal                | 3980  |
| 1631  | 83      | Multipurpose Supply   | 3900  |
| 5491  | 286     | Yogurt                | 2980  |
| 5504  | 286     | Milk                  | 1880  |
| 8435  | 448     | Milk                  | 1880  |
| 8437  | 448     | Yogurt                | 2980  |
| 8438  | 448     | Tea                   | 11000 |
| 20236 | 1034    | Yogurt                | 2980  |
| 20237 | 1034    | Butter                | 4890  |

- Cart **83** → does **not** contain Milk or Yogurt.
- Cart **286** → contains **both** Milk and Yogurt.
- Cart **448** → contains **both** Milk and Yogurt.
- Cart **1034** → contains only Yogurt, not Milk.

Expected output:

| CART_ID |
|---------|
| 286     |
| 448     |

---

## SQL Answer 
### Answer 1:

<details markdown="1"> 
<summary>Answer</summary>

```sql
SELECT CART_ID
FROM CART_PRODUCTS
WHERE NAME IN ('Milk', 'Yogurt')
GROUP BY CART_ID
HAVING COUNT(DISTINCT NAME) = 2
ORDER BY CART_ID;
```
</details>

### Answer 2:

<details markdown="1"> 
<summary>Answer</summary>

```sql
SELECT CART_ID
FROM CART_PRODUCTS
GROUP BY CART_ID
HAVING MAX(NAME = 'Milk') AND MAX(NAME = 'Yogurt')
ORDER BY CART_ID;
```
</details>

### Answer 3:

<details markdown="1"> 
<summary>Answer</summary>

```sql
SELECT DISTINCT a.CART_ID
FROM CART_PRODUCTS a
JOIN CART_PRODUCTS b
  ON a.CART_ID = b.CART_ID
WHERE a.NAME = 'Milk' AND b.NAME = 'Yogurt'
ORDER BY a.CART_ID;
```
</details>

---

## My Answer
<details markdown="1"> 
<summary>Answer</summary>

```sql
-- Create separate indicator columns for Milk and Yogurt
SELECT CART_ID
FROM (
    SELECT *,
           CASE WHEN NAME = 'Yogurt' THEN 1 ELSE 0 END AS have_yogurt,
           CASE WHEN NAME = 'Milk'  THEN 1 ELSE 0 END AS have_milk
    FROM CART_PRODUCTS
) AS a
GROUP BY CART_ID
HAVING SUM(have_yogurt) >= 1
   AND SUM(have_milk)  >= 1;
```
</details>
