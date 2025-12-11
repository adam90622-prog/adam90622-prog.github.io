----
layout: default
title: "SQL Study 006 – 내장 함수 (KR)"
date: 2025-12-10
order: 6
---

# SQL Study 006 – 내장 함수 (KR)

이 장에서는 `staff` 테이블을 기준으로, SQL에서 자주 사용하는 **내장 함수**들을 정리하고  
문제 풀이를 통해 활용법을 익힙니다.

사용 테이블: **staff**

```sql
CREATE TABLE staff (
  staff_id   INT PRIMARY KEY,
  name_ko    VARCHAR(50),
  name_en    VARCHAR(100),
  position   VARCHAR(50),
  manager_id INT,
  hired_at   DATE,
  salary     INT,
  bonus      INT,
  team_id    INT,
  is_active  BOOLEAN
);
```

---

# 1. 내장 함수란?

- 입력값을 받아 특정 연산을 수행하고 결과를 반환하는 데이터 처리 도구  
- SQL 함수는 크게 다음과 같이 나뉜다:

### 1-1. 단일행 함수 (Single-Row Function)
- 문자열 함수
- 숫자형 함수
- 날짜형 함수
- 변환형 함수
- NULL 관련 함수

### 1-2. 다중행 함수 (Multi-Row Function)
- 집계 함수 (SUM, AVG 등)
- 그룹 함수
- 윈도우 함수
→ 여러 행을 모아서 **요약값(집계 결과)**을 반환

---

# 2. 문자열 함수

## 2-1. 주요 문자열 함수

| 함수            | 의미                | 예시                              |
| ------------- | ----------------- | ------------------------------- |
| UPPER()       | 대문자로 변환           | `UPPER(name_en)`                |
| LOWER()       | 소문자로 변환           | `LOWER(name_en)`                |
| LENGTH()      | 바이트 길이            | `LENGTH(name_ko)`               |
| CHAR_LENGTH() | 문자 길이(한글 글자 수)    | `CHAR_LENGTH(name_ko)`          |
| LEFT()        | 왼쪽에서 N글자 잘라내기     | `LEFT('BIGDATA', 3)`            |
| RIGHT()       | 오른쪽에서 N글자 잘라내기    | `RIGHT('BIGDATA', 4)`           |
| SUBSTRING()   | 부분 문자열 추출         | `SUBSTRING(name_ko, 2, 2)`      |
| REPLACE()     | 문자열 치환            | `REPLACE(position, '부장', '이사')` |
| LTRIM()       | 왼쪽에서 특정 문자/공백 제거  | `LTRIM(' ABC', ' ')`            |
| RTRIM()       | 오른쪽에서 특정 문자/공백 제거 | `RTRIM('ABC ', ' ')`            |
| TRIM()        | 양쪽 공백 제거          | `TRIM(name_en)`                 |
| CONCAT()      | 문자열 연결            | `CONCAT(name_ko, '님')`          |
| LPAD()        | 왼쪽을 채워 길이 맞추기     | `LPAD(name_ko, 5, '*')`         |
| RPAD()        | 오른쪽을 채워 길이 맞추기    | `RPAD(name_ko, 5, '*')`         |
| POSITION()    | 부분 문자열 위치 (없으면 0) | `POSITION('D' IN 'BIGDATA')`    |

→ 한글 이름 글자 수는 LENGTH()가 아니라 CHAR_LENGTH() 사용

---

## 2-2. 문제

### 문제 1:
staff 테이블에서 아래와 같은 형식으로 출력하시오.

예) 윤사령 [대표이사]

<details markdown="1">
<summary>정답</summary>

```sql
SELECT CONCAT(name_ko, ' [', position, ']') AS '이름 [직급]'
FROM staff;
```
</details>

## 문제 2:
staff 테이블에서 이름 글자 수별 인원 수를 구하시오.
(이름 글자 수는 한글 기준, CHAR_LENGTH(name_ko) 사용)

<details markdown="1"> 
<summary>정답</summary>

