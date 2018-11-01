def SumSquare():
	j = 0
	l = 0
	for i in range(1, 101):
		j = j + (i*i)
	for k in range(1, 101):
		l = l + k
	l = l * l
	m = l - j
	print(m)

SumSquare()
