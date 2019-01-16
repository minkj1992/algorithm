# first try
# list를 활용하여 stack 구현

class Stack():
    def __init__(self):
        self.li = []
    def push(self,num):
        self.li.append(num)
    def pop(self):
        try:
            print(self.li.pop()) 
        except IndexError:
            print(-1)
    def size(self):
        print(len(self.li))
    def empty(self):
        print(int(len(self.li)==0))
    def top(self):
        try:
            print(self.li[-1] )
        except IndexError:
            print(-1)
        
if __name__=="__main__":
    s=Stack()
    for _ in range(int(input())):
        cmd = input().split()
        if cmd[0] == 'push':
            s.push(cmd[1])
        elif cmd[0] == 'pop':
            s.pop()
        elif cmd[0] == 'size':
            s.size()
        elif cmd[0] == 'empty':
            s.empty()
        elif cmd[0] == 'top':
            s.top()

#second try
#implement with node

