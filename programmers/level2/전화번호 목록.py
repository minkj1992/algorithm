# first try
def solution(phone_book): 
    for i in range(len(phone_book)): 
        pivot = phone_book[i] 
        for j in range(i+1, len(phone_book)): 
            strlen = min(len(pivot), len(phone_book[j])) 
            if pivot[:strlen] == phone_book[j][:strlen]: return False 
            
    return True

# 2nd try
def solution(phone_book):
    num = len(phone_book) 
    for i in range(num):
        for j in range(i+1,num):
            flag =False
            for a,b in zip(phone_book[i],phone_book[j]):
                if a!=b:
                    flag = True
                    break
            # 계속 false로 있으면(접두어 존재)
            if not flag: return flag
    return flag
