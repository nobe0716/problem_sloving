for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    dx, dy = x2 - x1, y2 - y1

    r = dx * dy + 1
    print(r)
