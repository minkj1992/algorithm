# Counting sort
> 자연수, 정수에서 가능한 sorting 알고리즘, index가 value다 라는 발상의 전혼.

- stable하다.
- 정수 자연수에서 적은 개수의 숫자를 정렬할 때 유용하다.
- 정렬할 때 추가적인 메모리( 숫자 개수를 저장할 공간, 결과를 저장할 공간)가 필요하다
- 가장 큰 숫자에 영향을 받는다.(이는 one hot encoding 처럼 sparse matrix가 생성되고, 공간 활용도가 떨어진다. )

c.f **`차원의 저주`**: 데이터가 커질수록(차원이 커질수록) 훨씬 더 많은 데이터를 가지고도 높은 성능에 이르지 못한다는 점입니다.
즉, 정리해서 이야기하면 우리가 한 샘플을 특정짓기 위해서 많은 양의 정보를 준비할수록 (즉 고차원 데이터일수록) 그 데이터로부터 모델을 학습하기가 훨씬 더 어려워지고 훨씬 더 많은 데이터 양이 필요하게 됩니다

## 첫번쨰 코드
```python
def countingSort(li):
    max_v=max(li)
    
    out_li = [0]*len(li)
    # max value +1 크기의 count_li
    count_li = [0]*(max_v+1)

    # count occurence
    for i in li:
        count_li[i] += 1

    # Update(partial_sum count_li)
    for i in range(max_v):
        count_li[i+1] +=count_li[i]

    for i in li[::-1]:
        out_li[count_li[i]-1] = i
        count_li[i] -= 1
    return out_li

li = []
for _ in range(int(input())):
    li.append(int(input()))

print(*countingSort(li),sep="\n")
```

- list1: out list를 생성하고 복사해준다. 즉 n 만큼의 out_list가 필요하다. 

- list2: count_list를 생성한다. 이때 count list의 크기는 `max_value+1`인데 `+1`은 index가 0부터 시작하기때문에 +1을 해주어 index out of range 방지

- 1) 정렬되지 않은 배열들을 돌아가면서 해당 숫자에 맞는 count_list의 index에 +1씩해준다. 여러개일 경우에 count는 상승한다.

- 2) 이후 count list를 partial sum해주어, index화 시켜준다. 
  - 예를 들어서 [0 1 2 1 0 3 ] -> [0 1 3 4 4 7]  (index 0은 0이 된다. 자연수의 경우일떄)
  - 정렬 해야 될 list에는 0,1,2,2,3,5,5,5 가 정렬 되지 않은 상태로 있는 것이다.  (0 1 3 4 4 7) 

- 3) 역순으로(stable) 배열을 돌아가면서 해당 element가 있는 count 배열을 찾고 해당 값을 index로 sorted list에 넣어준다. 이후 count -=1 해주면 정렬 끝.

- 단점: 공간복잡도가 O(n+k)이다.  

## 두번째 코드

```python
n=MAX_VALUE+1;a=[0]*n;f=open(0);f.readline()
for i in f:a[int(i)]+=1
for i in range(n):print("%s\n"%i*a[i],end="")
```

- 첫번째 코드의 경우의 메모리 낭비를 줄이고자 input을 받으면서 정렬을 실행하였다. 
- 이 코드의 경우는 print 단계에서 index * count 만큼 print하라고 하였다. (즉 stable 인지 아닌지 떠나서 같은 원소 복사 개념으로 접근하여 input()값과 값만 같은 원소이다.)

## 세번째 코드

Negative 처리 가능 코드

### 문제

수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

산술평균 : N개의 수들의 합을 N으로 나눈 값

중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값

최빈값 : N개의 수들 중 가장 많이 나타나는 값

범위 : N개의 수들 중 최댓값과 최솟값의 차이

N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

### 입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

```python
n,m,s,k=8001,4000,0,[];a=[0]*n;N=int(input())
for _ in range(N):i=int(input());a[i+m]+=1;s+=i
for i in range(n): k+=[i-m]*a[i]
print(round(s/N));mm=max(a);idx=[i for i,j in enumerate(a) if j==mm]
if N==1: print(k[0])
else: print(k[(N-1)//2])
if len(idx)==1: print(idx[0]-m)
else: print(idx[1]-m)
print(k[-1]-k[0])
```

- abs값 *2 +1을 하여 2배크기의 배열을 생성해 준뒤 -4000~0~4000 범위를 0~8001로 땡겨주었다.

- 문제점: 문제를 풀다보니까 median과 최빈값 복수개 있을 경우, range 찾기에 문제가 생겼다

- 해결법: idx(max들의 index 리스트), k(정렬된 최종 배열)
