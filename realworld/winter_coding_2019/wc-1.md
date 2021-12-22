# 직사각형 대각선 갯수
```python
def solution(w,h):
    def gcd(a, b):
        if a < b:
            (a, b) = (b, a)
        while b != 0:
            (a, b) = (b, a % b)
        return a
    answer = w*h-(w + h - gcd(w, h))
    return answer
```