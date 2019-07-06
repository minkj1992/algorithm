# 1st try
- `[1...13]` * 7
- `output`
    - 0
        - 같을경우
    - 1
        - arr1이 클경우
    - 2
        - arr2 클경우

- `숫자페어가 2벌이 나오는 경우에는 더 큰 숫자로 되어있는 페어만 고려한다`
    - 그렇다면 arr1Dic에서 뒤에부터 2이상인 숫자 weight return
    - 아무리 페어 등수가 높아도, 숫자가 작다면 큰 숫자로 return 한다는 뜻이지?
    - 위에 의견이 틀린듯 pair 등수가 큰 수로

- `페어 등수(2,3,4)`
    - 4이상부터는 모두 같은 등수

- `weight`
    - (페어등수,숫자)


- 주의점
    - 만약 4개 이상인 녀석들이 오면 큰 숫자로 정렬해야 한다.


- `접근법`
    - 
```python
from collections import defaultdict
def solution(arr1,arr2):
    arr_dic1 = defaultdict(list)
    arr_dic2 = defaultdict(list)
    # {값:[pair,값]}
    for arr_dic,arr in [(arr_dic1,arr1),(arr_dic2,arr2)]:
        for i in arr:
            if arr_dic[i]==[]:
                arr_dic[i]=[1,i]
            else:
                arr_dic[i][0]= min(4,arr_dic[i][0]+1)

    # for i in arr2:
    #     if arr_dic2[i]==[]:
    #         arr_dic2[i]=[1,i]
    #     else:
    #         arr_dic2[i][0]= min(4,arr_dic2[i][0]+1)
    # 만약 값이 없으면?
    # sorted(list(arr_dic1.keys()), key= lambda x: arr_dic1[x])
    one = max(arr_dic1.values())
    two = max(arr_dic2.values())
    print(arr_dic1)
    print(arr_dic2)
    print(one,two)
    #  페어가 없을 경우
    if one[0] == two[0] == 1:
        return 0

    if one>two:
        return 1
    elif one<two:
        return 2
    else: return 0
    
    
# a = [1, 2, 3, 4, 9, 10, 11]
# b = [1, 2, 3, 4, 5, 6, 7]
# a=[1, 2, 2, 2, 2, 2, 5]
# b= [4,4,4,4,5,6,7]
a = [1, 2, 3, 4, 5, 6, 7]
b = [1,1,1, 2, 3, 4, 5, 5, 6,6]
print(solution(a,b))
    
```


# 2nd try

[링크](https://drive.google.com/drive/u/1/folders/14o1cdGnjJ-Q6jsB96LHQxeGOCRMPZxkm)