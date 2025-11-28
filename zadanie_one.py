
g = 10
def my_func(m, h, v):
    E_k = (m * v ** 2) / 2
    E_p = m * g * h
    E_poln = E_k + E_p
    return E_poln 
print(my_func(3, 4, 5))

