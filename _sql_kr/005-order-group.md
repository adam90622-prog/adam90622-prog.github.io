---
layout: default
title: "SQL Study 005 – ORDER BY, LIMIT, GROUP BY, HAVING (KR)"
date: 2025-12-10
order: 5
---

# SQL Study 005 – ORDER BY, LIMIT, GROUP BY, HAVING (KR)

이 장에서는 조회 결과의 **정렬(ORDER BY)**, **행 개수 제한(LIMIT)**,  
그리고 **그룹화(GROUP BY), 그룹 조건(HAVING)** 을 다룹니다.

---

## 1. ORDER BY 개념

- ORDER BY는 **조회된 데이터를 정렬(Sort)하는 절**입니다.
- 숫자, 문자열, 날짜를 기준으로 **오름차순(ASC) / 내림차순(DESC)** 정렬이 가능합니다.
- **SELECT 결과의 “보이는 순서”만 바뀌며, 실제 저장된 데이터는 변하지 않습니다.**

---

## 2. ORDER BY 기본 문법

```sql
SELECT 컬럼명
FROM 테이블명
ORDER BY 컬럼명 [ASC | DESC];
```
ASC : 오름차순 (기본값, 생략 가능)
DESC : 내림차순

### 2-1. ORDER BY에서 별칭 사용

```sql
SELECT salary * 12 AS annual_salary
FROM staff
ORDER BY annual_salary DESC;
```

SELECT에서 만든 별칭(annual_salary) 은 ORDER BY에서 사용할 수 있습니다.
단, WHERE 절에서는 별칭을 사용할 수 없습니다.

---

## 3. LIMIT 개념

LIMIT는 조회할 행(row)의 개수를 제한하는 절입니다.
상위 N개 조회, 페이징 처리 등에 자주 사용됩니다.

--- 

## 4. LIMIT 기본 문법

```sql
SELECT 컬럼명
FROM 테이블명
LIMIT 개수;
```

예시:

```sql
SELECT name_ko, salary
FROM staff
ORDER BY salary DESC
LIMIT 5;
```
→ 급여가 높은 순으로 상위 5명만 조회

### 4-1. LIMIT + OFFSET (페이징)

```sql
SELECT *
FROM staff
ORDER BY staff_id
LIMIT 5 OFFSET 5;
```
→ staff_id 기준으로 정렬했을 때, 6번째 행부터 5개 행을 조회

---

## 5. GROUP BY 개념

GROUP BY는 특정 컬럼을 기준으로 행들을 “그룹(묶음)”으로 모으는 절입니다.
보통 COUNT, SUM, AVG, MAX, MIN 같은 집계 함수와 함께 사용합니다.

예: “팀별 인원 수”, “직급별 평균 급여” 같은 요약 통계에 사용됩니다.

---

## 6. GROUP BY 기본 문법

```sql
SELECT 그룹기준컬럼, 집계함수(컬럼)
FROM 테이블명
GROUP BY 그룹기준컬럼;
```

### 6-1. 집계 함수 정리

| 함수      | 의미  | 예시 용도 |
| ------- | --- | ----- |
| COUNT() | 개수  | 인원 수  |
| SUM()   | 합계  | 총 급여  |
| AVG()   | 평균  | 평균 급여 |
| MAX()   | 최댓값 | 최고 급여 |
| MIN()   | 최솟값 | 최저 급여 |

---

## 7. HAVING 개념

HAVING은 GROUP BY로 묶인 그룹 결과에 조건을 거는 절입니다.
WHERE는 각 행(row) 을 필터링할 때 사용합니다.
HAVING은 그룹화된 결과(집계 값) 를 필터링할 때 사용합니다.

---

## 8. HAVING 기본 문법

```sql
SELECT 그룹컬럼, 집계함수(컬럼)
FROM 테이블명
GROUP BY 그룹컬럼
HAVING 그룹조건;
```

## 9. 문제 풀이

### 문제 1:
staff 테이블에서 급여(salary)가 5000 이상인 직원 중,
급여가 높은 순으로 3명만 조회하시오.

<details markdown="1"> 
<summary>정답</summary>

```sql
SELECT *
FROM staff
WHERE salary >= 5000
ORDER BY salary DESC
LIMIT 3;
```
</details>

### 문제 2:

staff 테이블에서 급여(salary)가 5000 이상인 직원 중,
급여가 높은 순으로 정렬했을 때, 상위 3명을 건너뛰고 다음 5명을 조회하시오.

<details markdown="1"> 
<summary>정답</summary>

```sql
SELECT *
FROM staff
WHERE salary >= 5000
ORDER BY salary DESC
LIMIT 5 OFFSET 3;
```
</details>

### 문제 3:

staff 테이블에서 팀별 인원 수를 구하시오.

예상 결과 예시:

| 팀 번호 | 인원수 |
| ---- | --- |
| NULL | 1   |
| 10   | 1   |
| 11   | 6   |
| 12   | 3   |
| 40   | 1   |
| 80   | 2   |

<details markdown="1"> 
<summary>정답</summary>

```sql
SELECT team_id, COUNT(*) AS '인원수'
FROM staff
GROUP BY team_id;
```
</details>

### 문제 4:

staff 테이블에서 평균 급여가 7000 이상인 직급(position) 만 조회하시오.

예상 결과 예시:

| 직급        | 평균급여       |
| --------- | ---------- |
| CEO       | 82000.0000 |
| Executive | 23000.0000 |
| Manager   | 14000.0000 |
| Deputy    | 10200.0000 |
| Lead      | 7650.0000  |

<details markdown="1"> 
<summary>정답</summary>

```sql
SELECT position, AVG(salary) AS '평균급여'
FROM staff
GROUP BY position
HAVING AVG(salary) >= 7000;
```
</details>

### 문제 5:

staff 테이블에서 팀별 최고 급여, 최저 급여, 평균 급여를 구하시오.

예상 결과 예시:

| 팀 번호 | 최고급여  | 최저급여  | 평균급여       |
| ---- | ----- | ----- | ---------- |
| NULL | 82000 | 82000 | 82000.0000 |
| 10   | 23000 | 23000 | 23000.0000 |
| 11   | 16000 | 4850  | 8450.0000  |
| 12   | 12500 | 4520  | 8205.0000  |
| 40   | 6050  | 6050  | 6050.0000  |
| 80   | 13500 | 5050  | 9275.0000  |

<details markdown="1"> 
<summary>정답</summary>

```sql
SELECT  team_id AS '팀 번호'
       ,MAX(salary) AS '최고급여'
       ,MIN(salary) AS '최저급여'
       ,AVG(salary) AS '평균급여'
FROM staff
GROUP BY team_id;
```
</details> 
