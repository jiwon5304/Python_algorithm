# 나의 풀이
def solution(n):
    s = '수박'
    return n // 2 * s if n % 2 == 0 else n // 2 * s + '수'

# 다른 사람 풀이
def solution(n):
    return '수박'*(n//2) + '수'*(n%2)