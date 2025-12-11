---
layout: default
title: "SQL Study 006 – 내장 함수 (KR)"
date: 2025-12-10
order: 6
---

# SQL Study 006 – 내장 함수 (KR)

SQL에서 자주 사용하는 **문자열 함수, 숫자 함수, 날짜 함수, 변환형 함수, NULL 처리 함수**를 정리하고  
각 개념을 연습 문제로 확인합니다.

---

# 1. 내장 함수란?

- 입력값을 받아 특정 연산을 수행하고 결과를 반환하는 데이터 처리 도구  
- SQL 함수는 크게 다음과 같이 나뉜다:

### 단일행 함수 (Single-Row Function)
- 문자열 함수
- 숫자형 함수
- 날짜형 함수
- 변환형 함수
- NULL 관련 함수

### 다중행 함수 (Multi-Row Function)
- 집계 함수 (SUM, AVG 등)
- 그룹 함수
- 윈도우 함수

---

# 2. 문자열 함수

## 2-1. 주요 문자열 함수

| 함수 | 의미 | 예시 |
|------|------|------|
| UPPER() | 대문자로 변환 | UPPER(name) |
| LOWER() | 소문자로 변환 | LOWER(name) |
| LENGTH() | 바이트 길이 | LENGTH(name) |
| LEFT() | 왼쪽에서 문자 추출 | LEFT('BIGDATA', 3) |
| RIGHT() | 오른쪽에서 문자 추출 | RIGHT('BIGDATA', 4) |
| SUBSTRING() | 부분 문자열 추출 | SUBSTRING(name, 1, 2) |
| REPLACE() | 문자열 치환 | REPLACE(name, '김', '이') |
| LTRIM() | 왼쪽 문자 제거 | LTRIM('ABCD','A') |
| RTRIM() | 오른쪽 문자 제거 | RTRIM('ABCD','A') |
| TRIM() | 양쪽 공백 제거 | TRIM(name) |
| CONCAT() | 문자열 결합 | CONCAT(name, deptno) |
| LPAD() | 왼쪽 채우기 | LPAD(name, 8, '*') |
| RPAD() | 오른쪽 채우기 | RPAD(name, 8, '*') |
| POSITION() | 특정 문자 위치 반환 | POSITION('D' IN 'BIGDATA') |

> 한글 길이는 반드시 **CHAR_LENGTH()** 사용

---

## 2-2. 문제

### 문제 1:
아래와 같은 형태로 출력하시오.

| 이름 [직급] |
|-------------|
| 김대표 [CEO] |
| 최재혁 [부장] |
| … |

<details markdown="1">
<summary>정답</summary>

```sql
SELECT CONCAT(ename_ko, ' [', joblv, ']') AS '이름 [직급]'
FROM emp;
```
</details>

## 문제 2:
이름 글자수별 인원수를 출력하시오.

예시:
| 이름길이 | 카운트 |
| ---- | --- |
| 3    | 13  |
| 4    | 1   |

<details markdown="1"> 
<summary>정답</summary>

```sql
SELECT CHAR_LENGTH(ename_ko) AS '이름길이',
       COUNT(*) AS '카운트'
FROM emp
GROUP BY 이름길이;
```
</details>

## 문제 3:
이름의 마지막 글자가 ‘수’로 끝나는 직원의 정보를 아래와 같이 출력하시오.
(영문명은 대문자로 출력)

예시:
| 이름   | 영문명           |
| ---- | ------------- |
| 남궁민수 | NAMGUNG MINSU |
| 김낙수  | KIM NAKSU     |

<details markdown="1"> 
<summary>정답</summary>

```sql
SELECT ename_ko AS '이름',
       UPPER(ename_en) AS '영문명'
FROM emp
WHERE RIGHT(ename_ko, 1) = '수';
```
</details>

## 문제 4:
이름이 김낙수인 사원의 직급을 REPLACE 함수로 ‘부장 → 상무’로 변경하여 출력하시오.

