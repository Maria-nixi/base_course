import functools
import match


def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs) :
        args_repr = [str(a) for a in args]
        kwargs_repr = [f"{k}={v}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print (f"Вызываем функцию {func.name} ({signature})")
        value - func(*args, **kwargs)
        print (f"Функцию {func.__name_} вернула значение {value}")
        return value
    

debug_factorial = debug(math.factorial)
# @debug
# def debug_factorial():
    return math.factorial

def show_debug_function(terms=5):
    return [debug_factorial(n) for n in range(terms+1)]
TrU
show_debug_function(7)