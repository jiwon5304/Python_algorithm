def solution(n):
    for i in range(1,n+1):
        if n % i == 0 and i**2 == n:
            return (i+1)**2          
    return -1