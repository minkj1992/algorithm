#190106
#input을 한번에 받고 싶었는데 stdin의 경우에는 import에 의한 오버헤드발생
#first try
a = [0]*10
for i in (list(str(int(input())*int(input())*int(input())))):
    a[int(i)]+=1
# 반복문을 쓰지 않고 list a를 돌면서 \n을 붙이는 방법.
print("\n".join(map(str,a)))

#second try
#input에 ()를 붙이지 않으면 버퍼크기만큼 한번에 데이터를 받을 수 있다.
k=input
a = str(int(k())*int(k())*int(k()))
for i in range(10):
#count를 통하여 i의 갯수를 샌다.
    print(str(a).count(str(i)))
    
# short coding
#exec
m=1;exec(3*'m*=int(input());')
for i in range(10):print(str(m).count(str(i)))
