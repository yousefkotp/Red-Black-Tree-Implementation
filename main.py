class Node:
    #if color = 0 then red, if 1--> black
    def __init__(self, key):        #self refrence the current instance of this class
        self.key=key
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

