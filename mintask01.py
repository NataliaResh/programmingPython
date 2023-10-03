from math import ceil, log

n = int(input())
ans = 0
if n < 0:
    bits_count = ceil(log(abs(n) + 1, 2))
    n = (abs(n) ^ (2 ** bits_count - 1)) + 1
    ans += 1

while n > 0:
    ans += n & 1
    n = n >> 1
print(ans)
