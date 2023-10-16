from functools import partial, wraps


def deprecated(f=None, *, since=None, will_be_removed=None):
    if f is None:
        return partial(deprecated, since=since, will_be_removed=will_be_removed)

    @wraps(f)
    def inner(*args, **kwargs):
        if since and will_be_removed:
            print(
                f"Warning: function {inner.__name__} is deprecated since version {since}. It will be removed in version {will_be_removed}")
        elif since:
            print(
                f"Warning: function {inner.__name__} is deprecated since version {since}. It will be removed in future versions")
        elif will_be_removed:
            print(
                f"Warning: function {inner.__name__} is deprecated. It will be removed in version {will_be_removed}")
        else:
            print(
                f"Warning: function {inner.__name__} is deprecated. It will be removed in future versions")
        rep = f(*args, **kwargs)
        return rep

    return inner


@deprecated
def foo():
    print("Hello from foo!")


@deprecated(since="4.2.0", will_be_removed="5.0.1")
def bar():
    print("Hello from bar!")


foo()
bar()
