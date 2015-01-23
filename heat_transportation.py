import numpy as np
import matplotlib.pyplot as plt

def k(x):
	if x <= 1: return 1
	else: return 2

def gaussian(a):
	n = len(a)
	for k in range(1, n):
		for j in range(k, n):
			m = a[j][k - 1] / float(a[k - 1][k - 1])
			for i in range(0, n + 1):
				a[j][i] = a[j][i] - m*a[k - 1][i]

	x = [0] * n
	for i in range(n - 1, -1, -1):
		for j in range(i + 1, n):
			x[i] += a[i][j] * x[j]
		x[i] = (a[i][n] - x[i]) / float(a[i][i])

	return x

def create_matrix(n):
	a = []
	left = 0.0
	right = 2.0
	h = (right - left) / n
	a.append([h - 1, 1] + [0]*(n - 1) + [h])
	x = left + h
	i = 1
	for i in range(1, n):
		tmp = [0]*(i - 1) + [k(x), -(k(x) + k(x + h)), k(x + h)] + [0]*(n - i - 1) + [0]
		a.append(tmp)
		x += h
	a.append([0]*n + [1] + [0])
	return a, h


a, h = create_matrix(3)
x = gaussian(a)

x = np.array(x)
t = np.arange(0., 2 + h/2, h)
# print x.shape, t.shape

plt.plot(t, x)
plt.show()

