n = int(input())

for a in range(1, n + 1):
    for b in range(1, a + 1):
        if a % b == 0 and a * b > n and a // b < n:
            print(a, b)
            exit()
print(-1)
