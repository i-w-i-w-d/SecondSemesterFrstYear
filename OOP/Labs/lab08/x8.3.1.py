def seq_o(x, n):
    result = [x]
    for k in range(2, n + 1):
        result.append(result[-1] * (x * (k - 1) / k))
    return result

print(seq_o(87, 32))

