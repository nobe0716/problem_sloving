import sys
from collections import defaultdict, deque
from typing import List, Tuple

input = sys.stdin.readline


def solve(n: int, edges: Tuple[List[int]], traverse: List[int]):
    if traverse[0] != 1:
        return False

    g = defaultdict(set)
    for a, b in edges:
        g[a].add(b)
        g[b].add(a)

    q = deque([1])
    head = 1
    for i in range(1, len(traverse)):
        e = traverse[i]
        if e not in g[head]:
            return False

        g[head].discard(e)
        g[e].discard(head)
        q.append(e)

        while q and not g[head]:
            head = q.popleft()
    return True


# assert solve(4, [[1, 2], [1, 3], [2, 4]], [1, 2, 3, 4])
# assert not solve(4, [[1, 2], [1, 3], [2, 4]], [1, 2, 4, 3])

n = int(input())
edges = []
for _ in range(n - 1):
    a, b = map(int, input().split())
    edges.append((a, b))
traverse = list(map(int, input().split()))
r = solve(n, edges, traverse)
print('Yes' if r else 'No')
