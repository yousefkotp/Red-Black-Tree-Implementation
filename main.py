class Node:
    #if color = 0 then red, if 1--> black
    def __init__(self, key):        #self references the current instance of this class
        self.key=key                #needs a key to be initialized
        self.right=None
        self.left=None
        self.color=0
        self.parent=None

    def __str__(self):
        if(self.color==0):
            color = "Red"
        else:
            color = "Black"
        msg = ("Key: {}\nColor: {}\nLeft: {}\nRight: {}\nParent: {}"
            .format(
            self.key,
            color,
            self.left.key,
            self.right.key,
            self.parent.key
        ))
        if self.parent.key is None:
            msg = "This node is the Root\n" + msg
        return msg
class RedBlackTree:
    def __init__(self,newNode=Node):        #needs a node to be initialized
        self.nil=newNode(0)
        self.nil.color = 1                  #the root and the nil are black
        self.root = self.nil
        self.number_of_nodes= 0

    def insertNode(self,key):
        newNode =Node(key)
        node = self.root
        parent=self.nil         #aka None aka nil
        while(node!=self.nil):  #as long as we didn't reach the end of the tree
            parent = node
            if newNode.key <node.key:
                node = node.left
            else:
                node = node.right

        if parent == self.nil:     #if the inserted node is the first node
            self.root=newNode
        elif newNode.key <parent.key:
            parent.left=newNode
        else:
            parent.right=newNode

        self.insertFix(newNode)
        self.number_of_nodes= self.number_of_nodes+1

        def insertFix(self, newNode=Node):
