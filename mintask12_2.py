def chain(*iterables):
    for iterable in iterables:
        yield from iterable


def take(seq, n):
    res = []
    for _ in range(n):
        try:
            res.append(next(seq))
        except StopIteration:
            break
    return res


my_list = [42, 13, 7]
print(list(chain([1, 2, 3], ['a', 'b'], my_list)))
