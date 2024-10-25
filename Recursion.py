def fun(x):
    if x>100:
        return x-10
    return fun(fun(x+11))

print(fun(91))