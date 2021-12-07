# 2개의 수를 입력받아 최대공약수와 최소공배수를 반환하라

def solution(n, m):
    result = []

    divisor = [a for a in range(1,min(n,m)+1) if n % a == 0 and m % a == 0]
    result.append(divisor[-1])

    multiple = [b for b in range(max(n,m),(n*m)+1) if b % n == 0 and b % m == 0]
    result.append(multiple[0])
    
    print(result)
    return result

solution(8,3)

