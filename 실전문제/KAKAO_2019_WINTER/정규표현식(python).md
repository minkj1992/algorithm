# 정규표현식 in python


- 숫자 뽑아내기
```python
[int(re.findall('\d+',file)[0]) for file in files]
```
```
in: ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
out: [12, 10, 2, 1, 1, 2]
```
- `findall()`: 매칭된 결과값들을 리스트 형태로 return
```python
[re.findall('\d+',file) for file in files]
```

```
in: ["i19m12g12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
out: [['19', '12', '12'], ['10'], ['02'], ['1'], ['01'], ['2']]
```

- 뽑아낸 숫자를 기준으로 sort하기
```python
a = sorted(files,key=lambda file:int(re.findall('\d+',file)[0]))
```
- 숫자를 기준으로 split() 해주기
```python
[re.split('\d+', file.lower()) for file in files]
```
```
in: ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
out: [['img', '.png'], ['img', '.png'], ['img', '.png'], ['img', '.png'], ['img', '.gif'], ['img', '.jpg']]
```

`sorted`에 `key`로 `lambda key: re.method`를 해주게 되면, erase없이 regex를 사용할 수 있다.


