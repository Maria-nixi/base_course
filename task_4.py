'''sp = []
n = int(input())
for _ in range(n):
    sp += [int(input())]

k = int(input())
for i in range(len(sp) - 1):
    if sp[i] % 10 == 0 and sp[i + 1] % 10 == k:
        print(sp[i], sp[i + 1])'''

n = int(input())
sp = []
c = 0
c1 = 1
for i in range(n + 1):
    sp.append(i)
for _ in range(n + 1):
    sm, sm1 = sp[c], sp[c1]
    print(sm, sm1)
    c += 1
    c1 += 1