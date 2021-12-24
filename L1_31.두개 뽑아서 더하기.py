def solution(numbers):
    index = 0
    add = []
    for i in numbers[index:]:
        for j in numbers[index+1:]:
            add.append(i+j)
        index += 1
    set_result = set(add)
    result = sorted(set_result)
    print(result)
    return list(result)

solution([5,0,2,7])
