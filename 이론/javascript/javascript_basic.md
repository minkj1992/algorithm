# javascript 알고리즘
## 변수 타입
1. let은 변수에 재할당이 가능하지만,
2. const는 변수 재선언, 재할당 모두 불가능하다.

## for

## stdin
```js
process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
    const n = data.split(" ");
    const a = Number(n[0]), b = Number(n[1]); 
});
```

## Console.log
```js
var time = ["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"];
console.log(solution(time));
```

## Enumerate
```js
const foobar = ['A', 'B', 'C'];

for (const [index, element] of foobar.entries()) {
  console.log(index, element);
}
```