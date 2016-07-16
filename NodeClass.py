__author__ = 'shahryar_slg'

class Node():
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def Str2Tree(preOrderedString,inOrderedString):
    preStr=str(preOrderedString)
    inStr = str(inOrderedString)
    root= preStr[0]
    node = Node(root)
    if (preStr==inSt and len(preStr)==len(inStr)==1) :
        return node



    inStr.find()
