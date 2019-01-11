#190106
#first try
n = input()
for a in range(int(n)):
    j,li =0,[]
    for i in input():
        if i == "X":
            j=0
        else:
            j+=1
        li.append(j)
    print(sum(li))
    
#second try
#input().split('X') == 연속된 'O'를 구할 수 있다.
# n(n+1)//2 == index들의 합
exec("print(sum(len(i)*(len(i)+1)//2 for i in input().split('X')));"*int(input()))
