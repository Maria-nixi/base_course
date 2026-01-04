# * - оператор распаковки кортежей

def compress(*values):
    return values


result = compress(1, 5, 7, 8, 9)
print("Compressed:", result)


def extract(value):
    print("Extracted: ", *value)


extract(result)

#------------------------------------------

# ** - оператор распаковки словарей

def parameters(**kwargs):
    print(kwargs)

parameters(first=1, second="two", something=False)


def discriminant(a, b, c):
    return b * b - 4 * a * c

polynom = {"a": 1, "b": 0, "c": 2}

print(f"{discriminant(**polynom) = }")