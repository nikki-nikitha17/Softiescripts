import math
from collections import defaultdict, deque

def find_center(x1, y1, x2, y2):
    return ((x1 + x2) / 2, (y1 + y2) / 2)

def chebyshev(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))

def min_stars():
    n = int(input().strip())
    lines = [tuple(map(int, input().split())) for _ in range(n)]
    sx, sy = map(int, input().split())
    dx, dy = map(int, input().split())

    centers = []
    for i in range(n):
        x1, y1, x2, y2 = lines[i]
        centers.append(find_center(x1, y1, x2, y2))

    graph = defaultdict(set)
    for i in range(len(centers)):
        for j in range(i + 1, len(centers)):
            if chebyshev(centers[i], centers[j]) <= 5:
                graph[i].add(j)
                graph[j].add(i)

    def find_nearest_star(x, y):
        dmin, idx = float('inf'), -1
        for i, c in enumerate(centers):
            d = chebyshev(c, (x, y))
            if d < dmin:
                dmin, idx = d, i
        return idx

    s_idx = find_nearest_star(sx, sy)
    d_idx = find_nearest_star(dx, dy)

    q = deque([(s_idx, 1)])
    visited = {s_idx}
    while q:
        node, dist = q.popleft()
        if node == d_idx:
            print(dist)
            return
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append((nei, dist + 1))

    min_shift = math.ceil(chebyshev(centers[d_idx], (dx, dy)))
    print(min_shift)

min_stars()
