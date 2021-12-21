# 나의 풀이
def solution(a, b):
    result = 0
    for i in range(min(a,b), max(a,b)+1):
        result += i
    return result

# 다른 풀이
def solution(a, b):
    return sum(range(min(a,b), max(a,b)+1))

# 다른 풀이
def solution(a, b):
    if a > b: a, b = b, a
    return sum(range(a,b+1))