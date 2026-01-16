
def mat_func(a, b, x, y):
    if a < x < b:
        y = x ** 4
        return x, y

print(mat_func(5, 90, 6, 3))