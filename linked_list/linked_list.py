

class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = Node()

	def append(self, data):
		new_node = Node(data)
		cur = self.head
		while cur.next != None:
			cur = cur.next
		cur.next = new_node

	def length(self):
		cur = self.head
		total = 0
		while cur.next != None:
			cur = cur.next
			total += 1
		return total

	def display(self):
		cur = self.head
		elems = []
		while cur.next != None:
			cur = cur.next
			elems.append(cur.data)
		print elems

	def get(self, index):
		if index >= self.length():
			print 'ERROR: get index is out of range!'
			return
		cur = self.head
		cur_indx = 0
		while True:
			cur = cur.next
			if index == cur_indx:
				return cur.data
			cur_indx += 1

	def erase(self, index):
		if index >= self.length:
			print 'ERROR: erase index is out of range!'
			return 
		cur = self.head
		cur_indx = 0
		while True:
			prev_node = cur
			cur = cur.next 
			if cur_indx == index:
				prev_node.next = cur.next
				return
			cur_indx += 1


if __name__ == '__main__':
	new_list = LinkedList()
	new_list.append(3)
	new_list.append(1)
	new_list.append(5)
	new_list.append(2)
	new_list.display()
	print new_list.get(0)
	new_list.erase(2)
	new_list.erase(2)
	new_list.display()