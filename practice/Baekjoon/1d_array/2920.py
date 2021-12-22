#input:1 2 3 4 5 6 7 8
#out:ascending or descending or mixed

#first try
#string의 경우도 sorted가 가능하다.
#list 굳이 씌우지 않아도 split() return 값이 list
a=list(input().split())
if a == sorted(a):
    print("ascending")
# reversed의 경우에는 틀렸다 나왔는데 sorted true하니까 정답처리되었다.
elif a == sorted(a,reverse=True):
    print("descending")
else:
    print("mixed")
    
#second try
#asc, dsc 모두 경우의수가 1개밖에 없었네
# set에서 else 는 변수로 두는 trick
#[2::2]인 이유는 ' '이 중간중간에 섞여있기때문에
a=input()[2::2];print({a:"mixed","2345678":"ascending","7654321":"descending"}[a])

#third try
#3항 연산자
l=input()[2::2];print('ascending'if l=='2345678'else'descending'if l=='7654321'else'mixed')
  
  
