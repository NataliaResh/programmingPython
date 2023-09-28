def bits_count(n):
    n = abs(n)
    count = 0
    while n > 0:
        count += 1
        n = n >> 1
    return count


n = int(input())
ans = 0
if n < 0:
    n = (abs(n) ^ (2 ** bits_count(n) - 1)) + 1
    ans += 1

while abs(n) > 0:
    ans += n & 1
    n = n >> 1
print(ans)