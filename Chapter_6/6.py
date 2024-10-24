class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)  
        else:
            self._insert_recursive(self.root, data)  

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)  
            else:
                self._insert_recursive(node.left, data)  
        else:
            if node.right is None:
                node.right = TreeNode(data)  
            else:
                self._insert_recursive(node.right, data)  

    def search(self, data):
        return self._search_recursive(self.root, data) 

    def _search_recursive(self, node, data):
        if node is None or node.data == data:
            return node 
        if data < node.data:
            return self._search_recursive(node.left, data) 
        return self._search_recursive(node.right, data) 

    def in_order_traversal(self):
        return self._in_order_recursive(self.root)  

    def _in_order_recursive(self, node):
        result = []
        if node:
            result.extend(self._in_order_recursive(node.left))  
            result.append(node.data) 
            result.extend(self._in_order_recursive(node.right)) 
        return result

    def pre_order_traversal(self):
        return self._pre_order_recursive(self.root)  

    def _pre_order_recursive(self, node):
        result = []
        if node:
            result.append(node.data)  
            result.extend(self._pre_order_recursive(node.left))  
            result.extend(self._pre_order_recursive(node.right))  
        return result

    def post_order_traversal(self):
        return self._post_order_recursive(self.root)  

    def _post_order_recursive(self, node):
        result = []
        if node:
            result.extend(self._post_order_recursive(node.left)) 
            result.extend(self._post_order_recursive(node.right))  
            result.append(node.data)  
        return result

tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)

print(tree.search(5)) 
print(tree.search(20)) 

print(tree.in_order_traversal())  
print(tree.pre_order_traversal())  
print(tree.post_order_traversal()) 
