def seq_d(n):
    a_prev_2 = 0
    a_prev_1 = 1
    s = 2 ** 1 * a_prev_2 + 2 ** 2 * a_prev_2
    for i in range(3, n + 1):
        a_current = a_prev_2 + i * a_prev_2
        s += 2 ** 1 * a_current
        a_prev_2, a_prev_1 = a_prev_1, a_current
        print(s, i)

    return s

print(seq_d(90))