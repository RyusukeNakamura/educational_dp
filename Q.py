N = int(input())
H = list(map(int, input().split()))
A = list(map(int, input().split()))
bit = [0 for i in range(N + 1)]

def set_value(i, x):
    while i <= N:
        bit[i] = max(bit[i], x)
        i += i & -i

def get_max(i):
    ret = 0
    while i > 0:
        ret = max(ret, bit[i])
        i -= i & -i
    return ret

for i in range(N):
    mx = get_max(H[i])
    set_value(H[i], mx + A[i])
print(max(bit))