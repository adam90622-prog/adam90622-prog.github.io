---
layout: default
title: "SQL Study 004 – Filtering Data with WHERE (KR)"
date: 2025-12-10
order: 4
---

# SQL Study 004 – Filtering Data with WHERE (KR)

이 장에서는 WHERE 절을 사용하여  
데이터를 필터링(조건 조회)하는 방법을 정리합니다.

---

## 1. WHERE 절의 개념

### 1-1. 정의
- WHERE는 **조회할 데이터의 조건(Filter)** 을 지정하는 절입니다.
- 전체 데이터 중에서 **필요한 행만 골라서 조회**할 때 사용하는 필수 구문입니다.

---

## 2. 기본 문법 구조

```sql
SELECT 컬럼명
FROM 테이블명
WHERE 조건식;
```

예시:
```sql
SELECT name_ko, position
FROM staff
WHERE team_id = 11;
```

---

## 3. WHERE에서 자주 사용하는 연산자

### 3-1. 산술 연산자

| 연산자 | 의미  | 예시     |
| --- | --- | ------ |
| +   | 더하기 | 10 + 3 |
| -   | 빼기  | 10 - 3 |
| *   | 곱하기 | 10 * 3 |
| /   | 나누기 | 10 / 3 |
| %   | 나머지 | 10 % 3 |


### 3-2. 비교 연산자

| 연산자     | 의미    | 예시             |
| ------- | ----- | -------------- |
| =       | 같다    | salary = 3000  |
| != , <> | 같지 않다 | team_id != 10  |
| >       | 크다    | salary > 3000  |
| <       | 작다    | salary < 3000  |
| >=      | 이상    | salary >= 3000 |
| <=      | 이하    | salary <= 3000 |

---

## 4. WHERE + AND / OR (복합 조건)

### 4-1. AND : 모든 조건을 동시에 만족

```sql
SELECT *
FROM staff
WHERE team_id = 11
  AND salary >= 7000;
```

→ 11번 팀에 속하면서, 급여가 7000 이상인 직원만 조회


### 4-2. OR : 조건 중 하나만 만족해도 조회

```sql
SELECT *
FROM staff
WHERE team_id = 11
   OR team_id = 12;
```

→ 팀 번호가 11 또는 12인 직원 조회

---

## 5. WHERE + BETWEEN (범위 조건)

```sql
SELECT name_ko, salary
FROM staff
WHERE salary BETWEEN 5000 AND 8000;
```

→ 급여가 5000 이상 8000 이하인 직원 조회


날짜에도 BETWEEN을 사용할 수 있습니다.

```sql
SELECT name_ko, hired_at
FROM staff
WHERE hired_at BETWEEN '2018-01-01' AND '2020-12-31';
```

### 5-1. DATETIME / TIMESTAMP 주의사항

BETWEEN '2023-01-01' AND '2023-12-31' 라고 쓰면
내부적으로는 다음과 같이 해석됩니다.

시작: 2023-01-01 00:00:00
끝: 2023-12-31 00:00:00

---

## 6. WHERE + IN (목록 조건)

```sql
SELECT *
FROM staff
WHERE team_id IN (10, 11, 12);
```

→ team_id가 10 또는 11 또는 12 인 직원 조회

같은 내용을 OR로 쓰면:

```sql
WHERE team_id = 10
   OR team_id = 11
   OR team_id = 12;
```

IN을 쓰는 편이 훨씬 간결하고 가독성이 좋습니다.

---

## 7. WHERE + LIKE (문자 패턴 검색)

| 패턴  | 의미           |
| --- | ------------ |
| %A% | A가 포함된 문자열   |
| A%  | A로 시작        |
| %A  | A로 끝         |
| _A  | 두 번째 글자가 A   |
| A_  | A로 시작하는 두 글자 |

예시:

```sql
SELECT *
FROM staff
WHERE name_ko LIKE '윤%';
```

→ 이름이 '윤'으로 시작하는 직원 조회

---

## 8. WHERE + IS NULL / IS NOT NULL

### 8-1. 구문
구문	의미
IS NULL	값이 없는 행 조회
IS NOT NULL	값이 존재하는 행 조회

예시: 보너스가 있는 직원만 조회

```sql
SELECT *
FROM staff
WHERE bonus IS NOT NULL;
```

예시: 보너스가 없는 직원만 조회

```sql
SELECT *
FROM staff
WHERE bonus IS NULL;
```

### 8-2. NULL의 의미

NULL은 “값이 없다 / 아직 정해지지 않았다” 는 뜻입니다.
0과도 다르고, 빈 문자열('')과도 다릅니다.
그래서 = NULL 이 아니라 반드시 IS NULL 로 비교해야 합니다.

---

## 9. 문제 풀이
### 문제 1:

staff 테이블에서 직급(position)이 'Deputy' 인 직원 정보를 조회하시오.

<details markdown="1"> 
<summary>정답</summary>

```sql
SELECT *
FROM staff
WHERE position = 'Deputy';
```
</details>

### 문제 2:

staff 테이블에서 팀 번호(team_id)가 11번이 아닌 직원 정보를 조회하시오.

<details markdown="1">
<summary>정답</summary>

```sql  
SELECT *
FROM staff
WHERE team_id != 11;
```

또는

```sql
SELECT *
FROM staff
WHERE team_id <> 11;
```
</details>

### 문제 3:

staff 테이블에서 팀 번호가 11번이고,
직급(position)이 'Lead' 또는 'Senior' 인 직원 정보를 조회하시오.

<details markdown="1">
<summary>정답</summary>

```sql  
SELECT *
FROM staff
WHERE team_id = 11
  AND position IN ('Lead', 'Senior');
```

또는

```sql
SELECT *
FROM staff
WHERE team_id = 11
  AND (position = 'Lead' OR position = 'Senior');
```
</details>

### 문제 4:

staff 테이블에서 보너스(bonus)가 없는 직원 정보를 조회하시오.

<details markdown="1"> 
<summary>정답</summary>

```sql
SELECT *
FROM staff
WHERE bonus IS NULL;
```
</details>

### 문제 5:

staff 테이블에서 이름의 두 번째 글자가 '운'인 직원 정보를 조회하시오.
(예: 김운항)

<details markdown="1"> 
<summary>정답</summary>

```sql  
SELECT *
FROM staff
WHERE name_ko LIKE '_운%';
```
</details> 
