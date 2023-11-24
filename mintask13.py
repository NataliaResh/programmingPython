from functools import wraps


def coroutine(gen):
    @wraps(gen)
    def inner(*args, **kwargs):
        rep = gen(*args, **kwargs)
        next(rep)
        return rep

    return inner


@coroutine
def storage():
    values = set()
    was_there = False

    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)


st = storage()
# next(st)
print(st.send(42))
print(st.send(42))
