def finite_product_squares(n):
    product = 1
    for i in range(2, n + 1):
        term = 1 - 1 / (i * i)
        product *= term
        yield product

def infinite_product_squares():
    product = 1
    i = 2
    while True:
        term = 1 - 1 / (i * i)
        product *= term
        yield product
        i += 1

def finite_product_factorials(n):
    product = 1
    for i in range(1, n + 1):
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        term = 2 + 1 / factorial
        product *= term
        yield product

def infinite_product_factorials():
    product = 1
    i = 1
    factorial = 1
    while True:
        term = 2 + 1 / factorial
        product *= term
        yield product
        i += 1
        factorial *= i

def finite_product_fractions(n):
    product = 1
    for i in range(1, n + 1):
        term = (i + 1) / (i + 2)
        product *= term
        yield product

def infinite_product_fractions():
    product = 1
    i = 1
    while True:
        term = (i + 1) / (i + 2)
        product *= term
        yield product
        i += 1

if __name__ == "__main__":
    n = 5

    print("Генератор 1 (скінченний):")
    for p in finite_product_squares(n):
        print(f"{p:.6f}", end=" ")

    print("\n\nГенератор 2 (скінченний):")
    for p in finite_product_factorials(n):
        print(f"{p:.6f}", end=" ")

    print("\n\nГенератор 3 (скінченний):")
    for p in finite_product_fractions(n):
        print(f"{p:.6f}", end=" ")

    print("\n\nГенератор 1 (нескінченний):")
    gen = infinite_product_squares()
    for _ in range(n - 1):
        print(f"{next(gen):.6f}", end=" ")

    print("\n\nГенератор 2 (нескінченний):")
    gen = infinite_product_factorials()
    for _ in range(n):
        print(f"{next(gen):.6f}", end=" ")

    print("\n\nГенератор 3 (нескінченний):")
    gen = infinite_product_fractions()
    for _ in range(n):
        print(f"{next(gen):.6f}", end=" ")
    print()