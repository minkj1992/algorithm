# first try
# 도대체 왜 runtime error가 뜨는 걸까 미쳐버리겠네
# *b를 통해서 첫째 이후는 b에 가도록 하였다.
a,*b=[eval(s) for s in input().split('-')];print(a-sum(b))



# second try
a,*b=[sum(map(int,s.split('+')))for s in input().split('-')];print(a-sum(b))
