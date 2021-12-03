def solution(arr1, arr2): 
    a = len(arr1)
    b = len(arr1[0])
    
    answer = []
    for i in range(a):
        e = []
        for j in range(b):
            c = arr1[i][j]
            d = arr2[i][j]
            e.append(c+d)
        answer.append(e)
    print(answer)
    return answer
    
solution([[1,2,3],[4,5,6]],[[2,3,4],[5,6,7]])

