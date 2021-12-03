# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 
# 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

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

