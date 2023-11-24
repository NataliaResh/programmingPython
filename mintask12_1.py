def cycle(iterable):
    while True:
        yield from iterable


def take(seq, n):
    res = []
    for _ in range(n):
        try:
            res.append(next(seq))
        except StopIteration:
            break
    return res


print(take(cycle([1, 2, 3]), 10))
