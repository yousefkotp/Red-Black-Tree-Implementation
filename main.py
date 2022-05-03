import DataStructure as ds
tree= ds.RedBlackTree()
def readFile(fileName):
    file = open(fileName, "r")
    for i in file:
        tree.insert(i.rstrip('\n'))
    file.close()
while True:
    print("What do you want to do?")
    option = int(input("1- Load Dictionary\t2- Print size of the Dictionary\n3- Insert Word\t4- Look-up a Word\n5-Print Tree Height\t6- Exit\n"))
    if option ==1:
        readFile("EN-US-Dictionary.txt")
    elif option ==2:
        print(tree.number_of_nodes)
    elif option ==3:
        s = str(input("Enter the word you want to insert: "))
        if tree.search(s):
            print("ERROR: Word already in the dictionary!")
        else:
            tree.insert(s)
            print("Inserted Successfully")
    elif option==4:
        s = str(input("Enter the word you want to look-up: "))
        if tree.search(s):
            print("YES")
        else:
            print("NO")
    elif option ==5:
        print(tree.heightOfTree(tree.root,0))
    else:
        print("Thank you for using our application! :)")
        break;

