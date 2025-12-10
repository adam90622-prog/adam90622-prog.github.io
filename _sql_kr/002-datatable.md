---
layout: post
title: "SQL Study 002 – DB & Table Setup (KR)"
date: 2025-12-09
order: 2
---

# 001. Part 1 — DB & Table Setup (KR)

## 1. 데이터베이스 만들기
```sql
-- 1-1. 기존에 learn_sql 데이터베이스가 존재하면 삭제
DROP DATABASE IF EXISTS learn_sql;

-- 1-2. learn_sql 이라는 이름의 새로운 데이터베이스 생성
CREATE DATABASE learn_sql
  DEFAULT CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;

-- 1-3. 앞으로 실행되는 모든 쿼리를 learn_sql 데이터베이스 기준으로 수행
USE learn_sql;
```

## 2. staff 테이블 만들기 (사원/직원 정보)
```sql
-- 2-1. staff 테이블이 이미 존재하면 먼저 삭제
DROP TABLE IF EXISTS staff;

-- 2-2. 직원 정보를 저장하는 staff 테이블 생성
CREATE TABLE staff (
  staff_id     INT PRIMARY KEY,   -- 사번
  name_ko      VARCHAR(50),       -- 직원 이름(국문)
  name_en      VARCHAR(100),      -- 직원 이름(영문)
  position     VARCHAR(50),       -- 직급
  manager_id   INT,               -- 직속 상사 사번
  hired_at     DATE,              -- 입사일
  salary       INT,               -- 기본 연봉(또는 월급)
  bonus        INT,               -- 성과급/보너스
  team_id      INT,               -- 소속 팀 번호
  is_active    BOOLEAN            -- 재직 여부(TRUE: 재직, FALSE: 퇴사)
);
```

## 3. team 테이블 만들기 (부서/팀 정보)
```sql
-- 3-1. team 테이블이 이미 존재하면 먼저 삭제
--     (재실행 시 오류 방지 및 초기화 목적)
DROP TABLE IF EXISTS team;

-- 3-2. 부서(팀) 정보를 저장하는 team 테이블 생성
CREATE TABLE team (
  team_id    INT PRIMARY KEY,   -- 팀 번호
  team_name  VARCHAR(100),      -- 팀 이름
  office     VARCHAR(100)       -- 근무 지역/사무실 위치
);
```

## 4. staff 테이블 데이터 적재
```sql
-- 4-1. staff 테이블에 기존 데이터가 있으면 모두 삭제(초기화)
DELETE FROM staff;

-- 4-2. 직원 데이터 신규 등록
INSERT INTO staff
(staff_id, name_ko, name_en, position, manager_id, hired_at, salary, bonus, team_id, is_active)
VALUES
(1000, '윤사령',  'Yoon Director',      '대표이사',   NULL,  '1996-01-01', 82000, 0,     NULL, TRUE),
(7001, '백항해',  'Baek Executive',     '전무',       1000,  '1998-07-01', 23000, 9000,  10,   TRUE),
(7002, '김운항',  'Kim Captain',        '부장',       7001,  '2000-03-15', 16000, 3000,  11,   TRUE),
(4001, '정민호',  'Jung Manager',       '부장',       1000,  '2003-08-19', 13500, 4000,  80,   TRUE),
(7003, '윤세진',  'Yoon Senior',        '부장',       7001,  '2006-05-21', 12500, 6000,  12,   TRUE),
(7004, '한지우',  'Han Deputy',         '차장',       7003,  '2017-11-10', 10200, 2500,  12,   TRUE),
(7005, '고은채',  'Ko Manager',         '과장',       7002,  '2000-03-15',  8100, 1800,  11,   FALSE),
(7006, '송도현',  'Song Manager',       '과장',       7002,  '2015-04-03',  7200, 1500,  11,   TRUE),
(7007, '임하늘',  'Lim Assistant',      '대리',       7002,  '2019-09-11',  6100,  0,    11,   TRUE),
(7008, '조민재',  'Cho Assistant',      '대리',       7003,  '2020-06-08',  5600,  0,    12,   TRUE),
(4002, '백다은',  'Baek Assistant',     '대리',       4001,  '2021-07-08',  5050,  0,    80,   TRUE),
(7009, '오지훈',  'Oh Staff',           '사원',       7002,  '2022-01-03',  4850,  900,  11,   TRUE),
(7010, '류서연',  'Ryu Staff',          '사원',       7003,  '2022-03-02',  4520,  900,  12,   TRUE),
(8001, '문건우',  'Moon FieldLeader',   '현장반장',   NULL,  '2015-04-03',  6050, 1900,  40,   TRUE);
```

## 5. team 테이블 데이터 적재
```sql
-- 5-1. team 테이블에 기존 데이터가 있으면 모두 삭제(초기화)
DELETE FROM team;

-- 5-2. 부서(팀) 데이터 신규 등록
INSERT INTO team (team_id, team_name, office) VALUES
  (10, '비즈니스본부',   '서울'),
  (11, '국내영업1팀',   '서울'),
  (12, '국내영업2팀',   '서울'),
  (40, '생산센터',       '아산'),
  (80, '인사운영팀',     '서울');
```

## 6. 데이터 적재 확인용 조회
```sql
-- 6-1. 직원 데이터가 잘 들어갔는지 확인
SELECT * FROM learn_sql.staff;

-- 6-2. 팀 데이터가 잘 들어갔는지 확인
SELECT * FROM learn_sql.team;
```
