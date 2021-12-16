def solution(s):
    result = []

    for s in s.split(" "):
        list = []
        for i in range(len(s)):
            if i % 2 == 1:
                list.append(s[i].lower())
            else:
                list.append(s[i].upper())
                
        result.append((''.join(list)))
        result.append(' ')

    return ''.join(result)[:-1]


