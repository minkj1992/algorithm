# `Selection Sort` ![](https://latex.codecogs.com/gif.latex?%5Cinline%20O%28n%5E%7B2%7D%29)
> 선택적으로 loop당 최종 max값만 swap한다.\
버블정렬을 일부 개선한 알고리즘.\
정렬 순서가 맞지 않으면 무조건 자리를 바꿔줬던 버블과 달리
iteration마다 max를 찾고 단 한번만 `swap()`

- 버블에 비하여 swap이 적다.
- comparison은 버블과 동일하다.
- n번의 swap, ![](https://latex.codecogs.com/gif.latex?%5Cinline%20n%5E%7B2%7D)의 comparison

```python
def selectionSort(li):
    for sorted_num in range(len(li)-1):
        # comparison
        # start는 항상 0, 비교대상은 i+1부터(i는 항상 0으로 고정)
        max_idx=0
        for i in range(len(li)-1-sorted_num):
            if li[max_idx]<li[i+1]:
                max_idx = i+1
        #swap
        #trick: -sorted_num을 사용하여 뒤에서 부터 max가 들어가도록 하였다.]
        li[-(sorted_num+1)],li[max_idx]=li[max_idx],li[-(sorted_num+1)]
    return li

```
