

class Node:
    def __init__(self, value):
        self.left= None
        self.data= value
        self.right= None

#Create tree type DS

class Tree:
    def create_node(self,data):
        print('inside create_node')
        return Node(data)  #This will create a node using Node first time "None, 5, None"
    def insert_node(self,node, data):
        print("inside insert node", node, data)
        if node is None:
            print("node is None")
            return self.create_node(data)
        if data < node.data:
            print("node.left, data", node.left, data)
            node.left = self.insert_node(node.left,data)
        if data > node.data:
            print("node.right, data", node.right, data)
            node.right = self.insert_node(node.right,data)
        return node

# first_node = Node(5)
# print(first_node.left, first_node.data, first_node.right)

tree=Tree()
parent_node = tree.create_node(5)
child_node = tree.insert_node(parent_node,3)
child_node = tree.insert_node(parent_node,8)

print(parent_node)
print(child_node)
print("parent_node:",parent_node.left, parent_node.data, parent_node.right)
print("child_node:",child_node.left, child_node.data, child_node.right)




