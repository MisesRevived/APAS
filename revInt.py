"""
APAS Problem 7: Reverse Integer 
Description: "Given a 32-bit signed integer reverse digits of an integer." 
Examples: "Input: 123, Output: 321"; "Input: -123, Output: -321", "Input: 120, Output: 21"
""" 

def revInt(int): 
	strInt = str(int)
	arrInt = []
	for i in reversed(strInt):
		if i != "0" and i != "-":
			arrInt.append(i)
		elif i == "-":
			arrInt.insert(0, i)
	strInt2 = ""
	for k in arrInt:
		strInt2 += k
	return strInt2

int = input("Enter 3-digit integer: ")
rev = revInt(int)
print(rev)
