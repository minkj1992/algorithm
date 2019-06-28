class Node:
    def __init__(self,data):
        self.data = data
        self.childs = []
def dfs(A):
    stack = []
    visited = set()
    while stack:
        node = stack.pop()
        if node in visited:continue
        print(node.data)
        stack.extend(tmp.childs)

if __name__ == '__main__':
    A = Node('A',)
