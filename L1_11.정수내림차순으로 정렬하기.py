def solution(n):
    n_list = list(str(n))
    n_list.sort(reverse=True)
    n_int = int(''.join(n_list))
    return n_int