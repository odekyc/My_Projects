class Node:
	def __init__(self,value):
		self.value=value
		self.next=None

class Stack:
    def __init__(self):
    	self.head=None


    def push(self, new_node):
    	if (self.head==None):
    		self.head=new_node
    	else:
    		last_node=self.peek()
    		last_node.next=new_node

    def pop(self):
    	last_node=self.peek()
    	sec_to_last_node=self.find_2nd_last_node()
    	sec_to_last_node.next=None
    	return last_node

    def empty(self):
    	if (self.head==None):
    		return "the stack is empty"
    	else:
    		return "the stack is not empty"

    	


    def peek(self):
    	cur_node=self.head
    	if (self.head==None):
    		return None


    	else:
    		while (cur_node.next!=None):
    			cur_node=cur_node.next
    		return cur_node

    def find_2nd_last_node(self):
    	cur_node=self.head
    	if (self.head==None):
    		return None
    	elif (self.head.next==None):
    		return None
    	else:
    		last_node=self.peek()
    		while (cur_node.next!=None):
    			if (cur_node.next==last_node):
    				return cur_node
    			else:
    				cur_node=cur_node.next



stack_1=Stack()
print (stack_1.empty())
node_1=Node(3)
stack_1.push(node_1)
print (stack_1.empty())
stack_1.push(Node(8))
stack_1.push(Node(6))
print (stack_1.peek().value)
print (stack_1.find_2nd_last_node().value)
print (stack_1.pop().value)
print (stack_1.find_2nd_last_node().value)

