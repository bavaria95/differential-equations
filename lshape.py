from math import *

def g(x, y):
	theta = atan2(y, x)
	sin2 = sin(theta + pi/4)**2

	return (x**2 + y**2)**(1/3) * sin2**(1/3)

def phi(Ek, i, x, y):
	if (i == 0):
		result = (1 - (x - S[Ek][0])) * (1 - (y - S[Ek][1]))
	elif (i == 1):
		result = (x - S[Ek][0]) * (1 - (y - S[Ek][1]))
	elif (i == 2):
		result = (x - S[Ek][0]) * (y - S[Ek][1])
	elif (i == 3):
		result = (1 - (x - S[Ek][0])) * (y - S[Ek][1])
	else:
		print('Something went wrong')

	return result


def derivativePhi(i, derByX):
	if ((i == 3) or (i == 2 and derByX) or (i == 4) and (not derByX)):
		return 0.5
	else:
		return -0.5 


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


def printB(B):
	for i in B:
		for j in i:
			print(j, end=' ')
		print()


B = [[0]*8 for i in range(8)]
L = [0]*8

Ek = [[4, 5, 2, 1], [5, 6, 3, 2], [7, 8, 6, 5]]
CP = [[[-1, 0.5], [-0.5, 1]], [[0.5, 1], [1, 0.5]], [[1, -0.5], [0.5, -1]]]			# center points
S = [[-1, 0], [0, 0], [0, -1]]				# B initial values

for k in range(3):			# quantity of elements
	for i in range(4):   # length of Ek
		for cp in CP[k]:
			L[Ek[k][i] - 1] += g(cp[0], cp[1]) * phi(k, i, cp[0], cp[1])

		for j in range(len(Ek[k])):
			derByX = derivativePhi(i + 1, True) * derivativePhi(j + 1, True)
			derByY = derivativePhi(i + 1, False) * derivativePhi(j + 1, False)

			B[Ek[k][i] - 1][Ek[k][j] - 1] += (derByX + derByY)

# setting up boundaries
for i in range(8):
		B[3][i], B[4][i], B[6][i] = 0, 0, 0
B[3][3], B[4][4], B[6][6] = 1, 1, 1

L[3], L[4], L[6] = 0, 0, 0

eq_matrix = [x + [y] for x, y in zip(B, L)]		# last column - L

for i in range(8):
	for j in range(8):
		print("% .2f" % B[i][j], end=' ', sep='')
	print('| ', L[i])

print()
uh = gaussian([x + [y] for x, y in zip(B, L)])

P = [[-1, 1], [0, 1], [1, 1], [-1, 0], [0, 0], [1, 0], [0, -1], [1, -1]]

for i in range(8):
	print("% d % d\t%f" % (P[i][0], P[i][1], uh[i]))

