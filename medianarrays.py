"""
Problem 4: Median of Two Sorted Arrays
Description: 
	"There are two sorted arrays nums1 and nums2 of size m and n respectively. 
	 Find the median of the two sorted arrays. The overall run time complexity should 
	 be 0(log(m+n)). You may assume nums1 and nums2 cannot be both empty."
"""


# Variables 
nums1 = [1, 3, 5, 7]
nums2 = [2, 4, 6, 8, 10] 

m = len(nums1) 
n = len(nums2) 


# Functions 
def odd_numbers(length): 
	"""
	Saving the odd numbers up to the length of the array to later easily 
	categorize arrays with lengths at odd and even numbers separately. 
	"""
	oddNr = []
	for i in range(1,length+1): 
		if i % 2 != 0: 
			oddNr.append(i)
	return oddNr 

# Main function
def arrMedian(array, length): 
	""" 
	Main function to calculate median based on whether there's only one item in the list, 
	and whether the number is odd or even.
	"""
	if length == 1:
		array_median = list[0]
		return array_median
	elif length not in odd_numbers(length): 
		# Floor division with two to access the second relevant number for the median, from which we can add the first one and divide to obtain the median. 
		median_floor = length // 2
		arr_median = (array[median_floor-1] + array[median_floor])/2 
		return arr_median
	elif length in odd_numbers(length):
		# Setting up a loop for the program to recognize when it has reached the middle (median) number, and returning it. 
		for i in range(length):
			if i + 1 == length - i: 
				median = array[i] 
				return median

nums1_median = int(arrMedian(nums1, m))
nums2_median = int(arrMedian(nums2, n))
total_median = (nums1_median + nums2_median) / 2 	

print ("The median of the first array is " + str(nums1_median) + ", the median of the second array is " + str(nums2_median) + ", the total of which is " + str(total_median) + ".")
