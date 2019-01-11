#처음에 이해한바는 대문자가 있을경우에는 대문자로 대문자가 없을 경우에는 소문자로 해야 된다 생각해서 logic을 복잡하게 짰다.
#그러나 그냥 무조건 대문자 반환 또는 2이상일 경우에는 ?로 반환해야 된다는 것을 아니까 허탈하다.
b = "Mississipi"
a = dict.fromkeys(b, 0)
for i in b:
    a[i]+=1
    if i.islower():
        if a.has_key(i.upper()):
            a[i.upper()]+=1
    else:
        if a.has_key(i.lower()):
            a[i.lower()]+=1

max_v=max(a.values())
li=[i for i,j in a.items() if j==max_v]
if len(li)==1:
    print(li[0])
else:
    low_li=set([i.lower() for i in li])
    if len(li)-1==len(low_li):
        print(li[0].upper())
    else:
        print("?")
    

#추가적으로
abs(대문자-소문자)==32이면 대소문자 관계이다.
elif len(li)==2:
    if (abs(ord(li[0])-ord(li[1]))==32):
        print(li[0].upper())
    else:
        print("?")
        
        
#second try
#모두 upper로 생성하고 코드를 짰다.
b = input().upper()
a = dict.fromkeys(b, 0)
for i in b:
    a[i]+=1
max_v=max(a.values())
li=[i for i,j in a.items() if j==max_v]
if len(li)==1:
    print(li[0])
else:
    print("?")

    
