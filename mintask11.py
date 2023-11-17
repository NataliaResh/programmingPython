def _fake_init(*args, **kwargs):
    return None


class Singleton:
    obj = None

    def __new__(cls, *args, **kwargs):
        if not cls.obj:
            cls.obj = object.__new__(cls)
        else:
            cls.__init__ = _fake_init
        return cls.obj


class Counter:
    def __init__(self, initial_count=0, step=1):
        self.count = initial_count
        self.step = step


class GC(Singleton, Counter):
    pass


counter1 = GC(1, 2)
counter2 = GC(2, 4)
print(counter1.step)
print(counter2.step)
print(id(counter1) == id(counter2))
