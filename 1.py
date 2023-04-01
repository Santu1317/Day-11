'''class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key
        
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key) + "->", end=' ')
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left,key)
    else:
        node.right = insert(node.right,key)
    return node
def minvalueNode(node):
    current=node
    while(current.left is not None):
        current = current.left
    return current
def deleteNode(root,key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left,key)
    elif key > root.key:
        root.right = deleteNode(root.right,key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minvalueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right,temp.key)
    return root
root = None
root = insert(root,8)
root = insert(root,3)
root = insert(root,1)
root = insert(root,6)
root = insert(root,7)
root = insert(root,10)
root = insert(root,14)
root = insert(root,4)
print("Inorder Traversal: ",end='')
inorder(root)
print("\nDelete 4")
root=deleteNode(root, 6)
print("Inorder Traversal: ",end='')
inorder(root)
print("\nDelete 6")
root=deleteNode(root, 8)
print("Inorder Traversal: ",end='')
inorder(root)'''



class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
def merge_lists(list1, list2, n):
    current_node = list1
    count = 1
    while count < n:
        current_node = current_node.next
        count += 1
    temp = current_node.next
    current_node.next = list2
    while list2.next:
        list2 = list2.next
    list2.next = temp
    return list1 
list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(4)
list1.next.next.next = Node(3)
list1.next.next.next.next = Node(5)
list2 = Node(9)
list2.next = Node(8)
list2.next.next = Node(11)
merged_list = merge_lists(list1, list2, 2)
current_node = merged_list
while current_node:
    print(current_node.data, end=' ')
    current_node = current_node.next



