# subtree rooted at index i
# n is size of heap
def heapify(li, n, i):
    # init largest as root
    largest = i
    left = 2*i+1
    right = 2*i+2

    # left child가 존재 하면서, left child 보다 root(li[i])가 작을 경우
    if left<n and li[largest]<li[left]:
        largest = left
    if right<n and li[largest] < li[right]:
        largest = right
    #swap if another max value found
    if largest !=i:
        li[i], li[largest] = li[largest],li[i]
        heapify(li,n,largest)

def heapSort(li):
    n = len(li)
    for i in range(n//2-1,-1,-1):
        heapify(li,n,i)
    for i in range(n - 1, 0, -1):
        li[0], li[i] = li[i], li[0]
        heapify(li, i, 0)       

li = [12,11,13,5,6,7]
heapSort(li)
print(li)


    