def func_step(a, n):
    a_n = 1
    for _ in range(n):
        a_n *= a
    return a_n 
    
print(func_step(2, 8))