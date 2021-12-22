# 나의 풀이
def solution(sizes):
    long_list  = []
    short_list = []
    for list in sizes:
        if list[0] < list[1]:
            long_list.append(list[1])
            short_list.append(list[0])
        else:
            long_list.append(list[0])
            short_list.append(list[1])
    return max(long_list) * max(short_list)

# 다른 풀이
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)


