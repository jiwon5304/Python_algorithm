#나의 풀이
def solution(n):
    n_list = list(map(int, str(n)))
    n_list.reverse()
    return n_list

# 다른풀이1
def solution(n):
    return list(map(int, reversed(str(n))))

# 다른풀이2
def solution(n):
    return [int(i) for i in str(n)][::-1]
