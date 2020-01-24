# [S/W 문제해결 기본] 1일차 - Flatten

> [알고리즘 분류],[문제 URI](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV139KOaABgCFAYh&probBoxId=AV6kld8aiskDFASb&type=PROBLEM&problemBoxTitle=%EC%82%BC%EC%84%B1%EC%8B%9C%ED%97%98%EB%8C%80%EB%B9%84+%EA%B8%B0%EB%B3%B8%EB%AC%B8%EC%A0%9C%EB%AA%A8%EC%9D%8C%28%EB%82%9C%EC%9D%B4%EB%8F%84+1~3%29&problemBoxCnt=15)


# `1st try`
- **`Before try`(`접근법`)**
  - `Condition(주의할 문제조건)`
    - `cond1`
        - 가장 높은 곳에 있는 상자를 가장 낮은 곳으로 옮기는 작업을 덤프라고 정의한다.
        - 덤프시 높이에 따른 `weight`존재 x
    - `cond2`
        - 주어진 덤프 횟수 이내에 평탄화가 완료되면 더 이상 덤프를 수행할 수 없으므로 그 때의 최고점과 최저점의 높이 차를 반환한다 (주어진 data에 따라 0 또는 1이 된다).
            - 1이 되는 경우가..? `평탄화: 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.`
    
    - `INPUT:` 
    - `OUTPUT:` 최고점과 최저점의 높이 차를 출력
  - `Variables(변수: 데이터타입)`
    - `Height` = 높이를 index로 하는 counter List
    - `counter` = index가 높이, value가 갯수 (문제 조건에 height max가 100이라 하였으니 가능)
    - `box`: 옮길 box의 갯수

  - `Algorithm`
    - counter의 max_idx와 min_idx를 사용하여, 각자 box 갯수와 dump 갯수중 작은 수만큼 box를 옮긴다.
    - `base condtion`:
        - 1) dump가 0이 될 경우
        - 2) max_idx - min_idx <= 1

    - `update index`
        - `if  counter[min]==0 or counter[max]==0`
        - 해당 index 업데이트 후 `continue`

    - `update counter`
        - `box = min(counter[min_idx],counter[max_idx],dump)` 
        - dump -= box
        - counter[min] -= box
        - counter[min+1] += box
        - counter[max] -= box
        - counter[max-1] += box


    - `return max_idx-min_idx`
    
  

```python
def find_dif_height(dump):
    # print(counter)
    max_idx = len(counter)-1
    min_idx = 0
    
    while True:
        # base condtion 1
        if (max_idx-min_idx <= 1): break # 1 이하 차이날 경우(Flatten)
        # update index
        if counter[min_idx]==0:min_idx+=1;continue
        if counter[max_idx]==0:max_idx-=1;continue
        # 이게 idx update보다 위에 나오면, index update 없이 값이 print 된다. 즉 box가 0인 녀석의 index값이 print 된다.
        if (dump==0): break # base condtion 2
        
        # update counter
        box = min(counter[min_idx],counter[max_idx],dump) 
        dump-=box
        counter[min_idx]-=box
        counter[min_idx+1]+=box # 작은녀석에 상자가 더해지면, 그보다 1큰 상자들 갯수가 +된다   
        counter[max_idx]-=box
        counter[max_idx-1]+=box
    
    return max_idx-min_idx

if __name__ == '__main__':
    N = 10
    for n in range(N):
        dump = int(input())
        MAX_HEIGHT = 100
        height = []
        counter = [0,]*(MAX_HEIGHT+1)
        for h in map(int,input().split()):
            height.append(h)
            counter[h]+=1
        result = find_dif_height(dump)

        print("#"+str(n+1)+" "+str(result))
```
- **After try(회고)**
- time: `O(n)`
- space: `O(n+100)` -> `O(n)`
- `while`을 돌면서 `if`를 4번 하는게 최선일까?

## 2nd try (x)

```python
from collections import deque

f = open('tmp.txt','r')
input = f.readline 

for tc in range(1,11):    
    dump = int(input())
    
    counter = {}
    for b in list(map(int,input().split())):
        if counter.get(b,-1) == -1:
            counter[b] = 1
        else:
            counter[b]+=1
    
    boxes = deque([k,counter[k]] for k in sorted(counter.keys()))

    result = 0
    while len(boxes)>1:
        l,r = boxes[0],boxes[-1] #popleft할때 달라질까? ref일까 val일까?
        print(boxes)
        if l[1]<r[1]:
            boxes.popleft()
            boxes[-1][1]-=l[1]
            boxes[0][1]+=l[1]
            dump-=l[1]
        else:
            boxes.pop()
            boxes[0][1]-=r[1]
            boxes[1][1]+=r[1]
            dump-=r[1]

        if dump <= 0:
            result = r[0]-l[0]
            break
    print(f'#{tc} {result}')


f.close()

```