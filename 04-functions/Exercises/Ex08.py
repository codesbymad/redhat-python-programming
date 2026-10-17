'''Write a function that returns a nested function.

When the nested function is executed it should return the sum of two integers.

The two parameters should be passed to the outer function and used by the inner function.'''

def outer(x, y):
    def inner():
        return x + y

    return inner

f = outer(9, 3)
print(f"O valor do retorno é {f()}")