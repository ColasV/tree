#==============================
# Laby class
# - Create a Binary tree
# - Chose the content of the node by adding attribut
#==============================
import svg


class Node():
	def __init__(self,data):
		# Minimum to create a binary tree
		self.right = None
		self.left = None
		self.data = data

class BinaryTree():

	def __init__(self): 
		self.root = None 

	def addNode(self,data):
		return Node(data)

	def insert(self,root,data):
		if root == None:
			return self.addNode(data)
		else:
			if data <= root.data:
				root.left = self.insert(root.left,data)
			else:
				root.right = self.insert(root.right,data)

			return root

	def printTree(self, root):
		if root == None:
 			pass
 		else:
  			self.printTree(root.left)
  			print root.data,
   			self.printTree(root.right)


   	def height(self,root,height):
   		if root == None:
   			return height-1
   		else:
   			left = self.height(root.left,height+1)
   			right = self.height(root.right,height+1)
   			return(max(left,right))

   	def printSVG(self,root):
   		# Need the height to define the size of the SVG file
   		# We know that there is a 2^n node at height n for binary tree
   		height = self.height(root,0)

   		self.F = svg.SVGFile('tree.svg')
   		self.F.write_header((2**height)*10,(2**height)*10)
   		self.createSVG(root,(2**height)*5,5,(2**height)*5,5)
   		self.F.write_footer()
   		self.F.write_in_file()

   	def createSVG(self,root,x_1,y_1,x_2,y_2):
   		if root == None:
   			pass
   		else:
   			# Case left
   			if x_1 > x_2:
   				self.F.write_line(x_1-2,y_1+2,x_2+2,y_2-2)
   				self.F.write_text(x_2-1,y_2+1,root.data)
   			elif x_2 > x_1:
   				self.F.write_line(x_1+2,y_1+2,x_2-2,y_2-2)
   				self.F.write_text(x_2-1,y_2+1,root.data)
   			else:
   				self.F.write_text(x_2-1,y_2,root.data)
   			self.createSVG(root.left,x_2,y_2,x_2-7,y_2+10)
   			self.createSVG(root.right,x_2,y_2,x_2+7,y_2+10)









