"""
Problem 5: Longest Palindromic Substring 
Description: 
	"Given a string s, find the longest palindromic substring in s.
	 You may assume that the maximum length of s is 1000."
"""

# Variables 
s = "aababcdcbab" 
longest_substr = "" 	

def isPalindromic(string): 
	# Testing if string is polindromic 
	len_str = len(string)
	len_str_halved = len_str // 2
	if len_str % 2 != 0: # Length of list is an odd number.
		return string[:len_str_halved] == string[:len_str_halved:-1] # List is symmetric

	elif len_str % 2 == 0: # Length of list is an even number.
		return string[:len_str_halved] == string[:len_str_halved - 1:-1] # List is symmetric
	
# Main loop 

for i in range(len(s)):
	substr = ""

	# Locating repeating characters. 
	i_repeat = [k for k in range(i, len(s)) if s[k] == s[i]] # List comprehension to identify indexes with character s[i]. 
	len_i_repeat = len(i_repeat)
	
	if len_i_repeat > 1:  
		substr = s[i_repeat[0]:i_repeat[1]+1] # Setting substring from the first index with the character to the second. 

	# Testing if the characters following the substring can be added to constitute a longer palindromic substring.
	if len_i_repeat > 2:  
		temp_substr = substr 
		for k in range(1, len_i_repeat - 1): 
			comp_substr = temp_substr + s[i_repeat[k]+1:i_repeat[k+1]+1] # Compounding substring up to the character's next repetition.
			temp_substr = comp_substr
			if isPalindromic(temp_substr): 
				substr = temp_substr

	if len(substr) > len(longest_substr) and isPalindromic(substr): 
		longest_substr = substr

print("The longest polindromic substring in s is: " + longest_substr) 

