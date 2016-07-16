__author__ = 'shahryar_slg'

class Node():
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def Str2Tree(preOrderedString,inOrderedString):
    """

    :rtype : object of Node class
    """
    preStr=str(preOrderedString)
    inStr = str(inOrderedString)
    root= preStr[0]
    print "root is ",root """ PPPPPPPPPRRRRRRRRRRRRRIIIIIIIIIIIIINNNNNNNNNNNNTTTTTTTTTTTTT"""
    node = Node(root)
    if (preStr==inStr and len(preStr)==len(inStr)==1) :
        return node

    inOrderStrOfLeftTree=inStr.partition(root)[0]
    print "inorder string of left tree is ",inOrderStrOfLeftTree""" PPPPPPPPPRRRRRRRRRRRRRIIIIIIIIIIIIINNNNNNNNNNNNTTTTTTTTTTTTT"""
    inOrderStrOfRightTree = inStr.partition(root)[2]
    print "inorder string of right tree is ", inOrderStrOfRightTree""" PPPPPPPPPRRRRRRRRRRRRRIIIIIIIIIIIIINNNNNNNNNNNNTTTTTTTTTTTTT"""
    lenofleft=len(inOrderStrOfLeftTree)
    lenOfRight = len(inOrderStrOfRightTree)
    preOrderStrOfLeftTree=preStr[1:lenofleft+1]

    preOrderStrOfRightTree=preStr[lenofleft+1:]
    if lenofleft>0:
        node.left=Str2Tree(preOrderStrOfLeftTree,inOrderStrOfLeftTree)
    if lenOfRight>0:
        node.right=Str2Tree(preOrderStrOfRightTree,inOrderStrOfRightTree)
