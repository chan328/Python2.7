def hap(x, y):
    return x + y
print(hap(10, 20))

print((lambda a, b: a + b)(10, 20))

print(map(lambda x : x ** 2, range(5)))

print(list(map(lambda x: x ** 2, range(5))))
