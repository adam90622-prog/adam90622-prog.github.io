---
layout: post
title: "SQL Study 001 – 데이터베이스 구조 이해 (KR)"
date: 2025-12-12
order: 1
---

# SQL Study 001 – 데이터베이스 구조 이해 (KR)

이 문서는 MySQL이 데이터를 어떻게 구성하고 저장하는지 설명합니다.  
우리가 앞으로 사용할 실습 환경 기준으로 정리되어 있습니다.

---

# 1. 인스턴스 → 데이터베이스 → 테이블

<!-- IMAGE_1_HERE -->

## 1-1. 인스턴스(Instance)

인스턴스는 **현재 실행 중인 MySQL 서버 프로그램**입니다.  
즉, 메모리를 점유하고 작동 중인 DB 엔진 자체를 의미합니다.


---

## 1-2. 데이터베이스(Database, Schema)

MySQL에서는 **Database = Schema (완전히 동일한 개념)** 입니다.

특징:

- 서로 완전히 **독립적**
- 다른 DB끼리는 **JOIN 불가**
- 운영/개발/테스트 등 용도별로 분리하여 사용

---

## 1-3. 테이블(Table)

실제 데이터가 저장되는 곳입니다.

테이블 = 엑셀 시트 1장  
- 행(Row) = 데이터 1건  
- 열(Column) = 속성(Attribute)

---

## 1-4. 컬럼(Column)

데이터의 속성을 정의합니다.

예시 (staff 테이블):

| 컬럼명      | 의미 |
|-------------|------|
| staff_id    | 고유 사번 |
| name_ko     | 한글 이름 |
| name_en     | 영문 이름 |
| position    | 직책/직급 |

---

## 1-5. 행(Row)

데이터 1건(레코드)을 의미합니다.

예시:

staff_id name_ko position team_id is_active
7001 백항해 Executive 10 TRUE


---

# 2. ERD (엔터티 관계도)

<!-- IMAGE_2_HERE -->

우리가 SQL 실습에서 사용할 테이블 구조(ERD)는 아래와 같습니다.

---

## 2-1. staff 테이블 설명

| 번호 | 컬럼명     | 타입           | 설명 |
|------|-------------|----------------|------|
| 1  | staff_id   | INT (PK)     | 직원 고유 번호 |
| 2  | name_ko    | VARCHAR(50)  | 한글 이름 |
| 3  | name_en    | VARCHAR(100) | 영어 이름 |
| 4  | position   | VARCHAR(50)  | 직책/직급 |
| 5  | manager_id | INT          | 직속 상사의 staff_id |
| 6  | hired_at   | DATE         | 입사일 |
| 7  | salary     | INT          | 기본급 |
| 8  | bonus      | INT          | 성과급/인센티브 |
| 9  | team_id    | INT (FK)     | team 테이블과 연결 |
|10 | is_active  | BOOLEAN      | 재직 상태 |

---

## 2-2. team 테이블 설명

| 번호 | 컬럼명     | 타입           | 설명 |
|------|-------------|----------------|------|
| 1 | team_id     | INT (PK)     | 팀 고유 ID |
| 2 | team_name   | VARCHAR(100) | 팀 이름 |
| 3 | office      | VARCHAR(100) | 근무 지역 |

---
