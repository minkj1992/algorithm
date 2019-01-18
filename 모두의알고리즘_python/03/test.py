import sys
f = open('./test.txt','r')
tmp = f.readlines()
n,m = map(int, tmp[0].split())
print(n,m)

board = list(map(lambda x: list(map(lambda y: True if y=='W' else False, x.strip())), tmp[1:]))

# chess = [[True if i%2 else False for i in range(m)] if j%2 else [False if i%2 else True for i in range(m)] for j in range(n)]
print([True if i%2 else False for i in range(m)])
print([False if i%2 else True for i in range(m)])
print([i%2 for i in range(m)])


# print(board)
# print(tmp[1:])
# field = []
# for line in f.readlines():
#     field.append(line.replace("\n",""))

f.close()