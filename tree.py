#==============================
# Laby class
# - Create a Binary tree
# - Chose the content of the node by adding attribut
#==============================
import svg

class Node():
	def __init__(self,data):
		self.right = None
		self.left = None
		self.data = data

class BinaryTree():

   def __init__(self): 
		self.root = None 

   def addNode(self,data):
		return Node(data)

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

   def printSVG(self,root,name):
   	height = self.height(root,0)
   	self.F = svg.SVGFile(name)
   	self.F.write_header((2**height)*10,(2**height)*10)
   	self.createSVG(root,(2**height)*5,5,(2**height)*5,5)
   	self.F.write_footer()
   	self.F.write_in_file()

   def createSVG(self,root,x_1,y_1,x_2,y_2):
   	if root == None:
   		pass
   	else:
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

class BinarySearchTree(BinaryTree):
	

	def insert(self,root,data):
		if root == None:
			return self.addNode(data)
		else:
			if data <= root.data:
				root.left = self.insert(root.left,data)
			else:
				root.right = self.insert(root.right,data)
		return root

	def search(self,root,data):
	    if root == None:
	        return False
	    elif root.data == data:
	        return True
	    elif data <= root.data:
	        return self.search(root.left,data)
	    else:
	        return self.search(root.right,data)

	def delete(self,root,data):

		if root == None:
			return
	      
		if root.left != None and root.left.data == data:
			left = root.left.left
			right = root.left.right

			root.left = left
			if left != None:
				left.right = right

			return
		elif root.right != None and root.right.data == data:
			left = root.right.left
			right = root.right.right

			root.right = right
			if right != None:
				right.left = left
	         
			return
			
		else:
			self.delete(root.left,data) 
			self.delete(root.right,data) 




