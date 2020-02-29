"""
Problem 5: Longest Palindromic Substring 
Description: 
	"Given a string s, find the longest palindromic substring in s.
	 You may assume that the maximum length of s is 1000."
"""

# Variables 
s = "cbaabaabc" 
longest_substr = "" 	

# Main loop 
for i in s:
	# Locating repeating characters. 
	i_repeat = [j for j in range(len(s)) if s[j] == i] # List comprehension to identify indexes with character i. 
	len_i_repeat = len(i_repeat)
	if len_i_repeat > 1: 
		substr = s[i_repeat[0]:i_repeat[1]+1] # Setting substring from the first index with i to the second. 
		if substr > longest_substr: 
			longest_substr = substr

	# Testing if the characters following the substring can be added to constitute a longer palindromic substring.
	if len_i_repeat > 2:  
		for j in range(2, len_i_repeat): 
			comp_substr = substr + s[i_repeat[j-1]+1:i_repeat[j]+1] # Compounding substring up to the character's next repetition. 
			for k in range(len(comp_substr)): 
				if len(comp_substr) % 2 != 0: # Length of list is an odd number.
					if comp_substr[1:k-1] == comp_substr[-k+1:-1]: # List is symmetric
						substr = comp_substr
				elif len(comp_substr) % 2 == 0: # Length of list is an even number.
					if comp_substr[1:k] == comp_substr[-k:-1]: 
						longest_substr = comp_substr  
						substr = comp_substr 
			if substr > longest_substr: 
				longest_substr = substr

print(longest_substr) 
		