n = int(input())
a = list(map(int, input().split()))
c = 0
pn = 0
mn = 0
zn = 0
for e in a:
    if e == 0:
        zn += 1
        continue

    if e > 0:
        c += (e - 1)
        pn += 1
    elif e < 0:
        c += (-e - 1)
        mn += 1

if mn % 2 == 1 and zn == 0:
    c += 2
else:
    c += zn
print(c)
