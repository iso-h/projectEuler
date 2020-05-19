def solveProblem():
	i = 1
	j = i
	sum = 0

	while True:
		j += i
		i = j - i
	
		if j < 4000000:
			if j % 2 == 0:
				sum += j
			
		else:
			break

	print(sum)
			

solveProblem()	
