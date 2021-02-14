N, K = map(int, input().split())
A = [list(map(int, input().split())) for j in range(N)]
mod = 10 ** 9 + 7
ans = 0

def multi_mat(a,b):
    c = [[0 for j in range(N)] for i in range(N)]
    for k in range(N):
        for j in range(N):
            for i in range(N):
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % mod
    return c

def matrix_pow(a, n):
    res = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        res[i][i] = 1
    
    while n:
        if n & 1:
            res = multi_mat(res, a)
        a = multi_mat(a, a)
        n >>= 1
    return res

res = matrix_pow(A, K)

for i in range(N):
    ans += sum(res[i]) % mod
print(ans%mod)