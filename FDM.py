def shift(a):
    return a[-1:] + a[:-1]

A = []
n = 4
n -= 1

a = [1] + [0 for i in range(n)]
A.append(a)

a = [1, -2, 1] + [0 for i in range(n - 2)]

for i in range(n - 1):
    A.append(a)
    a = shift(a)

a = [0 for i in range(n - 1)] + [-1, 1]
A.append(a)


print A