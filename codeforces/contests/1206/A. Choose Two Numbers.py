n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

for i in a:
    for j in b:
        if (i + j) not in a and (i + j) not in b:
            print(i, j)
            exit(0)
