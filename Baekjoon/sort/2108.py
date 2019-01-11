# counting sort를 사용해서 한방에 성공하였다.(숏코딩 1등)
# 음수를 사용해야 해서 -4000~4000 -(+4000)> 0~8001로 변환시켜서 저장한다.
#first try
n = 8001 #abs_value*2+1
m = 4000 #abs_value
#sum
s = 0
# counting sort에서 0을 지워준 list
k = []
#counting sort list
a=[0]*n
N=int(input())

# a update
for _ in range(N):
  i=int(input())
  a[i+m]+=1
  s+=i
# k update
for i in range(n):
  k+=[i-m]*a[i]
print(round(s/N))

mm=max(a)
idx=[i for i,j in enumerate(a) if j==mm]
if N==1: print(k[0])
else: print(k[(N-1)//2])

if len(idx)==1: print(idx[0]-m)
else: print(idx[1]-m)

print(k[-1]-k[0])
