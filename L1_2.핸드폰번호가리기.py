def solution(phone_number):
    answer = '*'* len(phone_number[:-4]) + phone_number[-4:]
    print(answer)
    return answer

solution('01011112222')