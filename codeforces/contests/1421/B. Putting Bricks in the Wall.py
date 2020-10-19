def solve(n, grid):
    pos = []
    if grid[0][1] == grid[1][0]:
        if grid[n - 1][n - 2] == grid[0][1]:
            pos.append((n - 1, n - 2))
        if grid[n - 2][n - 1] == grid[0][1]:
            pos.append((n - 2, n - 1))
    elif grid[n - 1][n - 2] == grid[n - 2][n - 1]:
        if grid[0][1] == grid[n - 1][n - 2]:
            pos.append((0, 1))
        if grid[1][0] == grid[n - 1][n - 2]:
            pos.append((1, 0))
    elif grid[0][1] == grid[n - 2][n - 1] and grid[1][0] == grid[n - 1][n - 2]:
        pos.append((0, 1))
        pos.append((n - 1, n - 2))
    else:
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        def is_valid(x, y, visited):
            if x == 0 and y == 0:
                return True
            elif x < 0 or y < 0 or x >= n or y >= n:
                return False
            for _ in range(4):
                nx, ny = x + dx[_], y + dy[_]
                if (nx, ny) in visited:
                    continue
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if nx == 0 and ny == 0:
                    return True
                if grid[x][y] != grid[nx][ny]:
                    continue

                visited.add((nx, ny))
                if is_valid(nx, ny, visited):
                    return True
                visited.discard((nx, ny))
            return False

        if is_valid(n - 1, n - 2, set()):
            pos.append((n - 1, n - 2))
            pos.append((1, 0))
        if is_valid(n - 2, n - 1, set()):
            pos.append((n - 2, n - 1))
            pos.append((0, 1))

    res = []
    for x, y in pos:
        res.append((x + 1, y + 1))
    return res


t = int(input())
for _ in range(t):
    n = int(input())
    g = [input() for _ in range(n)]
    pos = solve(n, g)
    if not pos:
        print(0)
    else:
        print(len(pos))
        print('\n'.join('{} {}'.format(_[0], _[1]) for _ in pos))
