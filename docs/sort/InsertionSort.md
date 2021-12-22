# `Insertion sort` ![](https://latex.codecogs.com/gif.latex?%5Cinline%20O%28n%5E%7B2%7D%29)
> `insert()`하면서 정렬을 시행한다.\
당연히 앞에서부터 작은 순서대로 정렬이 시행된다.\
[정렬된 배열]에 [insert_ele]가 들어간다.

- 이미 정렬된 상태라면 `O(n)`의 빠른 속도를 보이지만, 그렇지 않은 경우에는 
- 정렬된 상태에서 빠른 이유는 각 insert마다 1번의 비교만 하면 되기 때문이다.
- ins >= sorted_list[::-1]
- 단점: 삽입을 하게 되면 데이터가 하나씩 뒤로 밀려야 되기 때문에 배열이 길어질수록 효율이 떨어진다.
- 개인적으로 input()받을 때 insertionSort를 사용하면 입력과 정렬을 동시에 할 수 있어서 더욱 효율적인 것 같다.

```python
def insertionSort(sorted_li,ins):
    # for .insert()
    # len()를 indx로 잡을 경우 insert할때 맨 뒷부분 부터 insert된다.
    indx = len(sorted_li)
    #first try just insert
    if indx==0:
        sorted_li.append(ins)
        return
    
    #sorted_li의 뒤쪽부터 ins와 comparison
    for i in sorted_li[::-1]:
        # =를 포함하므로 stable하다.
        if ins>=i:
            # indx를 줄이지 않고 for 문을 빠져나온다.
            break
        indx-=1
    sorted_li.insert(indx,ins)


sorted_li = []
for _ in range(int(input())):
    insertionSort(sorted_li,int(input()))
print(*sorted_li,sep='\n')

```
