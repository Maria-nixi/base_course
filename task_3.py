year = int(input())
a = year % 4 == 0
b = year % 100 == 0
c = year % 400 == 0
if a:
    print(f'{year} - високостный')
elif b and c:
    print(f'{year} - високостный')
elif c:
    print(f'{year} - високостный')
else:
    print(f'{year} - не високостный')