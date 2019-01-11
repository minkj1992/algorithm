#단점: merge sort는 기본적으로 n크기의 메모리가 추가적으로 필요하다.
#장점: 정렬 상태와 무관하게(quick의 경우에는 worst n^2) nlogn으로 안정, n^2에 비하여(bubble, insert,selection) O(nlogn)이다.
#장점2: max mem을 넘지 않게 반반씩 잘라가면서,재귀호출로 parallel하게 작업하여 성능 향상을 꾀할 수 있다.
#first try
#TIL: mergesort = 1)divide 2)sort 3)merge
#merge sort의 관건은 새로운 배열을 최대한 만들지 않는 것이다. 
#TIL: li[piv:]=L[l:]
def mergeSort(li):
  #baseline
  if len(li)>1:
    #1)divide
    mid = len(li)//2
    
    L,R=li[:mid],li[mid:]
    mergeSort(L);mergeSort(R)

    l=piv=r=0
    #2)sort & merge
    while l<len(L) and r<len(R):
      if L[l]<R[r]: li[piv]=L[l];l+=1
      else: li[piv]=R[r];r+=1
      piv+=1
    #3) merge(spare care)
    if l==len(L): li[piv:]=R[r:]
    elif r==len(R): li[piv:]=L[l:]

#input()으로 하니까 시간 초과가 뜬다.
li=[]
for i in range(int(input())):
  li.append(int(input()))
mergeSort(li);print(*li,sep='\n')

#second try, stdin.readline()

from sys import stdin as I
def mergeSort(li):
  if len(li)>1:
    mid = len(li)//2
    L,R=li[:mid],li[mid:]
    mergeSort(L);mergeSort(R)
    l=piv=r=0
    while l<len(L) and r<len(R):
      if L[l]<R[r]: li[piv]=L[l];l+=1
      else: li[piv]=R[r];r+=1
      piv+=1
    if l==len(L): li[piv:]=R[r:]
    elif r==len(R): li[piv:]=L[l:]
li=[]
for i in range(int(I.readline())):
  li.append(int(I.readline()))
mergeSort(li);print(*li,sep='\n')

#third try
#시간 초과가 나서 결국에는 pypy3로 돌리니까 뚫렸다.
#추가적으로 stdout.write를 사용하니까 200ms 단축되었다.
from sys import stdin,stdout
def mergeSort(li):
  if len(li)>1:
    mid = len(li)//2
    L,R=li[:mid],li[mid:]
    mergeSort(L);mergeSort(R)
    l=piv=r=0
    while l<len(L) and r<len(R):
      if L[l]<R[r]: li[piv]=L[l];l+=1
      else: li[piv]=R[r];r+=1
      piv+=1
    if l==len(L): li[piv:]=R[r:]
    elif r==len(R): li[piv:]=L[l:]
li=[]
for i in range(int(stdin.readline())):
  li.append(int(stdin.readline()))
mergeSort(li)
for i in li:
  stdout.write(str(i)+'\n')

#4th try
#재귀함수를 사용하여 merge를 구현하는 것이 아닌 loop을 이용하여 구현하기
# 추가적인 메모리 없이 bubble로 sort구현해 보기
# STL사용하여 구현해 보기
