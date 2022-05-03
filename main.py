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
    def __init__(self):
        self.nil=Node(0)
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

        def insertFix(self, newNode):
            uncle = None
            parentIsLeft = False
            if newNode.parent==newNode.parent.parent.left:
                uncle = newNode.parent.parent.right
                parentIsLeft = True
            else:
                uncle = newNode.parent.parent.left
            while newNode.parent.color ==0:
                uncle = newNode.parent.parent.right
                #case 1: Uncle is red -> reverse colors of  uncle and parent with grandparent
                if uncle.color==0:
                    newNode.parent.color=1
                    uncle.color=1
                    newNode.parent.parent.color=0
                    newNode=newNode.parent.parent
                else:
                    #case 2: uncle is
                    # Left right condition
                    if parentIsLeft and newNode == newNode.parent.right:
                        newNode = newNode.parent        #Take care as we made the new node the parent
                        self.leftRotate(newNode)
                    #Right Left condition
                    elif parentIsLeft ==False and newNode==newNode.parent.left:
                        newNode=newNode.parent
                        self.rightRotate(newNode)
                    #left left condition
                    if parentIsLeft:
                        newNode.parent.color=1          #the new parent
                        newNode.parent.parent= 0        #the new grandparent will be red
                        self.rightRotate(newNode.parent.parent)
                    #right right condition
                    else:
                        newNode.parent.color =1
                        newNode.parent.parent.color=0
                        self.leftRotate(newNode.parent.parent)

                    self.root.color=1



