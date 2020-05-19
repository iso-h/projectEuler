def main():
	biggestPalendrome = 0

	for i in range(100,1000):
		for j in range(100,1000):
			if is_Palendrome(i * j) and i * j > biggestPalendrome:
				biggestPalendrome = i * j

	print(biggestPalendrome)

def is_Palendrome(palLead):
	palLead = str(palLead)

	if palLead == palLead[::-1]:
		return 1

main()			
