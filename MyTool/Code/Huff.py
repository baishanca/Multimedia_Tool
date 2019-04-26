# 树节点类构建
class TreeNode(object):
    def __init__(self, data):
        self.val = data[0]
        self.priority = data[1]
        self.leftChild = None
        self.rightChild = None
        self.code = ""
# 创建树节点队列函数
def creatnodeQ(codes):
    q = []
    for code in codes:
        q.append(TreeNode(code))
    return q
# 为队列添加节点元素，并保证优先度从大到小排列
def addQ(queue, nodeNew):
    if len(queue) == 0:
        return [nodeNew]
    for i in range(len(queue)):
        if queue[i].priority >= nodeNew.priority:
            return queue[:i] + [nodeNew] + queue[i:]
    return queue + [nodeNew]
# 节点队列类定义
class nodeQeuen(object):

    def __init__(self, code):
        self.que = creatnodeQ(code)
        self.size = len(self.que)

    def addNode(self,node):
        self.que = addQ(self.que, node)
        self.size += 1

    def popNode(self):
        self.size -= 1
        return self.que.pop(0)
# 各个字符在字符串中出现的次数，即计算优先度
def freChar(string):
    d ={}
    for c in string:
        if not c in d:
            d[c] = 1
        else:
            d[c] += 1
    return sorted(d.items(),key=lambda x:x[1])
# 创建Huffman树
def creatHuffmanTree(nodeQ):
    while nodeQ.size != 1:
        node1 = nodeQ.popNode()
        node2 = nodeQ.popNode()
        r = TreeNode([None, node1.priority+node2.priority])
        r.leftChild = node1
        r.rightChild = node2
        nodeQ.addNode(r)
    return nodeQ.popNode()
