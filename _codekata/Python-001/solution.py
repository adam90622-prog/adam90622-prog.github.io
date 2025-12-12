```python
"""
PY 001 – Sum of Digits (Programmers #12931)

Problem:
Given an integer n, return the sum of its digits.
"""

def solution(n: int) -> int:
    """Return the sum of digits of integer n."""
    return sum(map(int, str(n)))

def solution2(nums):
    num = str(nums)
    num2=list(num)
    t=[]
    for n in num2:
        t.append(int(n))
    return(sum(t))

if __name__ == "__main__":
    # Simple manual tests
    print(solution(123))  # Expected: 6
    print(solution(987))  # Expected: 24

    print(solution2(123))  # Expected: 6
    print(solution2(987))  # Expected: 24
