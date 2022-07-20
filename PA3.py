class BSTNode:
	# Class for Binary Search Tree Node
	def __init__(self, data, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right

class LinkedListNode:
	# Class for LinkedList Node
	def __init__(self, data, next = None):
		self.data = data
		self.next = next


def create_llist(listx):
    head=LinkedListNode(listx[0])
    new_node=head
    for i in range(1,len(listx)):
        prev_node=new_node
        new_node=LinkedListNode(listx[i])
        prev_node.next=new_node
    return head
        
        
def BST2LinkedList(root):
    linked_list=[]
    def inorder_traverse(root):
        if root.left!=None:
            inorder_traverse(root.left)
        linked_list.append(root.data)
        
        if root.right!=None:
            inorder_traverse(root.right)

    inorder_traverse(root)
    # print(linked_list)
    head=create_llist(linked_list)
    return head
    
	# Function that converts BST to a linked list whose data is in ascending order and returns the list

def place_node_into_BST(BST_root,node_data):
    new_node=BSTNode(node_data)
    if BST_root.data>node_data:
        if BST_root.left==None:
            BST_root.left=new_node
        else:
            place_node_into_BST(BST_root.left,node_data)
            
    elif BST_root.data<node_data:
        if BST_root.right==None:
            BST_root.right=new_node
        else:
            place_node_into_BST(BST_root.right,node_data)


def mergeBSTs(root1, root2):
 	# Merge two BSTs into one, return the root of new tree
     BST2_content=[]
     
     def inorder_traverse(root):
         if root.left!=None:
             inorder_traverse(root.left)
         BST2_content.append(root.data)
         
         if root.right!=None:
             inorder_traverse(root.right)
     inorder_traverse(root2)
     # print(BST2_content)
     for node in BST2_content:
         place_node_into_BST(root1,node)
     return root1
     # printBST(root1)
     
     
def printLinkedList(llist):
	# Takes the output of BST2LinkedList and prints its contents
	current = llist
	while current.next != None:
		print(str(current.data) + " -> ", end="")
		current = current.next
	print(current.data)	

def printBST(bst_root):
    if bst_root.left!=None:
        printBST(bst_root.left)
    print(bst_root.data)
    
    if bst_root.right!=None:
        printBST(bst_root.right)


# Node1=BSTNode(20)
# Node2=BSTNode(10)
# Node1.left=Node2
# Node3=BSTNode(30)
# Node1.right=Node3
# Node4=BSTNode(25)
# Node3.left=Node4
# Node5=BSTNode(100)
# Node3.right=Node5

# Nodex=BSTNode(50)
# Nodey=BSTNode(5)
# Nodex.left=Nodey
# Nodez=BSTNode(70)
# Nodex.right=Nodez

# x=BST2LinkedList(Node1)
# print(x)
# printLinkedList(x)
# printBST(Node1)
# y=mergeBSTs(Node1,Nodex)
# print(y)
# printBST(y)

