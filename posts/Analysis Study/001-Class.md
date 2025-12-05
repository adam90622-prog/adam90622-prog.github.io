# 클래스 구조로 분석 흐름 정리하기

## 1. 문제 정의
분석 과정에서  
필터 조건이 많아질수록  
코드가 복잡해졌다.

## 2. 데이터 설명
게임 로그 데이터 (CSV)

## 3. 접근 방법
GameRecord / Analyzer 클래스로  
역할을 분리했다.

## 4. 분석 코드
```python
class GameRecord:
    def __init__(self, data):
        self.win = data["win"]

## 5. 결과
코드 가독성 향상
조건 추가가 쉬워짐

## 6. 인사이트
분석도 구조 설계가 중요하다.
