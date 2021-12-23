def solution(a, b):
    array = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    days = 0

    for m in range(0,a-1):
        days += month[m]
    days += b
    return array[days%7-1]