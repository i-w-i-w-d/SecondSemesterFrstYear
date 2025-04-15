def finite_alternating_sum(n):
    total = 0
    sign = 1
    for i in range(1, n + 1):
        total += sign * i
        sign *= -1
        yield total

def infinite_alternating_sum():
    total = 0
    sign = 1
    i = 1
    while True:
        total += sign * i
        sign *= -1
        yield total
        i += 1

def finite_fraction_sum(n):
    total = 0
    for i in range(1, n):
        denominator = i * (i + 1)
        total += 1 / denominator
        yield total

def infinite_fraction_sum():
    total = 0
    i = 1
    while True:
        denominator = i * (i + 1)
        total += 1 / denominator
        yield total
        i += 1

def finite_alternating_fraction_sum(n):
    total = 0
    sign = 1
    for i in range(2, n + 1):
        total += sign * (i - 1) / i
        sign *= -1
        yield total

def infinite_alternating_fraction_sum():
    total = 0
    sign = 1
    i = 2
    while True:
        total += sign * (i - 1) / i
        sign *= -1
        yield total
        i += 1

if __name__ == "__main__":
    n = 5

    print("Генератор 1 (скінченний):")
    print(*finite_alternating_sum(n))

    print("\nГенератор 2 (скінченний):")
    print(*[f"{x:.4f}" for x in finite_fraction_sum(n)])

    print("\nГенератор 3 (скінченний):")
    print(*[f"{x:.4f}" for x in finite_alternating_fraction_sum(n)])

    print("\nГенератор 1 (нескінченний):")
    print(*[next(infinite_alternating_sum()) for _ in range(n)])

    print("\nГенератор 2 (нескінченний):")
    print(*[f"{next(infinite_fraction_sum()):.4f}" for _ in range(n-1)])

    print("\nГенератор 3 (нескінченний):")
    print(*[f"{next(infinite_alternating_fraction_sum()):.4f}" for _ in range(n-1)])