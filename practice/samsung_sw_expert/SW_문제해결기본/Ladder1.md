# Ladder1
> 

## 1st try (19.08.31)
```python
def search(x):
    result = x
    for y in range(100):
        if ladders[y][x]==2:
            return result
        # search
        left_cond = x and ladders[y][x-1]
        right_cond = x<99 and ladders[y][x+1]
        if left_cond:
            while x and ladders[y][x-1]:
                x -= 1
        elif right_cond:
            while x<99 and ladders[y][x+1]:
                x += 1
    return -1

for tc in range(10):
    input()
    ladders = [list(map(int,input().split())) for _ in range(100)]
    for x in range(100):
        if ladders[0][x]:
            result = search(x)
            if result!=-1:
                break
    print(f'#{tc+1} {result}')
```
## 2nd try (19.10.27)
```python
for tc in range(1,11):
    input() # trash
    boards = [list(map(int,input().split())) for _ in range(100)]
    goal = [i for i,v in enumerate(boards[-1]) if v==2][0]
    ladder_idx = [i for i,v in enumerate(boards[0]) if v]
    ladders = ladder_idx[:]
    for row in boards[:-1]:
        for swap_idx,v in enumerate(ladder_idx[1:]):
            if row[v-1]:
                ladders[swap_idx],ladders[swap_idx+1] = ladders[swap_idx+1],ladders[swap_idx]
    result = ladders[ladder_idx.index(goal)]
    print(f'#{tc} {result}')
```

## 3rd try (20.01.25)
