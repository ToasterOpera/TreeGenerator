import random

class Branch:
    def __init__(self, custom, customBranch, treeSpace):
        self.looks = ""
        self.treeSpace = treeSpace
        if custom:
            for x in range(int((self.treeSpace - len(customBranch)) / 2)):
                self.looks += " "
            self.looks += customBranch
        else:
            self.generate(customBranch)
        for x in range(self.treeSpace - len(self.looks)):
                self.looks += " "
    
    def generate(self, length):
        decor = "~`Oo^+*v.§"
        for x in range(int((self.treeSpace - length) / 2)):
            self.looks += " "
        for x in range(length):
            self.looks += random.choice(decor)

class Tree:
    def __init__(self, height, width, custom):   
        self.height = height
        self.width = width
        self.branches = []
        if custom:
            for x in range(height):
                inp = input("Would you like branch " + str(x) + " to be custom (c) or random (r)?")
                while(inp.lower() != "r" and inp.lower() != "c"):
                    inp = input("Please only type \"c\" or \"r\".")
                if inp.lower() == "c":
                    customBranch = input("Type in your custom branch.\n")
                    while(len(customBranch) > width):
                        customBranch = input("That branch is too long! This tree is only " + width + " characters wide. Try again.\n")
                    self.branches.append(Branch(True, customBranch, width))
                else:
                    self.branches.append(Branch(False, int((x * width) / height), width))   
        else:
            for x in range(height):
                self.branches.append(Branch(False, int((x * width) / height), width))

            
def makeTree():
    inp = input("Do you want to make a custom tree (c) or a random tree (r)? (c or r)\n")
    while(inp.lower() != "r" and inp.lower() != "c"):
        inp = input("Please only type \"c\" or \"r\".")
    if inp.lower() == "c":
        height = int(input("How tall do you want your tree?"))
        width = int(input("How wide do you want your tree?"))
        return Tree(height, width, True)
    else:
        return Tree(random.randrange(2, 25), random.randrange(2, 25), False)

def printTree(tree):
    for x in range(tree.height):
        print(tree.branches[x].looks)

#def printTrees(trees, maxHeight):
#    for x in range(maxHeight):
#        for tree in trees:
#            if x - (maxHeight + 1 - tree.height) > 0 and x - (maxHeight + 1 - tree.height) < tree.height:
#                print(tree.branches[x - (maxHeight + 1 - tree.height)].looks, end="")
#            else:
#                for x in range(tree.width-1):
#                    print(" ", end="")
#        print("")

#trees = []
#maxHeight = 0
#again = input("Hello! Would you like to plant a tree? (y or n)\n")
#while (again.lower() == "y"):
#    nextTree = makeTree()
#    trees.append(nextTree)
#    if nextTree.height > maxHeight:
#        maxHeight = nextTree.height
#    printTrees(trees, maxHeight)
#    again = input("Would you like to plant another tree?\n")

printTree(makeTree())

