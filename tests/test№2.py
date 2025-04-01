class rational:
    def __init__(self, n, d=1):
        self.n = n
        if d == 0:
            raise ValueError("Знаменник не має дорівнювати 0")
        self.d = d

    def __str__(self):
        return f"{self.n}/{self.d}"

    def __add__(self, other):
        d = self.d * other.d
        n = self.n * other.d + self.d * other.n
        return rational(n, d)

    def __mul__(self, other):
        n = self.n * other.n
        d = self.d * other.d
        return rational(n, d)

x = rational(2, 3) + rational(5) * rational(5, 6)
print(x)