```sql
SELECT CHAR_LENGTH(name_ko) AS '이름길이',
       COUNT(*)             AS '카운트'
FROM staff
GROUP BY 이름길이;
```
</details>

## 문제 3:
이름의 **마지막 글자가 ‘현’**으로 끝나는 직원을 조회하고,
아래와 같이 출력하시오. (영문 이름은 대문자로 출력)

예시:
| 이름  | 영문명         |
| --- | ----------- |
| 송도현 | SONG DOHYUN |

<details markdown="1"> 
<summary>정답</summary>

```sql
SELECT name_ko        AS '이름',
       UPPER(name_en) AS '영문명'
FROM staff
WHERE RIGHT(name_ko, 1) = '현';
```
</details>

## 문제 4:
이름이 **'김운항'**인 직원에 대해,
현재 직급이 '부장'일 때 이를 '상무'로 바꾼 승진 직급을 함께 출력하시오.

<details markdown="1"> 
<summary>정답</summary>

```sql
SELECT name_ko                        AS '이름',
       position                       AS '현 직급',
       REPLACE(position, '부장', '상무') AS '승진 직급'
FROM staff
WHERE name_ko = '김운항';
```
</details>

## 문제 5:
이름을 익명 처리해서 성과 정보를 전달하려고 합니다.
성을 제외한 이름 부분은 모두 **로 처리하여 아래와 같이 출력하세요.

예시:

| 직급   | 이름  | 연봉    | 성과급  |
| ---- | --- | ----- | ---- |
| 대표이사 | 윤** | 82000 | 0    |
| 전무   | 백** | 23000 | 9000 |
| …    | …   | …     | …    |


<details markdown="1"> 
<summary>정답</summary>

```sql
SELECT position                         AS '직급',
       CONCAT(LEFT(name_ko, 1), '**')   AS '이름',
       salary                           AS '연봉',
       bonus                            AS '성과급'
FROM staff;
```
</details>

---

# 3. 숫자형 함수

## 3-1. 주요 숫자 함수

| 함수             | 의미                   | 예시                   |
| -------------- | -------------------- | -------------------- |
| TRUNCATE(x, n) | 소수점 n자리까지 남기고 **버림** | TRUNCATE(3.14159, 2) |
| ROUND(x, n)    | 소수점 n자리에서 **반올림**    | ROUND(3.14159, 2)    |
| MOD(a, b)      | a를 b로 나눈 **나머지**     | MOD(10, 3)           |
| CEIL(x)        | x 이상인 최소 정수(올림)      | CEIL(3.2)            |
| FLOOR(x)       | x 이하인 최대 정수(내림)      | FLOOR(3.8)           |
| ABS(x)         | 절댓값                  | ABS(-10)             |
| SIGN(x)        | 부호 (-1, 0, 1)        | SIGN(-5)             |
| POWER(a, b)    | a의 b제곱               | POWER(2, 3)          |
| SQRT(x)        | 제곱근                  | SQRT(16)             |


---

## 3-2. 문제

### 문제 1:

급여(salary)가 6000 이상인 직원에 대해,
아래와 같이 출력하시오.
 -이름[직급]
 -연봉(salary)
-월급 = 연봉 / 12 (소수점 버림, 0자리까지)
-월급 기준 내림차순 정렬.

<details markdown="1"> 
<summary>정답</summary>
  
```sql
SELECT CONCAT(name_ko, ' [', position, ']') AS '이름[직급]',
       salary                               AS '연봉',
       TRUNCATE(salary / 12, 0)             AS '월급'
FROM staff
WHERE salary >= 6000
ORDER BY 월급 DESC;
```
</details>

### 문제 2:

보너스 비율을 계산해 보겠습니다.
| 보너스 비율(%) = bonus / salary × 100

다음 조건에 맞게 조회하시오.

성과급(bonus)이 0이 아닌 직원만

보너스 비율은 소수점 둘째 자리에서 반올림

예: 33.33% 형태의 문자열로 표시

보너스 비율 기준 내림차순 정렬
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
