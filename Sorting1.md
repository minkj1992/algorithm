# Comparison sorting(비교 정렬 알고리즘)

> 두 element의 순서를 비교하는 알고리즘이다.

## Lower Bound
- 이론적으로 Comparison sorting은 worst case O(nlogn)이 lower bound이다.
- 즉 최악의 경우에 nlogn보다 빠르게는 불가능하다.

## 증명
[원본 링크](https://medium.com/@igniter.yoo/algorithms-%EB%B9%84%EA%B5%90-%EC%A0%95%EB%A0%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%98-%ED%95%98%ED%95%9C%EA%B3%BC-%EC%9D%98%EC%82%AC-%EA%B2%B0%EC%A0%95-%ED%8A%B8%EB%A6%AC-4cdd993bf370")

n개를 비교하는 의사 결정 트리에서 가능한 모든 리프의 개수는 n!개입니다. n개에 대한 모든 순열이 존재하기 때문이죠. 그리고 트리의 높이를 h라고 했을 때, 최대 리프의 개수는 이진 트리이므로 2^h개가 됩니다. 즉, 도달 가능한 리프가 L개인 의사 결정트리에서 다음과 같은 식이 성립합니다.

**n! ≤ L ≤ 2^h**

양변에 로그를 취하면,

**h ≥ log(n!) (log 함수는 단조 증가이므로)**

이 되고, n!은 Stirling Equation에 의해 근사되어 h = Ω(n * logn) 이 성립합니다. 
참고로 Stirling Equation은 다음과 같습니다.


  <p align="center">
  Stirling’s Approximation</br>
  <img src="https://cdn-images-1.medium.com/max/800/1*IJihFYuWrYnNicgSYAC5uA.png"></p>

즉, 모든 비교 정렬 알고리즘은 최악의 경우 Ω(n * logn)의 비교가 필요합니다.

## 종류
- Bubble sort
- Selection sort
- Insertion sort
- Shell sort

- Quick sort
- Heap sort

- Cycle sort
- Tim sort

# Non-comparative sorting(비 비교 정렬 알고리즘)

> 특별한 상황에서 사용할 수 있는 sorting 알고리즘으로 비교를 실행하지 않고 정렬을 실행한다. 예를 들어 counting의 경우에는 max value 만큼의 array를 생성하여 해당 array의 index가 elem의 숫자가 되도록 만들어 정렬한다.

- Bucket Sort
- Counting Sort(계수 정렬)
- Radix Sort
