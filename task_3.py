year = int(input())
a = year % 4 == 0
b = year % 100 == 0
c = year % 400 == 0
if a and (b and c):
    print(f'{year} - високостный')
else:
    print(f'{year} - не високостный')