# 나의 풀이
def solution(s):
    count_p = 0
    count_y = 0
    
    for i in s:
        if i == 'p' or i == 'P':
            count_p += 1
            
        if i == 'y' or i == 'Y':
            count_y += 1
    
    if count_p != count_y:
        return False
    
    else:
        return True

# 다른 풀이
def solution(s):
    return s.lower().count('p') == s.lower().count('y')