# 2개의 수를 입력받아 최대공약수와 최소공배수를 반환하라

def solution(n, m):
    result = []
    
    # 범위 : 1 ~ 입력 중 작은수 / n,m 모두 나눠지는 숫자중에서 가장 큰 수
    divisor = [a for a in range(1,min(n,m)+1) if n % a == 0 and m % a == 0]
    result.append(divisor[-1])

    # 범위 : 입력 중 큰 수 ~ 두 수의 곱 / 두 개의 입력으로 나눠지는 수 중에서 가장 작은 수
    multiple = [b for b in range(max(n,m),(n*m)+1) if b % n == 0 and b % m == 0]
    result.append(multiple[0])
    
    return result

solution(8,3)

