a = int(input())
b = int(input())
c = a / b
if b == 0:
    print('НА 0 ДЕЛИТЬ НЕЛЬЗЯ') 
elif a % b == 0:
    print(f'Можно {c}')
else:
    print(f'Нельзя {c}')
