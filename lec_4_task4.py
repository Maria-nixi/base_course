def final_func(a: float, b: int=0, c=1, *args, **kwargs):
    print(f'a: {a}, b: {b}, c: {c}')
    print(f'args: {args}, kwargs: {kwargs} \n')
    return 'done'

final_func(1)
final_func(1, 'Good', 4)
final_func(1, 2, 4, 5)
final_func(1, 2, 4, 5, 1, 2, 4, 5)
final_func(1, red=0, green=1, blue=0)
final_func(1, 2, 4, 5, 1, red=0, green=1, blue=0)

def E_polnaia(m: float, h: int=0, v: float=0, g=10, *args, **kwargs):
    E_p = m * g * h + (m * (v ** 2) / 2) 
    print(f'm: {m}, h: {h}, v: {v}')
    print(f'args: {args}, kwargs: {kwargs} ')
    print(E_p)
    return 'done'
E_polnaia(4, 2, 5, 80, 9000, red=0, green=1, blue=0)

def plohad(pi=3.14, ):
    if 