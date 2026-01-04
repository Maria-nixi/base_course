# global - позволяет локально изменять глобальные переменные
counter = 0

def update(value):
    global counter
    result = counter + value

    print(f"{counter} + {value} = {result}")
    counter = result

update(1)
update(5)
update(3)

print(f"{counter = }")

#------------------------------------

# nonlocal - позволяет локально изменять переменные,
# находящиеся предшествующей локальной области видимости
counter = 0

def create_scope(default):
    counter = default * 2

    def nonlocal_print():
        nonlocal counter
        print(f"scoped {counter = }")

    def global_print():
        global counter
        print(f"global {counter = }")

    nonlocal_print()
    global_print()

create_scope(-4)