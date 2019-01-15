[출처](https://ratsgo.github.io/data%20structure&algorithm/2017/09/27/heapsort/)

# Heap
> complete binary tree(heap shape property) + Heap property(heap order propertry)

힙은 우선 순위가 큰 키에 자주 액세스하거나 우선순위 중심으로 정렬된 시퀀스를 활용해야 할 때 유용한 자료구조이다.
힙은 한 node에 최대 두개의 child node를 가지며, 마지막 레벨을 제외한 모든 레벨에서 node들이 꽉 채워진 complete binary tree이다.

- 단순히 최댓값(최솟값)을 O(1) 안에 찾기 위해서라면, "Complete binary tree" 특성을 만족시킬 필요는 없다.
- `Complete binary tree`를 사용하는 이유는 `삽입/삭제`의 속도 때문이다.

## 특징 
- 힙에서는 가장 높은 우선순위를 가지는 노드가 항상 root node에 오게 되는 특징이 있으며, 이를 응용하면 priority queue와 같은 ADT를 만들 수 있다.
- `minHeap` : 맨 위에 가장 작은 값
- `maxHeap`: 맨 위에 가장 큰 값

- 삽입/삭제 : `O(logN)`

- 힙의 시간복잡성은 O(log n) 이다.

## 데이터 삽입
1. 가장 끝의 자리에 노드를 삽입한다.

2. 그 노드와 부모 노드를 서로 비교한다.

3. 규칙에 맞으면 그대로 두고, 그렇지 않으면 부모와 교환한다.

4. 규칙에 맞을 때까지 3번 과정을 반복한다.

![](http://www.cprogramming.com/tutorial/computersciencetheory/heapadd.jpg)

## 데이터 삭제[편집]
최댓값 혹은 최솟값이 저장된 루트 노드만 제거할 수 있다.

1. 루트 노드를 제거한다.

2. 루트 자리에 가장 마지막 노드를 삽입한다.[3]

3. 올라간 노드와 그의 자식 노드(들)와 비교한다.

4. 조건에 만족하면 그대로 두고, 그렇지 않으면 자식과 교환한다.

    - 최대 힙
        - 부모보다 더 큰 자식이 없으면 교환하지 않고 끝낸다.
        - 부모보다 더 큰 자식이 하나만 있으면 그 자식하고 교환하면 된다.
        - 부모보다 더 큰 자식이 둘 있으면 자식들 중 큰 값과 교환한다.

    - 최소 힙
        - 부모보다 더 작은 자식이 없으면 교환하지 않고 끝낸다.
        - 부모보다 더 작은 자식이 하나만 있으면 그 자식하고 교환하면 된다.
        - 부모보다 더 작은 자식이 둘 있으면 자식들 중 작은 값과 교환한다.

5. 조건을 만족할 때까지 4의 과정을 반복한다.

![](http://www.cprogramming.com/tutorial/computersciencetheory/heapremove.jpg)


## Heap property

1. `Heap order property`: 뿌리노드를 제외한 각 내부노드는 key(T.parent(v)) < key(v) 또는 key(T.parent(v)) > key(v)이다. (즉, 키 값은 오름차순이거나 내림차순이다.)

2. `Heap shape property`: 모양은 완전이진트리이다. 즉 마지막 레벨의 모든 노드는 왼쪽에 쏠려 있다.


# Heap vs Binary Search Tree

아래 그림은 이진탐색트리(Binary Search Tree)를 나타내고 있습니다. 
힙과 이진탐색트리 모두 이진트리라는 점에서 공통점을 가지만 노드값이 다소 다르게 구성돼 있는 점을 확인할 수 있습니다. 
힙은 각 노드의 값이 자식노드보다 큰 반면, 이진탐색트리는 왼쪽 자식노드가 제일 작고 부모노드가 그 다음 크며 오른쪽 자식노드가 가장 큰 값을 가집니다. 힙은 우선순위(키) 정렬에, 이진탐색트리는 탐색에 강점을 지닌 자료구조라고 합니다.

![](https://i.imgur.com/YmnDkvE.png)

# Heap을 Array로 표현

> 힙은 완전이진트리(complete binary tree) 성질을 만족하기 때문에 다음처럼 1차원 배열(array)로도 표현이 가능합니다.

![](https://i.imgur.com/3sUWVY2.png)

    left_index = 2 * index + 1
    right_index = 2 * index + 2

# Heapify

# Heap Sort 

> **O(nlogn)**

1. 주어진 원소들로 최대 힙을 구성합니다.(heapify, O(logn))
2. 최대 힙의 루트노드(=현재 배열의 첫번째 요소=최댓값)와 말단노드(=현재 배열의 마지막 요소)를 교환해 줍니다.
3. 새 루트노드에 대해 최대 힙을 구성합니다.(heapify)
4. 원소의 개수만큼 2와 3을 반복 수행합니다.O(n)






[힙을 사용하는 이유](https://skydrm.wordpress.com/2009/10/31/%ED%9E%99-%EC%9E%A5%EC%A0%90%EA%B3%BC-%EB%8B%A8%EC%A0%90/)
