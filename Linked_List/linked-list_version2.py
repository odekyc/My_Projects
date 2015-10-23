
class Node:
	def __init__(self,value):
		self.value=value
		self.next=None
		
class LinkedList:
	def __init__(self, head):
		self.head=head
	

	def find_end_node(self):
		cur_node=self.head

		while (cur_node.next!=None):
			cur_node=cur_node.next

		return cur_node	


	def append(self,new_node):
		end_node=self.find_end_node()
		end_node.next=new_node
		
	def iter_search(self, node_value):
		cur_node=self.head
		while (cur_node!=None):
			if (cur_node.value== node_value):
				return cur_node
			elif (cur_node== self.find_end_node()):
				return "the node value you are looking for is not in this LinkedList"
				break
			else:
				cur_node=cur_node.next
				

	def recur_search(self, current_node, node_value):
		cur_node=current_node
		
		if (cur_node.value==node_value):
			return cur_node
		elif ( cur_node.next==None):
			return "the node value you are looking for is not in this LinkedList"
		else:
			return self.recur_search(cur_node.next,node_value)
			
	def insert(self, cur_node_value , new_node):
		cur_node=self.iter_search(cur_node_value)
		cur_next_node=cur_node.next
		cur_node.next=new_node
		new_node.next=cur_next_node

	def insert_head(self, new_node):
		orig_head=self.head
		self.head=new_node
		self.head.next=orig_head


	def delete(self, node_value):
		cur_node=self.iter_search(node_value)
		if (cur_node is self.head):
			self.head=self.head.next
		else:

			loop_node=self.head
			while (loop_node!=None):
				if (loop_node.next is cur_node):
					prev_node=loop_node
				else:
					loop_node=loop_node.next

			prev_node.next=cur_node.next
			cur_node.next=None
		


	def print_backwards(self, end_node):
		if (end_node==self.find_end_node()):
			print (end_node.value)
		cur_next_node=end_node
		cur_node=self.head
		while (cur_node.next!=None):
			if (cur_node.next==cur_next_node):
				print (cur_node.value)
				return self.print_backwards(cur_node)
			else:
				cur_node=cur_node.next









head=Node(4)
my_linked_list=LinkedList(head)
my_linked_list.append(Node(2))
my_linked_list.append(Node(7))
my_linked_list.append(Node(9))
my_linked_list.append(Node(8))
my_linked_list.append(Node(2))

end_node=my_linked_list.find_end_node()
my_linked_list.print_backwards(end_node)

print (my_linked_list.recur_search(head, 2))
print (my_linked_list.iter_search( 2))
print (my_linked_list.iter_search( 9))
my_linked_list.delete(4)
new_node=Node(10)
new_node2=Node(15)
my_linked_list.insert(2, new_node)
my_linked_list.insert_head(new_node2)
my_linked_list.print_backwards(end_node)
		