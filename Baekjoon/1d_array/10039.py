#평균점수
s = []
for _ in range(5):
  s.append(int(input())
print(sum([i if i>40 else 40 for i in s])//5)
