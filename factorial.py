def memoize(func):
    cache = {}
    def wrapper(num):
        if num in cache:
            return cache[num]
        cache[num] = func(num)
        return cache[num]
    return wrapper
@memoize
def factorial_recursive(num):
    return num*factorial_recursive(num-1) if num>1 else 1

print(factorial_recursive(10))