'''
	Heat flux model with finite difference method
	'''

def shift(a):					 
    return a[-1 :] + a[: -1]

A = []
n = 4

a = [1] + [0]*(n - 1)
A.append(a)

a = [1, -2, 1] + [0]*(n - 3)

for i in range(n - 2):
    A.append(a)
    a = shift(a)

a = [0]*(n - 2) + [-1, 1]
A.append(a)

H = [0]*(n - 1) + [1]


'''
	Gaussian elimination
	'''

for i in range(n ):
	A[i] = [A[i][j] - float(A[i  - 1][j]*A[i][i - 1]) for j in range(n)]
	H[i] -= H[i - 1]*A[i][i - 1]
	d = float(A[i][i])
	A[i] = [k/d for k in A[i]]
	H[i] /= d

