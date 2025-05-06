def a_k_generator(n):
    a = [1, 1, 1]
    for k in range(1, n + 1):
        if k <= 3:
            yield a[k - 1]
        else:
            next_a = a[-1] + a[-3]
            a.append(next_a)
            yield next_a

def calculate_S_n(n):
    if n < 1:
        return 0

    S = 0.0
    a_prev3 = 1
    a_prev2 = 1
    a_prev1 = 1

    for k in range(1, n + 1):
        if k <= 3:
            a_k = 1
        else:
            a_k = a_prev1 + a_prev3
            a_prev3, a_prev2, a_prev1 = a_prev2, a_prev1, a_k

        S += a_k / (2 ** k)

    return S

n_values = [1, 2, 3, 4, 5, 6, 7, 8]
print("\nЗадача d:")
for n in n_values:
    print(f"S_{n} = {calculate_S_n(n)}")