def sum(x, y):
    return x, y


def specialize(func, *args, **kwargs):
    def f(*add_args, **add_kwargs):
        return func(*args, *add_args, **kwargs, **add_kwargs)

    return f


plus_one = specialize(sum, y=1)
print(plus_one(10))

just_two = specialize(sum, 1, 1)
print(just_two())
