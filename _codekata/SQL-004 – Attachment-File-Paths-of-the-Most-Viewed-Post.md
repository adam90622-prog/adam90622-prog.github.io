---
title: "SQL 004 – Attachment File Paths of the Most Viewed Post"
date: 2025-12-12
language: sql
order: 4
---

# SQL Problem Explanation

## 조회수가 가장 많은 중고거래 게시판의 첨부파일 조회하기 (KR)

중고거래 게시판 정보가 담긴 **USED_GOODS_BOARD** 테이블과  
게시글 첨부파일 정보가 담긴 **USED_GOODS_FILE** 테이블이 있습니다.

### USED_GOODS_BOARD 테이블

| NAME | TYPE |
|------|------|
| BOARD_ID | INT |
| WRITER_ID | INT |
| TITLE | VARCHAR |
| CONTENTS | VARCHAR |
| PRICE | INT |
| CREATED_DATE | DATE |
| STATUS | VARCHAR |
| VIEWS | INT |

### USED_GOODS_FILE 테이블

| NAME | TYPE |
|------|------|
| FILE_ID | INT |
| FILE_EXT | VARCHAR |
| FILE_NAME | VARCHAR |
| BOARD_ID | INT |

---

### 문제 설명 (KR)

조회수가 가장 높은 **단 하나의 게시글**에 대해  
해당 게시글에 포함된 **첨부파일의 전체 경로(FILE_PATH)** 를 조회하는 SQL을 작성하세요.

- 파일 경로 형식  
  `/home/grep/src/{BOARD_ID}/{FILE_ID}{FILE_NAME}{FILE_EXT}`
- 결과는 `FILE_ID` 기준 **내림차순 정렬**
- 조회수가 가장 높은 게시글은 **유일함이 보장**됩니다.

---

## Attachment File Paths for the Most Viewed Post (EN)

You are given:
- **USED_GOODS_BOARD**: second-hand marketplace posts
- **USED_GOODS_FILE**: attachment file information

### Task (EN)

Write an SQL query to retrieve the **FILE_PATH** of attachments  
for the **single post with the highest number of views**.

- File path format  
  `/home/grep/src/{BOARD_ID}/{FILE_ID}{FILE_NAME}{FILE_EXT}`
- Sort results by `FILE_ID` in **descending order**
- The most-viewed post is guaranteed to be unique

---

## Source

- Programmers SQL Practice  
  https://school.programmers.co.kr/learn/courses/30/lessons/164671

---

## SQL Answer

### Answer 1 (My Answer)

<details markdown="1">
<summary>Answer</summary>

```sql
SELECT CONCAT('/home/grep/src/', a.BOARD_ID, '/', b.FILE_ID, b.FILE_NAME, b.FILE_EXT) AS FILE_PATH
FROM USED_GOODS_BOARD a
JOIN USED_GOODS_FILE b
  ON a.BOARD_ID = b.BOARD_ID
WHERE a.VIEWS = (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
ORDER BY b.FILE_ID DESC;
```
</details>

### Answer 2 (Efficient / Production-Friendly)

<details markdown="1"> <summary>Answer</summary>

```sql
SELECT CONCAT('/home/grep/src/', f.BOARD_ID, '/', f.FILE_ID, f.FILE_NAME, f.FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE f
JOIN (
    SELECT BOARD_ID
    FROM USED_GOODS_BOARD
    ORDER BY VIEWS DESC
    LIMIT 1
) b
ON f.BOARD_ID = b.BOARD_ID
ORDER BY f.FILE_ID DESC;
```
</details>
