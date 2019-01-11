# `Shell sort(쉘 정렬)` ![](https://latex.codecogs.com/gif.latex?%5Cinline%20O%28n%5E%7B2%7D%29)
> `Insertion sort`의 개선버전\
정렬되지 않은 배열의 경우 비효율적으로 되는 insertion의 단점을 `gap`을 통하여 개선하였다.

- 삽입정렬의 최대 문제점은 바로 요소들이 삽일 될 위치가 +1씩 움직인다는 것이다.(이러한 이유로 내림차순 정렬일 경우네는 n^2이 되는 것)
- `shell sort`의 경우에는 gap을 따라가면서 sublist(n/gap)를 생성한다. 
- number of sublist = |gap|

# `셸 정렬` 구체적 개념

- gap 의 초깃값: n/2((n//2+1) if n%2==1)
- gap, gap//2, gap//4 순으로 gap이 1이 될때까지 반복한다.

순서
1) gap을 정한다.
2) 0, 0+gap, 0+gap+gap index를 따라가면 sublist한개를 만들고 이를 0~gap-1까지 돌면서 sublist들을 만든다.(gap만큼의 sublist 생성)
3) 각 sublist들



