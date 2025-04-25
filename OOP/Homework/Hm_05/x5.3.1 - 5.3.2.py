class Rational:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            parts = args[0].split('/')
            if len(parts) == 1:
                n = int(parts[0])
                d = 1
            else:
                n = int(parts[0])
                d = int(parts[1])
        elif len(args) == 2:
            n, d = args
        elif len(args) == 1 and isinstance(args[0], (int, Rational)):
            if isinstance(args[0], int):
                n = args[0]
                d = 1
            else:
                n = args[0].n
                d = args[0].d
        else:
            raise ValueError("Value error")
        if d == 0:
            raise ZeroDivisionError("Zero division")
        gcd_val = self._gcd(abs(n), abs(d))
        self.n = n // gcd_val
        self.d = d // gcd_val
        if self.d < 0:
            self.n *= -1
            self.d *= -1

    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            return NotImplemented
        new_n = self.n * other.d + other.n * self.d
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            return NotImplemented
        new_n = self.n * other.d - other.n * self.d
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __rsub__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            return NotImplemented
        return other.__sub__(self)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            return NotImplemented
        new_n = self.n * other.n
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            return NotImplemented
        if other.n == 0:
            raise ZeroDivisionError("Zero division")
        new_n = self.n * other.d
        new_d = self.d * other.n
        return Rational(new_n, new_d)

    def __rtruediv__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            return NotImplemented
        return other.__truediv__(self)

    def __call__(self):
        return self.n / self.d

    def __getitem__(self, key):
        if key == "n":
            return self.n
        elif key == "d":
            return self.d
        else:
            raise KeyError("Key error")

    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise ValueError("Value error")
        if key == "n":
            gcd_val = self._gcd(abs(value), abs(self.d))
            self.n = value // gcd_val
            self.d = self.d // gcd_val
        elif key == "d":
            if value == 0:
                raise ZeroDivisionError("Zero division")
            gcd_val = self._gcd(abs(self.n), abs(value))
            self.n = self.n // gcd_val
            self.d = value // gcd_val
        else:
            raise KeyError("Key error")
        if self.d < 0:
            self.n *= -1
            self.d *= -1

    def __str__(self):
        if self.d == 1:
            return str(self.n)
        return f"{self.n}/{self.d}"

    def __repr__(self):
        return f"Rational({self.n}, {self.d})"

class RationalList:
    def __init__(self, data=None):
        self.data = []
        if data is not None:
            for item in data:
                self.append(item)

    def append(self, item):
        if isinstance(item, (int, Rational)):
            self.data.append(Rational(item))
        else:
            raise TypeError("Type error")

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        if isinstance(value, (int, Rational)):
            self.data[index] = Rational(value)
        else:
            raise TypeError("Type error")

    def __len__(self):
        return len(self.data)

    def __add__(self, other):
        if isinstance(other, RationalList):
            new_list = RationalList(self.data)
            new_list.data.extend(other.data)
            return new_list
        elif isinstance(other, (int, Rational)):
            new_list = RationalList(self.data)
            new_list.append(other)
            return new_list
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, (int, Rational)):
            new_list = RationalList([other])
            new_list.data.extend(self.data)
            return new_list
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self.data.extend(other.data)
        elif isinstance(other, (int, Rational)):
            self.append(other)
        else:
            return NotImplemented
        return self

    def __str__(self):
        return str([str(item) for item in self.data])

    def __repr__(self):
        return repr(self.data)

def evaluate_expression(expr):
    tokens = expr.split()
    if not tokens:
        return Rational(0)

    result = Rational(tokens[0])
    i = 1
    while i < len(tokens):
        token = tokens[i]
        if token in ('+', '-', '*', '/'):
            right = Rational(tokens[i + 1])
            if token == '+':
                result += right
            elif token == '-':
                result -= right
            elif token == '*':
                result *= right
            elif token == '/':
                result /= right
            i += 2
        else:
            i += 1
    return result


def process_file(filename):
    results = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    result = evaluate_expression(line)
                    results.append(result)
                except Exception as e:
                    print(f"Error, can not do that :( '{line}': {e}")
    return results

def sum_rational_list(numbers):
    total = Rational(0)
    for num in numbers:
        total += num
    return total

input_file = "input01.txt"
results = process_file(input_file)
print("Результати:")
for res in results:
    print(res)

numbers_file = "numbers.txt"
rational_list = RationalList()
with open(numbers_file, 'r') as f:
    for line in f:
        tokens = line.split()
        for token in tokens:
            rational_list.append(Rational(token))

total_sum = sum_rational_list(rational_list)
print(f"\nСума чисел: {total_sum}")