class Node:
	def __init__(self,value):
		self.value=value
		self.greater=None
		self.lesser=None

class Tree:
	def __init__(self, root_node):
		self.root=root_node

	def search(self, current_node, value):
		cur_node=current_node
		if (cur_node==None):
			return False
		elif (value==cur_node.value):
			return True
		elif (value>cur_node.value):
			cur_node=cur_node.greater
			return self.search(cur_node,value)
		elif (value<cur_node.value):
			cur_node=cur_node.lesser
			return self.search(cur_node,value)

	def insert(self,new_node):
		my_root=self.root_node()
		node_exist=self.search(my_root, new_node.value)
		if (node_exist==True):
			print ("this node already exist in the tree")
		else:
			insert_pos_node=self.find_insert_pos(my_root, new_node.value)
			if (new_node.value>insert_pos_node.value):
				insert_pos_node.greater=new_node
			elif (new_node.value<insert_pos_node.value):
				insert_pos_node.lesser=new_node







	def lowest_node(self):
		cur_node=self.root_node()
		while (cur_node.lesser!=None):
			cur_node=cur_node.lesser

		return cur_node

		



	def root_node(self):
		return self.root

	def find_insert_pos(self,current_node, value):
		cur_node=current_node
		if (value>cur_node.value):
			if (cur_node.greater==None):
				return cur_node
			else:
				cur_node=cur_node.greater
				return self.find_insert_pos(cur_node,value)
		elif (value<cur_node.value):
			if (cur_node.lesser==None):
				return cur_node

			else:
				cur_node=cur_node.lesser
				return self.find_insert_pos(cur_node,value)

		else:
			return False


		



my_tree=Tree(Node(9))
my_tree.insert(Node(6))
my_tree.insert(Node(13))
root=my_tree.root_node()
print (my_tree.search(root, 21))
print (my_tree.lowest_node().value)

		



#	def insert(self,new_node):




