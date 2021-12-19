def solution(s, n):
    result = []
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'

    for i in s:
        if i == ' ':
            result.append(' ')
        elif i in upper:    
            result.append(upper[(upper.find(i)+n)%26])
        else:
            result.append(lower[(lower.find(i)+n)%26])

    return ''.join(result)