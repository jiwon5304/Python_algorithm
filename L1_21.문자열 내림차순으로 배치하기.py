# 나의 풀이
def solution(s):
    list_s = list(s)
    list_s.sort()
    list_s.reverse()
    return ''.join(list_s)

# 다른 풀이
def solution(s):
    return ''.join(sorted(s, reverse=True))