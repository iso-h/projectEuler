def primeFactors(unfactored):
	print(unfactored)
	for x in range(1, unfactored):
		if unfactored % x == 0:
			print(x)

primeFactors(600851475143)
