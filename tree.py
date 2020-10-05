class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

class Binarytree:
	def __init__(self,data):
		self.root = Node(data)

	def preorder(self,start):
		if start:
			print(start.data,end= " ")
			self.preorder(start.left)
			self.preorder(start.right)

	def inorder(self,start):
		if start:
			self.inorder(start.left)
			print(start.data,end = " ")
			self.inorder(start.right)

	def postorder(self,start):
		if start:
			self.postorder(start.left)
			self.postorder(start.right)
			print(start.data, end= " ")

	def insert(self,start,data):
		if not start:
			self.root = Node(data)
		else:
			if data < start.data:
				if not start.left:
					start.left = Node(data)
				else:
					self.insert(start.left,data)
			else:
				if not start.right:
					start.right = Node(data)
				else:
					self.insert(start.right,data)

	def levelOrder(self):
		traversal = ""
		l= list()
		t = self.root
		l.append(t)
		while(len(l)!=0):
			traversal += (str(l[0].data) + " ") 
			if l[0].left:
				l.append(l[0].left)
			if l[0].right:
				l.append(l[0].right)
			l.remove(l[0])
		return traversal

	def height(self,start):
		if start is None:
			return -1

		left_height = self.height(start.left)
		right_height = self.height(start.right)
		return 1 + max(left_height,right_height)

	def sizeOfTree(self,start):
		stack = list()
		stack.append(start)
		count = 1
		while len(stack) != 0:
			if stack[0].left:
				stack.append(stack[0].left)
				count += 1
			if stack[0].right:
				stack.append(stack[0].right)
				count += 1
			stack.remove(stack[0])
		return count

	def search(self,start,data):
		if data == start.data:
			return True
		else:
			if data < start.data and start.left:
				 return (self.search(start.left,data))
				
			if data > start.data and start.right:
				return (self.search(start.right,data))
	def BstProperty(self,start):
		if start:
			self.BstProperty(start.left)
			l.append(start.data)
			self.BstProperty(start.right)

	def maxDepth(self,start):
		if not start:
			return 1
		else:
			return 1 + max(self.maxDepth(start.left),self.maxDepth(start.right))



l=[]
tree = Binarytree(10)
print("Binary Search Tree Operations")
while True:
	print('''1.Insert
2.Preorder Traversal
3.Postorder Traversal
4.Inorder Traversal
5.Level Traversal
6.Search
7.Size
8.Height
9.Bst property
10.max depth
11.Exit
		''')
	choice = int(input("Enter your choice: "))
	if choice == 1:
		value = int(input("Enter data to insert: "))
		tree.insert(tree.root,value)

	elif choice == 2:
		tree.preorder(tree.root)

	elif choice == 3:
		tree.postorder(tree.root)

	elif choice == 4:
		tree.inorder(tree.root)

	elif choice == 5:
		print(tree.levelOrder())

	elif choice == 6:
		key = int(input("Enter data to search: "))
		print(tree.search(tree.root,key))

	elif choice == 7:
		print(tree.sizeOfTree(tree.root))

	elif choice == 8:
		print(tree.height(tree.root))

	elif choice == 9:
		tree.BstProperty(tree.root)
		t=l[0]
		flag = True
		for i in range(1,len(l)):
			if l[i] < t:
				flag = False
			else:
				t = l[i]
		print(flag)
	elif choice == 10:
		print((tree.maxDepth(tree.root)-1))
	elif choice == 11:
		break
	else:
		print("Invalid choice")


