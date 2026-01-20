year = int(input())
a = year % 4 == 0
b = year % 100 == 0
c = year % 400 == 0
s = (year % 100 // 10) == 0
s1 = (year % 100 % 10) == 0

if s and s1:
    if c and not b:
        print(f'{year} - високостный')
    else:
        print(f'{year} - не високостный')
else:
    if a:
        print(f'{year} - високостный')
    else:
        print(f'{year} - не високостный')
