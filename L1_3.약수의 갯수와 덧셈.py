# 두 정수 left와 right가 매개변수로 주어집니다. 
# left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 
# 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

# ex) 13 ... 15 => 13(1,13 -> 2) / 14(1,2,7,14 -> 4) / 15(1,3,5,15 -> 4) => 13+14+15=42

def solution(left, right):
    temp  = []
    for a in range(left, right+1):
        count = 0
        for b in range(1,a+1):
            if a % b == 0:
                count += 1
        if count % 2 == 0:
            temp.append(a)
        else:
            temp.append(a * -1)
    print(sum(temp))
    return sum(temp)

solution(13, 17)


