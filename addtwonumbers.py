"""
Problem 2: Add Two Numbers. 

APAS' description of problem: 

	"You are given two non-empty linked lists representing two non-negative integers.
	 The digits are stored in reverse order and each of their nodes contain a single digit.
	 Add the two numbers and return it as a linked list. 
	 You may assume the two numbers do not contain any leading zero, except the number 0 itself."

"""
# Creating linked list
class Node: 
	def __init__(self, dataval=None): 
		self.dataval = dataval 
		self.nextval = None 

class SLinkedList: 
	def __init__(self, dataval=None): 
		self.headval = None 

# First linked list
list1 = SLinkedList() 
list1.headval = Node(2)
e2 = Node(4)
e3 = Node(3)
list1.headval.nextval = e2 # Connecting first node to second 
e2.nextval = e3 # Connecting second node to third

# Second linked list
list2 = SLinkedList() 
list2.headval = Node(5)
f2 = Node(6)
f3 = Node(4)
list1.headval.nextval = f2 
f2.nextval = f3 

# Adding the respective numbers and reversing the order.
g1 = list1.headval.dataval + list2.headval.dataval 
g2 = e2.dataval + f2.dataval 
g3 = e3.dataval + f3.dataval 

# When one of the digits are ten or above, add to the higher order.
if g1 >= 10: 
	g1 = str(g1)
	g2 += int(g1[0])  
	if g1 == 0 or g1 == None:
		g1 = 0 
	else: 
		g1 = int(g1[1])
if g2 >= 10: 
	g2 = str(g2)
	g3 += int(g2[0])  
	if g2 == 0 or g2 == None:
		g2 = 0 
	else: 
		g2 = int(g2[1])

# Setting up solution in a new linked list. 	
list_solution = SLinkedList() 
list_solution.headval = Node(g3) 
i2 = Node(g2)
i3 = Node(g1) 
list_solution.headval.nextval = i2 
i2.nextval = i3
	
output = str(list_solution.headval.dataval) + " " + str(i2.dataval) + " " + str(i3.dataval)

print (output)