<details markdown="1"> 
<summary>정답</summary>

```sql
SELECT ename_ko AS '이름',
       joblv AS '현 직급',
       REPLACE(joblv, '부장', '상무') AS '승진 직급'
FROM emp
WHERE ename_ko = '김낙수';
```
</details>

## 문제 5:
이름을 익명 처리하여 출력하시오.
(성을 제외한 모든 글자는 ** 처리)

예시:

| 직급 | 이름 | 연봉 | 성과금 |
| -- | -- | -- | --- |

<details markdown="1"> 
<summary>정답</summary>

```sql
SELECT joblv AS '직급',
       CONCAT(LEFT(ename_ko,1),'**') AS '이름',
       sal AS '연봉',
       comm AS '성과금'
FROM emp;
```
</details>

---

# 3. 숫자형 함수

## 3-1. 주요 숫자 함수

| 함수         | 의미         | 예시                  |
| ---------- | ---------- | ------------------- |
| TRUNCATE() | 버림(내림)     | TRUNCATE(3.14159,3) |
| ROUND()    | 반올림        | ROUND(3.6)          |
| MOD()      | 나머지 반환     | MOD(10,3)           |
| CEIL()     | 올림         | CEIL(3.2)           |
| FLOOR()    | 내림         | FLOOR(3.6)          |
| ABS()      | 절댓값        | ABS(-10)            |
| SIGN()     | 양수/음수/0 판별 | SIGN(-20)           |
| SQRT()     | 제곱근        | SQRT(16)            |
| POWER()    | 거듭제곱       | POWER(2,3)          |
| LOG()      | 자연 로그      | LOG(10)             |

---

## 3-2. 문제

### 문제 1:

급여가 6000 이상인 사원의 연봉·월급을 출력하시오.
(월급 = 연봉/12, 소수점 0자리까지 버림, 월급 기준 내림차순)

<details markdown="1"> 
<summary>정답</summary>
  
```sql
SELECT CONCAT(ename_ko, ' [', joblv, ']') AS '이름[직급]',
       sal AS '연봉',
       TRUNCATE(sal/12, 0) AS '월급'
FROM emp
WHERE sal >= 6000
ORDER BY 3 DESC;
```
</details>

### 문제 2:

보너스 비율(= 성과금 / 연봉 × 100)을 소수점 2자리 반올림하여 출력하시오.
(성과금 0원 제외)

<details markdown="1"> 
<summary>정답</summary>

```sql
SELECT ename_ko AS '이름',
       sal AS '연봉',
       comm AS '성과금',
       CONCAT(ROUND(comm/sal*100, 2), '%') AS '보너스 비율'
FROM emp
WHERE comm != 0
ORDER BY 4 DESC;
```
</details>

---

# 4. 날짜형 함수

## 4-1. 주요 날짜 함수

| 함수            | 의미         |
| ------------- | ---------- |
| NOW()         | 현재 날짜+시간   |
| CURDATE()     | 현재 날짜      |
| DATE()        | 날짜만 추출     |
| YEAR()        | 연도         |
| MONTH()       | 월          |
| DAY()         | 일          |
| HOUR()        | 시          |
| MINUTE()      | 분          |
| SECOND()      | 초          |
| DATEDIFF()    | 날짜 차이      |
| ADDDATE()     | 날짜 더하기     |
| SUBDATE()     | 날짜 빼기      |
| LAST_DAY()    | 해당 월 마지막 날 |
| DATE_FORMAT() | 날짜 → 문자열   |

---

## 4-2. 문제

### 문제 1:

오늘 날짜를 YY.MM.DD 형식으로 출력하시오.

<details markdown="1"> 
<summary>정답</summary>

```sql
SELECT DATE_FORMAT(CURDATE(), '%y.%m.%d') AS 'Today';
```
</details>

### 문제 2:

