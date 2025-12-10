---
layout: default
title: "SQL Study 003 – Basic SQL (KR)"
date: 2025-12-10
order: 3
---

# SQL Study 003 – Basic SQL (KR)

기초 SQL에서 가장 먼저 배우는 SELECT 구문과  
데이터 조회 방식의 기본 구조를 정리한 내용입니다.

---

## 1. SQL 작성 순서와 실행 순서

### 1-1. 작성 순서 (사람이 쓰는 순서)

SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY


### 1-2. 실행 순서 (DB가 처리하는 실제 순서)

FROM → ON → JOIN → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY

---

## 2. SELECT ~ FROM의 기본 개념

### 2-1. 정의  
SELECT 구문은 데이터베이스의 데이터를 조회하기 위한 가장 기본적인 SQL 문입니다.  
즉, “어떤 테이블에서 어떤 컬럼을 가져올 것인지”를 지정합니다.

### 2-2. 기본 문법 구조

```sql
-- 모든 컬럼 조회
SELECT * FROM staff;

-- 특정 컬럼 조회 (별칭 사용)
SELECT name_ko AS '이름', position AS '직급'
FROM staff;
```

### 2-3. 핵심 요소

SELECT : 가져올 컬럼 지정
FROM : 데이터를 가져올 테이블 지정
* : 모든 컬럼 조회
AS : 결과 화면에서만 표시되는 임시 컬럼명(별칭)

---

## 3. DISTINCT
DISTINCT는 SELECT 결과에서 중복 값을 제거하고 고유한 값만 출력하는 기능입니다.

```sql
SELECT DISTINCT position
FROM staff;
```

---

## 4. 문제 풀이

### 문제 1:
staff 테이블을 전체 조회하시오.

<details>
<summary>정답</summary>
       
```sql
SELECT * FROM staff;
</details>
```

### 문제 2:
아래 출력 형식을 만족하도록 staff 테이블에서 사번, 이름(한글), 직급을 조회하시오.

| 사번   | 이름  | 직급        |
| ---- | --- | --------- |
| 1000 | 윤사령 | CEO       |
| 7001 | 백항해 | Executive |
| 7002 | 김운항 | Manager   |
| 4001 | 정민호 | Manager   |
| 7003 | 윤세진 | Manager   |
| 7004 | 한지우 | Deputy    |
| 7005 | 고은채 | Lead      |
| 7006 | 송도현 | Lead      |
| 7007 | 임하늘 | Senior    |
| 7008 | 조민재 | Senior    |
| 4002 | 백다은 | Senior    |
| 7009 | 오지훈 | Junior    |
| 7010 | 류서연 | Junior    |
| 8001 | 문건우 | FieldLead |

<details>
<summary>정답</summary>

```sql
SELECT  staff_id AS '사번'
       ,name_ko  AS '이름'
       ,position AS '직급'
FROM staff;
</details>
```

### 문제3:
staff 테이블에서 중복 없이 직급 목록을 출력하시오.

<details>
<summary>정답</summary>

```sql
SELECT DISTINCT position
FROM staff;
</details>
```
