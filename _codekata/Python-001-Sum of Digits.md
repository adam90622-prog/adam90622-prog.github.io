---
title: "PY 001 – Sum of Digits"
date: 2025-12-11
language: python
order: 1
---

# Python Code Kata – PY 001: Sum of Digits (Programmers #12931)

---

# 📘 Problem (EN)
Given a positive integer `n`, return the sum of its digits.

For example:
- Input: `123` → Output: `6`
- Input: `987` → Output: `24`

This task requires splitting the number into digits and summing them.

---

# 📘 문제 설명 (KR)
양의 정수 `n`이 주어졌을 때, 각 자릿수의 합을 구하는 문제입니다.

예시:
- 입력: `123` → 출력: `6`
- 입력: `987` → 출력: `24`

즉, 숫자를 자릿수로 나누고 모두 더하면 됩니다.

---

# 🔒 Constraints / 제한사항
- 1 ≤ n ≤ 1,000,000,000

---

# ✨ Examples / 예시

| Input | Output |
|-------|--------|
| 123   | 6      |
| 987   | 24     |

---

# 💡 Approach (EN)
1. Convert the integer into a string.  
2. Iterate through each character (digit).  
3. Convert each character back to an integer.  
4. Sum all digits and return the result.

---

# 💡 사고 과정 (KR)
1. 숫자를 **문자열로 변환**한다.  
2. 문자열은 이미 **자릿수별로 나뉘어 있음**.  
3. 각 자릿수를 **정수로 변환**한다.  
4. 숫자들을 **모두 더해서** 반환한다.

---

# 🐍 Python Solution (EN)

<details markdown="1">
<summary>Solution (My Approach)</summary>

```python
def solution(nums):
    num = str(nums)
    num2 = list(num)
    t = []
    for n in num2:
        t.append(int(n))
    return sum(t)
```
</details> 

<details markdown="1"> <summary>Solution (Most Pythonic)</summary>
  
```python
def solution(n):
    return sum(map(int, str(n)))
```
</details>

---

# 🧪 Test Cases / 테스트 예시

- print(solution(123))   # 6
- print(solution(987))   # 24
- print(solution(1001))  # 2
