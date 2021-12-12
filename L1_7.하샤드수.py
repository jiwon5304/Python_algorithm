def solution(x):
    result = 0
    for a in str(x):
        result += int(a)
    if x % result == 0:
        return True
    return False