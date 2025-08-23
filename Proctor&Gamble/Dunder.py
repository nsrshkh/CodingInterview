class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r})"

# Usage
p = Person("Alice", 30)
print(str(p))    # Alice is 30 years old.
print(repr(p))   # Person(name='Alice', age=30)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

# Usage
v1 = Vector(1, 2)
v2 = Vector(1, 2)
print(v1 == v2)         # True
print(hash(v1), hash(v2)) # Same value
s = {v1, v2}
print(len(s))           # 1


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

# Usage
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3.x, p3.y)  # 4 6

class MyList:
    def __init__(self, items):
        self.items = list(items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

# Usage
l = MyList([1, 2, 3])
print(len(l))     # 3
print(l[0])       # 1
l[1] = 5
print(l.items)    # [1, 5, 3]

class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

# Usage
for num in Counter(1, 3):
    print(num)  # 1 2 3


class MyContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")

# Usage
with MyContext():
    print("Inside context")
# Entering context
# Inside context
# Exiting context