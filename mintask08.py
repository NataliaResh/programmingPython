from functools import partial, wraps


def deprecated(f=None, *, since=None, will_be_removed=None):
    if f is None:
        return partial(deprecated, since=since, will_be_removed=will_be_removed)

    @wraps(f)
    def inner(*args, **kwargs):
        warning_deprecated = f"Warning: function {inner.__name__} is deprecated"
        if since:
            warning_deprecated += f" since version {since}"
        warning_removed = f"It will be removed in "
        if will_be_removed:
            warning_removed += f"version {will_be_removed}"
        else:
            warning_removed += f"future versions"
        print(f"{warning_deprecated}. {warning_removed}.")
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