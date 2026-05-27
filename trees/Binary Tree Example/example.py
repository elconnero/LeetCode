
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = BinaryTree("R")
leafA =  BinaryTree("A")
leafB =  BinaryTree("B")
leafC =  BinaryTree("C")
leafD =  BinaryTree("D")
leafE =  BinaryTree("E")
leafF =  BinaryTree("F")
leafG =  BinaryTree("G")
leafH =  BinaryTree("H")



#This is where we are making the tree
root.left = leafA
root.right = leafB

leafA.left = leafC
leafA.right = leafD

leafB.left = leafE
leafB.right = leafF

leafC.left = leafG
leafC.right = leafH

print("root.left.right.data:", root.left.left.left.data)