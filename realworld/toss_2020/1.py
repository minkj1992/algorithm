arr = input().split()
weight = (8, 5, 2, 4, 3, 7, 6, 1, 0, 9)
weight_dict = {str(w): v for v, w in zip(range(10), weight)}

raw_result = sorted([(weight_dict[a],a) for a in arr])
result = [i[1] for i in raw_result]
print(' '.join(map(str, result)))