2010년대(2010–2019) 입사자를 입사일 기준 오름차순으로 출력하시오.

<details markdown="1"> 
<summary>정답</summary>

```sql
SELECT ename_ko AS '이름',
       joblv AS '직급',
       DATE_FORMAT(hiredate, '%m/%d/%y') AS '입사일'
FROM emp
WHERE hiredate >= '2010-01-01'
  AND hiredate < '2020-01-01'
ORDER BY hiredate;
```
</details>

### 문제 3:

입사일 기준 근속연수를 계산하여 내림차순 정렬하시오.
(입사 즉시 1년차로 간주)

<details markdown="1"> 
<summary>정답</summary>

```sql
SELECT ename_ko AS '이름',
       YEAR(CURDATE()) - YEAR(hiredate) + 1 AS '근속연수'
FROM emp
ORDER BY 2 DESC;
```
</details>

### 문제 4:

근무일수(= 오늘 − 입사일)가 2500~7500일 사이인 직원을 출력하시오.

<details markdown="1"> 
<summary>정답</summary>

```sql
SELECT ename_ko AS '이름',
       DATEDIFF(CURDATE(), hiredate) AS '근무일수'
FROM emp
WHERE DATEDIFF(CURDATE(), hiredate) BETWEEN 2500 AND 7500
ORDER BY 2 DESC;
```
</details>

### 문제 5:

입사 요일별 인원수를 출력하시오.

<details markdown="1"> 
<summary>정답</summary>

```sql
SELECT DAYOFWEEK(hiredate) AS '요일',
       COUNT(*) AS '직원수'
FROM emp
GROUP BY 1
ORDER BY 1;
```
</details>

---

# 5. 변환형 함수

## 5-1. 주요 변환 함수

| 함수            | 의미            | 예시                                    |
| ------------- | ------------- | ------------------------------------- |
| CAST()        | 타입 변환         | CAST(100 AS CHAR)                     |
| FORMAT()      | 숫자 포맷 (콤마 포함) | FORMAT(9999.9,1)                      |
| DATE_FORMAT() | 날짜 → 문자열      | DATE_FORMAT(NOW(),'%Y%m%d')           |
| STR_TO_DATE() | 문자열 → 날짜      | STR_TO_DATE('20230301','%Y%m%d')      |
| CONVERT_TZ()  | 시간대 변환        | CONVERT_TZ(NOW(), '+00:00', '+09:00') |

---

## 5-2. 문제

### 문제 1:

총급여(연봉+성과금)를 ‘만원’ 단위로 계산하여 출력하시오.
재직 중인 직원만 포함.

<details markdown="1"> 
<summary>정답</summary>

```sql
SELECT ename_ko AS '이름',
       CONCAT(FORMAT(sal + comm, 0), '만원') AS '총급여'
FROM emp
WHERE employed = 1
ORDER BY sal + comm DESC;
```
</details>

### 문제 2:

UTC 시간을 한국 시간(KST, +09:00)으로 변환하여 함께 출력하시오.

<details markdown="1"> 
<summary>정답</summary>

```sql
SELECT NOW() AS 'utc_time',
       CONVERT_TZ(NOW(), '+00:00', '+09:00') AS 'kst_time';
```
</details>

---

# 6. NULL 관련 함수

## 6-1. 주요 NULL 함수

| 함수         | 의미                | 예시                     |
| ---------- | ----------------- | ---------------------- |
| IFNULL()   | NULL → 지정값        | IFNULL(comm,0)         |
| COALESCE() | NULL 아닌 첫 번째 값 반환 | COALESCE(comm, sal, 0) |

---

## 6-2. 문제

### 문제:

매니저 번호가 NULL이면 자신의 사번을 매니저 사번으로 출력하시오.

<details markdown="1"> 
<summary>정답</summary>

```sql
SELECT empno AS '사원번호',
       IFNULL(mgr, empno) AS '매니저사번'
FROM emp;
```
</details>
