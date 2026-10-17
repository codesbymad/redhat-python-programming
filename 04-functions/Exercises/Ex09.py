# Re-write your solution to Exercise 8 such that the outer function receives no parameters, and the nested function is defined as taking the two parameters.

def outer():
    def inner(x, y):
        return x + y

    return inner

f = outer()
print(f"O valor do retorno é {f(9, 3)}")
print(f"O valor do retorno é {f(9, 12)}")