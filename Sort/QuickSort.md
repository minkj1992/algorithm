# QuickSort
> 기존 merge에 pivot개념을 도입하여 ??

- 퀵 정렬의 내부 loop는 메모리 참조가 지역화 되어 있어, cpu 캐시 히트율이 높기 때문에 효율적이다. 실제구현이??
- 다른 **O(nlogn)** 알고리즘에 비해 훨씬 빠르게 동작한다.
- 정렬을 위하여 **O(logn)** 만큼의 메모리가 필요하다.
- Unstable 하다. 이유는?

# 알고리즘
> `Divide and conquer`

1. `piv` 고르기
2. `Divide` 
  - [left list] + piv + [right list]
  - `left=[i for i in li if i<=piv]`
3. `Conquer`, `Recursion` 
  - 분할된 [left], [right]에 대해 `Recursive`하게 반복한다.
  - `Base`: len(li)<=1
 
 재귀 호출이 한번 진행될때, 최소 하나의 원소는 정렬된다. (Base를 만족할 수 있다.)
 
 

