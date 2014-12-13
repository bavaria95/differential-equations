def shift(a):
    return a[-1 :] + a[: -1]

A = []
n = 4

a = [1] + [0 for i in range(n - 1)]
A.append(a)

a = [1, -2, 1] + [0 for i in range(n - 3)]

for i in range(n - 2):
    A.append(a)
    a = shift(a)

a = [0 for i in range(n - 2)] + [-1, 1]
A.append(a)

A[0] = [float(k/A[0][0]) for k in A[0]]


for i in range(1, n ):
	A[i] = [A[i][j] - float(A[i  - 1][j]*A[i][i - 1]) for j in range(n)]
	d = float(A[i][i])
	A[i] = [k/d for k in A[i]]

A = [[round(e, 3) for e in l] for l in A]

print A
