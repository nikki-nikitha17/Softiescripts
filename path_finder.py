import heapq
import sys
def main():
    input=sys.stdin.read
    data=input().split()
    index=0
    n=int(data[index]);index+=1
    m=int(data[index]);index+=1
    grid=[]
    for i in range(n):
        row=[]
        for j in range(m):
            row.append(int(data[index]));index+=1
        grid.append(row)
    sx=int(data[index])-1;index+=1
    sy=int(data[index])-1;index+=1
    dx=int(data[index])-1;index+=1
    dy=int(data[index])-1;index+=1
    k=int(data[index]);index+=1
    blocked_set=set()
    for _ in range(k):
        bx=int(data[index])-1;index+=1
        by=int(data[index])-1;index+=1
        blocked_set.add((bx,by))
    def in_bounds(x, y, n, m):
        return 0 <= x < n and 0 <= y < m
    directions=[(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    dist=[[float('inf')] * m for _ in range(n)]
    dist[sx][sy]=0
    pq=[(0,sx,sy)]
    while pq:
        cost,x,y = heapq.heappop(pq)
        if cost>dist[x][y]:
            continue
        if x == dx and y == dy:
            print(cost)
            return
        neigh = []
        for dx_, dy_ in directions:
            nx=x+dx_
            ny=y+dy_
            if in_bounds(nx,ny,n,m) and (nx,ny) not in blocked_set:
                neigh.append((nx,ny,grid[nx][ny]))
        if not neigh:
            continue
        max_all=max(v for _, _, v in neigh)
        current_val=grid[x][y]
        for tx,ty,vt in neigh:
            other_vals=[v for px,py,v in neigh if (px, py) != (tx, ty)]
            max_other=max(other_vals) if other_vals else -10**9 - 1
            if current_val>=max_all:
                added=current_val+1-vt
            else:
                added=(max_other+1 -vt) if other_vals else 0
            edge_cost=max(0,added)
            new_cost=cost+edge_cost
            if new_cost<dist[tx][ty]:
                dist[tx][ty] =new_cost
                heapq.heappush(pq, (new_cost,tx,ty))
    print(-1 if dist[dx][dy] == float('inf') else dist[dx][dy])

if __name__ == "__main__":
    main()