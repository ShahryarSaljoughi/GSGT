__author__ = 'shahryar_slg'

class Node():
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def Str2Tree(preOrderedString,inOrderedString):
    """

    :rtype : object
    """
    preStr=str(preOrderedString)
    inStr = str(inOrderedString)
    root= preStr[0]
    node = Node(root)
    if (preStr==inStr and len(preStr)==len(inStr)==1) :
        return node

    inOrderStrOfLeftTree=inStr.partition(sep=root)[0]
    inOrderStrOfRightTree = inStr.partition(sep=root)[2]
    lenOfLeft=len(inOrderStrOfLeftTree)
    lenOfRight = len(inOrderStrOfRightTree)
    preOrderStrOfLeftTree=preStr[1:lenOfLeft]
    preOrderStrOfRightTree=preStr[lenOfLeft+1:]
    if lenOfLeft>0:
        node.left=Str2Tree(preOrderStrOfLeftTree,inOrderStrOfLeftTree)
    if lenOfRight>0:
        node.right=Str2Tree(preOrderStrOfRightTree,inOrderStrOfRightTree)
