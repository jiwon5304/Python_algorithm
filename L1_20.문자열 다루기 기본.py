# 나의 풀이
def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i not in ['1','2','3','4','5','6','7','8','9','0']:
                return False
        return True
        
    else:
        return False

# 다른 풀이
def solution(s):
    return s.isdigit() and (len(s)==4 or len(s)==6)


