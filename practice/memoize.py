def memoize(func):
    cache = {}
    def wrapped(n):
        if n in cache:
            return cache[n]
        cache[n] = func(n)
        return cache[n]
    return wrapped

@memoize
def fib(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)
