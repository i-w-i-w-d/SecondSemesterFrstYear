def gen1_finite(x, n):
    for k in range(n + 1):
        numerator = 1
        for i in range(1, 2 * k + 2):
            numerator *= x
        denominator = 1
        for i in range(1, 2 * k + 2):
            denominator *= i
        yield numerator / denominator

def gen1_infinite(x):
    k = 0
    while True:
        numerator = 1
        for i in range(1, 2 * k + 2):
            numerator *= x
        denominator = 1
        for i in range(1, 2 * k + 2):
            denominator *= i
        yield numerator / denominator
        k += 1

def gen2_finite(x, n):
    for k in range(1, n + 1):
        sign = -1 if k % 2 else 1
        xk_power = 1
        for i in range(1, k + 1):
            xk_power *= x
        yield sign * xk_power / k

def gen2_infinite(x):
    k = 1
    while True:
        sign = -1 if k % 2 else 1
        xk_power = 1
        for i in range(1, k + 1):
            xk_power *= x
        yield sign * xk_power / k
        k += 1

def gen3_finite(x, n):
    for k in range(n + 1):
        sign = -1 if k % 2 else 1
        xk_power = 1
        for i in range(1, k + 1):
            xk_power *= x
        factorial = 1
        for i in range(1, k * k + k + 2):
            factorial *= i
        yield sign * xk_power / factorial

def gen3_infinite(x):
    k = 0
    while True:
        sign = -1 if k % 2 else 1
        xk_power = 1
        for i in range(1, k + 1):
            xk_power *= x
        factorial = 1
        for i in range(1, k * k + k + 2):
            factorial *= i
        yield sign * xk_power / factorial
        k += 1

def gen4_finite(x, n):
    for k in range(n + 1):
        xk_power = 1
        for i in range(1, k + 1):
            xk_power *= x
        factorial = 1
        for i in range(1, k + 1):
            factorial *= i
        yield (k + 1) * xk_power / factorial

def gen4_infinite(x):
    k = 0
    while True:
        xk_power = 1
        for i in range(1, k + 1):
            xk_power *= x
        factorial = 1
        for i in range(1, k + 1):
            factorial *= i
        yield (k + 1) * xk_power / factorial
        k += 1

if __name__ == "__main__":
    x = float(input("x = "))
    k = int(input("k = "))

    print("\nГенератор 1 (скінченний):")
    for i, val in enumerate(gen1_finite(x, k)):
        print(f"x_{i} = {val}")

    print("\nГенератор 2 (скінченний):")
    for i, val in enumerate(gen2_finite(x, k), 1):
        print(f"x_{i} = {val}")

    print("\nГенератор 3 (скінченний):")
    for i, val in enumerate(gen3_finite(x, k)):
        print(f"x_{i} = {val}")

    print("\nГенератор 4 (скінченний):")
    for i, val in enumerate(gen4_finite(x, k)):
        print(f"x_{i} = {val}")

    print("\nГенератор 1 (нескінченний):")
    inf_gen = gen1_infinite(x)
    for i in range(k + 1):
        print(f"x_{i} = {next(inf_gen)}")

    print("\nГенератор 2 (нескінченний):")
    inf_gen = gen2_infinite(x)
    for i in range(1, k + 1):
        print(f"x_{i} = {next(inf_gen)}")

    print("\nГенератор 3 (нескінченний):")
    inf_gen = gen3_infinite(x)
    for i in range(1, k + 1):
        print(f"x_{i} = {next(inf_gen)}")

    print("\nГенератор 4 (нескінченний):")
    inf_gen = gen4_infinite(x)
    for i in range(1, k + 1):
        print(f"x_{i} = {next(inf_gen)}")