'''
if <условие прерывания>:
    break

if <условие пропуска>:
    continue
'''

for i in 'hello world':
    if i == 'o':
        break
    print(i)

for i in 'hello world':
    if i == 'o':
        continue
    print(i)