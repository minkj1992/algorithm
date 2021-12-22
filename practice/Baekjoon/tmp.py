h,m = map(int,input().split())
sum = 60*h+m-45
if sum<0:print(23,60+sum)
else:print(sum//60,sum%60)