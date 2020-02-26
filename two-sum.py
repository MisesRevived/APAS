nums = [2, 3, 5, 7]

def twosum(target):
	for num in nums: 
		for i in nums: 
			if num + i == target:
				firstNr = num
				secondNr = i
				break
	try: 
		return str(firstNr) + " and " + str(secondNr) + " add up to " + str(target) + "!" 
	except NameError: 
		return "There are no two numbers in the array that add up to the target integer."

target = int(input("Enter your target integer here: "))
print(twosum(target))
