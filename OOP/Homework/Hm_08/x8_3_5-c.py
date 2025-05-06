def calculate_determinant(n, a, b):
    if n < 1:
        return 0
    elif n == 1:
        return a + b
    elif n == 2:
        return (a + b) ** 2 - a * b

    d_prev_prev = a + b
    d_prev = (a + b) ** 2 - a * b

    for i in range(3, n + 1):
        d_current = (a + b) * d_prev - a * b * d_prev_prev
        d_prev_prev, d_prev = d_prev, d_current

    return d_prev

a, b = 2, 3
n_values = [1, 2, 3, 4, 5]
print("\nЗадача c:")
print(f"a = {a}, b = {b}")
for n in n_values:
    print(f"D_{n} = {calculate_determinant(n, a, b)}")