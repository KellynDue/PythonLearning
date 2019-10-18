
"""结点"""
class Node():
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

"""二叉树"""
class BinaryTree():
    def __init__(self, root = None):
        self.root = root
    def add(self, elem):
        # 初始化一个结点
        node = Node(elem)
        # 判断根结点是否为空
        if self.root == None:
            # 根结点为空，赋值
            self.root = node
        else:
            # 用队列的方式判断当前结点有没有可加入的位置
            myqueue = []
            myqueue.append(self.root)
            while myqueue:
                current = myqueue.pop(0)
                if current.lchild == None:
                    current.lchild = node
                    return
                elif current.rchild == None:
                    current.rchild = node
                    return
                else:
                    myqueue.append(current.lchild)
                    myqueue.append(current.rchild)

    def depth_first_search(self, root):
        if root == None:
            return
        myStack = []
        current = root
        while current or myStack:
            # 当前结点存在并且左子树存在
            while current:
                myStack.append(current)
                current = current.lchild
            # 当前结点为空，即前一结点没有左子树
            current = myStack.pop()
            print(current.elem,' ')
            current = current.rchild

    def breath_first_search(self,root):
        if root == None:
            return
        myQueue = []
        current = root
        myQueue.append(current)
        while myQueue:
            current = myQueue.pop(0)
            print(current.elem,' ')
            if current.lchild != None:
                myQueue.append(current.lchild)
            if current.rchild != None:
                myQueue.append(current.rchild)


"""主函数"""
if __name__ == '__main__':
    elems = [10, 2, 14, 8, 12, 13]
    tree = BinaryTree()
    for elem in elems:
        tree.add(elem)
    # print(tree)
    print("DFS:")
    tree.depth_first_search(tree.root)
    print("BFS:")
    tree.breath_first_search(tree.root)


