from collections import deque

H, W = map(int, input().split())
A = [list(input()) for j in range(H)]

deq = deque()
deq.append((0, 0))
ans = 0
mod = 10**9 + 7

di = (0, 1)
dj = (1, 0)

for _ in range(10**10):
    (i, j) = deq.popleft()

    if (i, j) == (H-1, W-1):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
        ans += 1
    
    for k in range(2):
        y = i + di[k]
        x = j + dj[k]
        
        if y != H and x != W and A[y][x] != '#':
            deq.append((y, x))
    
    if not deq:
        break