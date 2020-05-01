# Radix Sort
> Counting sort에서 k가 커지면 효율이 크게 떨어진다. k를 자릿수로 대체하여 정렬하면 게산복잡성을 낮출 수 있다.

<p align="center"><img src="https://i.imgur.com/gcVBdYZ.png"></p>

- `digit = int(log(max(list), base) + 1)` 입력된 리스트 max value 자릿수 확인
- 숫자에서 각 자릿수 뽑아내는 법: `(number // 진수 ** 원하는 자리) % 진수`

```python
#NOTATION == 진법
#Decimal number = 10
# radix with Integer
def radixNatural(li,NOTATION=10):
    flag = False
    # 자릿수
    power = 1
    while not flag:
        # split into buckets
        buckets = [[] for _ in range(NOTATION)]
        flag = True
        for i in li:
            # 자릿수 뽑아내기
            # find the digit corresponding to radix_power
            #  example with radix_power = 1000; el = 123456
            #  el % (radix_power*RADIX) == 123456 % 10000 == 3456
            #  3456 // radix_power == 3456 // 1000 == 3
            digit = i % (power*NOTATION) // power
            # 0~9 bucket중에서 해당 숫자의 bucket에 넣는다.
            # append 이므로 stable하다.
            buckets[digit].append(i)
            # 어차피 max 찾는데 n 걸리니까, 반복하면서 power*notation보다 큰 i가 존재한다면 loop 반복
            if i >= power*NOTATION:
                flag = False

        # flatten
        li = [el for bucket in buckets for el in bucket]
        # 자릿수 상승(10의자리-> 100의 자리 )
        power *= NOTATION
    return li


def radixInteger(li):
    positive_ints = radixNatural( x for x in li if x >= 0)
    negative_ints = radixNatural(-x for x in li if x <  0)
    return [-x for x in reversed(negative_ints)] + positive_ints

```

- radix의 경우에는 O(n*d) counting의 경우에는 O(n+k)이다. k 가 n보다 작다면 counting이 더 효율적이라고 할 수 있다.
- integer의 경우에는 radixInteger를 사용하면 되고, natural일 경우에는 radixNatural을 사용하면 된다.
