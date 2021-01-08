N = int(input())
H = list(map(int, input().split()))
A = list(map(int, input().split()))
n = 1 << N.bit_length()
dat = [0 for i in range(2 * n - 1)]

def set_value(i, x):
    i += n - 1 # offset
    dat[i] = x
    while i >= 0:
        if dat[i] < x:
            dat[i] = x
        i = (i - 1) // 2

def get_max(i):
    i += n - 1
    ret = dat[i]
    while i > 0:
        # iが右の枝なら左の木と比較．
        if i % 2 == 0:
            ret = max(ret, dat[i - 1])
        i = (i - 1) // 2
    return ret

# ソートして高さを無視できるように．
srt = sorted((h, i) for i, h in enumerate(H))
for h, i in srt:
    set_value(i, get_max(i) + A[i])
print(dat[0])