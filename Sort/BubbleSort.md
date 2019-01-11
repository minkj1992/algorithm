# `Bubble sort`![](https://latex.codecogs.com/gif.latex?%5Cinline%20O%28n%5E%7B2%7D%29)
> 0~n-1의 pivot으로 부터 2개씩 비교하여, 가장 큰 수(맨 오른쪽 부터) 정렬하는 방법.
- 추가적인 mem이 필요하지 않다.
- loop 한번 마다 마지막 하나가 정렬된다.(가장 큰 값부터 정렬된다.)
- 어느정도 정렬된 데이터에선 효율적으로 사용된다. `O(n)`

```python
# len()-1 = idx화, 만약 i+1까지 비교하지 않는다면 그냥 range(len(S))
for sorted_num in range(len(S)-1):
    # n-1번 큰 녀석들을 찾는다.
    # sorted_num = 기존에 정렬된 요소 갯수.
    # len(S)-1-sorted_num = n-1개 정렬하면 되는데, 그중에서 정렬된 요소들 삭제한 만큼 비교
    for i in range(len(S)-1-sorted_num):
        if S[i]>S[i+1]:
            #swap
            S[i],S[i+1]=S[i+1],S[i]   
```
