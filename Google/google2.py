# Given the root to a binary tree, implement serialize(root), 
# which serializes the tree into a list, and deserialize(s), 
# which deserializes the list back into the tree.

index = int(0)

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node, data=[]):
    data.append(node.val)
    
    if node.left == None:
        data.append(-1)
    else:
        serialize(node.left, data)

    if node.right == None:
        data.append(-1)
    else:
        serialize(node.right, data)

    return data

def deserialize(data):
    global index

    if data[index] == -1:
        index += 1
        return None
    else:
        val = data[index]
        index += 1
        left = deserialize(data)
        right = deserialize(data)
        return Node(val, left, right)

# Create Tree:
#               (root)
#               /    \
#           (left)  (right)
#           /    \  /     \
#     (left.left)
#      /       \

node = Node('root', Node('left', Node('left.left')), Node('right'))

# Check Serialization
print(serialize(node))

# Check Tree integrity
print(deserialize(serialize(node)).val == 'root')
print(deserialize(serialize(node)).left.val == 'left')
print(deserialize(serialize(node)).left.left.val == 'left.left')
print(deserialize(serialize(node)).right.val == 'right')
print(deserialize(serialize(node)).right.right == None)