"""
Function testing if any two numbers in an array add up to a given target number, regardless of the size of the array. 
The function can also be easily edited to test for other conditions of the two numbers by changing the operator in 
the conditional on line 12, i.e. to -, *, /, **, or %. 
"""

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
