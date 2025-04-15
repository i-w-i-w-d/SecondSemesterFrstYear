def seq_b(n):
    p = 1/2
    a = 2
    for i in range(2, n + 1):
        a *= (i + 1)
        p *= 1/a
    return p

print(seq_b(4))