def pick(n,picked,toPick):
  global ret
  ''' 
  Recursive
  n개의 원소중 m개를 고르는 모든 조합을 찾는 알고리즘
  n: 전체 원소의 수 (int number)
  picked: 지금까지 고른 원소들의 번호(init [])
  toPick: 더 고를 원소의 수(int number )
  OUTPUT : toPick개의 원소를 고르는 모든 방법
  '''
  # base condition
  if toPick==0:print(picked);ret+=1;return
  smst = 0 if not picked else picked[-1]+1
  
  for next in range(smst,n):
      picked.append(next)
      pick(n,picked,toPick-1)
      picked.pop()

if __name__=='__main__':
    # picked = ['a','b','c','d']
    picked = []
    ret =0
    pick(7,picked,4)
    print(ret)

#  7 C 3 = 35
# [0, 1, 2, 3]
# [0, 1, 2, 4]
# [0, 1, 2, 5]
# [0, 1, 2, 6]
# [0, 1, 3, 4]
# [0, 1, 3, 5]
# [0, 1, 3, 6]
# [0, 1, 4, 5]
# [0, 1, 4, 6]
# [0, 1, 5, 6]
# [0, 2, 3, 4]
# [0, 2, 3, 5]
# [0, 2, 3, 6]
# [0, 2, 4, 5]
# [0, 2, 4, 6]
# [0, 2, 5, 6]
# [0, 3, 4, 5]
# [0, 3, 4, 6]
# [0, 3, 5, 6]
# [0, 4, 5, 6]
# [1, 2, 3, 4]
# [1, 2, 3, 5]
# [1, 2, 3, 6]
# [1, 2, 4, 5]
# [1, 2, 4, 6]
# [1, 2, 5, 6]
# [1, 3, 4, 5]
# [1, 3, 4, 6]
# [1, 3, 5, 6]
# [1, 4, 5, 6]
# [2, 3, 4, 5]
# [2, 3, 4, 6]
# [2, 3, 5, 6]
# [2, 4, 5, 6]
# [3, 4, 5, 6]
