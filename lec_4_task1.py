
def E_polnaia(m: float, h: int=0, v: float=0, g=10, *args, **kwargs):
    E_p = m * g * h + (m * (v ** 2) / 2) 
    print(f'm: {m}, h: {h}, v: {v}')
    print(f'args: {args}, kwargs: {kwargs} ')
    print(E_p)
    return 'done'
E_polnaia(4, 2, 5, 80, 9000, red=0, green=1, blue=0)