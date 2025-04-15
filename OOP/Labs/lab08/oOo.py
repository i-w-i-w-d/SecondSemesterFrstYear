def det(n):
    if n == 1: yield 2
    if n == 2: yield 1
    d_prev_1 = 1
    d_prev_2 = 1
    for i in range(3, n + 1):
        d = 2 * d