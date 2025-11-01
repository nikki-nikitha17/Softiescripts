from collections import deque

def chairs_needed(orders):
    orders_sorted = sorted(orders, key=lambda x: x[0])
    n = len(orders_sorted)
    i = 0
    time = 0
    vip_q = deque()
    norm_q = deque()
    max_chairs = 0

    while i < n or vip_q or norm_q:
        if not vip_q and not norm_q:
          
            time = max(time, orders_sorted[i][0])
            a = orders_sorted[i][0]
            same = []
            while i < n and orders_sorted[i][0] == a:
                same.append(orders_sorted[i])
                i += 1
    
            vips = sorted([o for o in same if o[2] == 1], key=lambda x: x[1])
            norms = sorted([o for o in same if o[2] == 0], key=lambda x: x[1])
            for o in vips: vip_q.append(o)
            for o in norms: norm_q.append(o)

            job = vip_q.popleft() if vip_q else norm_q.popleft()
            waiting = len(vip_q) + len(norm_q)
            max_chairs = max(max_chairs, waiting)

            start = time
            finish = start + job[1]

            while i < n and orders_sorted[i][0] < finish:
                a = orders_sorted[i][0]
                same = []
                while i < n and orders_sorted[i][0] == a:
                    same.append(orders_sorted[i])
                    i += 1
                vips = sorted([o for o in same if o[2] == 1], key=lambda x: x[1])
                norms = sorted([o for o in same if o[2] == 0], key=lambda x: x[1])
                for o in vips: vip_q.append(o)
                for o in norms: norm_q.append(o)
                waiting = len(vip_q) + len(norm_q)
                max_chairs = max(max_chairs, waiting)

            time = finish

        else:
            job = vip_q.popleft() if vip_q else norm_q.popleft()
            waiting = len(vip_q) + len(norm_q)
            max_chairs = max(max_chairs, waiting)

            start = time
            finish = start + job[1]

            while i < n and orders_sorted[i][0] < finish:
                a = orders_sorted[i][0]
                same = []
                while i < n and orders_sorted[i][0] == a:
                    same.append(orders_sorted[i])
                    i += 1
                vips = sorted([o for o in same if o[2] == 1], key=lambda x: x[1])
                norms = sorted([o for o in same if o[2] == 0], key=lambda x: x[1])
                for o in vips: vip_q.append(o)
                for o in norms: norm_q.append(o)
                waiting = len(vip_q) + len(norm_q)
                max_chairs = max(max_chairs, waiting)

            time = finish

    return max_chairs


n = int(input())
orders = [tuple(map(int, input().split())) for _ in range(n)]
print(chairs_needed(orders))
