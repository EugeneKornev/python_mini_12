def coroutine(f):
    def wrapper(*args, **kwargs):
        g = f(*args, **kwargs)
        next(g)
        return g

    return wrapper


def storage():
    values = set()
    was_there = False

    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)


def test():
    base_storage = storage
    improved_storage = coroutine(storage)
    try:
        st1 = base_storage()
        print(st1.send(42))
        print(st1.send(42))
    except TypeError:
        print("It doesn't work without coroutine")
    try:
        st2 = improved_storage()
        print(st2.send(42))
        print(st2.send(42))
    except TypeError:
        print("It doesn't work with coroutine")
    finally:
        print("It works with coroutine")


if __name__ == '__main__':
    test()

