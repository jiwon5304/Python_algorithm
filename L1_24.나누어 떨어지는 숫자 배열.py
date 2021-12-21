# 나의 풀이
def solution(array, divisor):
    list = [i for i in array if i % divisor == 0]
    
    if len(list) == 0: 
        return [-1]

    else:
        return sorted(list)

# 다른 풀이
def solution(array, divisor):
    return sorted([n for n in array if n%divisor == 0]) or [-1]
