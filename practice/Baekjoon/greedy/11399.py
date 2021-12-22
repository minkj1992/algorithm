#first try
input();n=sorted(list(map(int,input().split())))
for i in range(len(n)-1):
    n[i+1]+=n[i]
print(sum(n))
