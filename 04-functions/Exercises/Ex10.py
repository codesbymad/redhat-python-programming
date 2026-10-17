# Re-write your solution to either Exercise 8 or 9 so that it uses a lambda expression as the nested function.

def outer():
        return lambda x, y: x + y

f = outer()
print(f"O valor do retorno é {f(9, 3)}")
print(f"O valor do retorno é {f(9, 12)}")