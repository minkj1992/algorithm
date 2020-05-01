#first try
#TIL: insertioin sort를 활용하여 insert 될때마다 
#TIL: reversed(s) == s[::-1]
#TIL: print(*list,sep='\n')
#TIL: s.insert(index,value)

s = []
for _ in range(int(input())):
  if len(s)==0:
    s.append(int(input()))
  else:
  #맨 뒤에서 부터 index를 빼주면서 전진한다.
    ins,indx = int(input()),len(s)
    for i in s[::-1]:
      if ins>=i:
        break
      indx-=1
    s.insert(indx,ins)
print(*s,sep='\n')

#second try, stl사용
#TIL: sorted는 원본을 바꾸지 않고
#TIL: s.sort()는 원본을 바꾼다. 하지만 None 을 return한다.
from sys import stdin as I
s = []
for _ in range(int(I.readline())):
  s.append(int(I.readline()))
print(*sorted(s),sep='\n')

#short coding
#TIL: print(eval("5,")*5) == (5,5,5,5,5)
#TIL: print([eval("i") for i in [5, 2, 3, 4, 1]]) == [5, 2, 3, 4, 1]
print(*sorted(eval("int(input()),")*int(input()))))

