def fat(x):
    ans = x
    while (x > 2):
        x -= 1
        ans *= x
    return ans

fatoriais = {x: fat(x) for x in range(1, 11)}
print(fatoriais)
print(fatoriais[6] * fatoriais[5])