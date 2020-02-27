"""
Problem 3: Longest Substring Without Repeating Characters 
Description: 
	"Given a string, find the length of the longest substring without repeating characters."
"""

# Variables 
input = "abcabcbb" 
input_array = []
for char in input:
	input_array.append(char) 
input_length = len(input_array)
substrlen = 0
substr = ""

# Main function 

for i in range(input_length-1):
	for j in range(i+1,input_length): 
		if input_array[j] == input_array[i]: # Locating repeating characters.  
			substrlen_temp = j - i # Temporary variable for substring length.
			# Updating results when a longer substring than the previous is located.
			if substrlen_temp > substrlen:
				substrlen = substrlen_temp 
				substr = input[i:j]
			break # End second loop when input_array[j] == input_array[i] identified.


print ("The longest substring is " + substr + " with a length of " + str(substrlen) + ".")