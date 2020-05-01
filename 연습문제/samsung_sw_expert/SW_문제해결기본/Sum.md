# [S/W 문제해결 기본] 2일차 - Sum

> [Brute Force],[문제 URI](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV13_BWKACUCFAYh&probBoxId=AV6kld8aiskDFASb&type=PROBLEM&problemBoxTitle=%EC%82%BC%EC%84%B1%EC%8B%9C%ED%97%98%EB%8C%80%EB%B9%84+%EA%B8%B0%EB%B3%B8%EB%AC%B8%EC%A0%9C%EB%AA%A8%EC%9D%8C%28%EB%82%9C%EC%9D%B4%EB%8F%84+1~3%29&problemBoxCnt=15)
# `1st try`
- **`Before try`(`접근법`)**
  - `Condition(주의할 문제조건)`
    - `cond1`   배열의 크기는 100X100으로 동일하다.
    - `cond2`   각 행의 합은 integer 범위를 넘어가지 않는다.
    - `cond3`   **대각선은 최대 길이만 고려하는 건가?**
    - `INPUT:` 2차원 배열의 각 행 값
    - `OUTPUT:` 가로 세로 대각선 max
  - `Variables(변수: 데이터타입)`
    - `findsum((dir))`:주어진 direction에 대하여 sum값을 return
    
  - `Algorithm`
    - 가로,세로,대각선*2 해주면 끝
    - **여기서 간과한점은 대각선 길이가 가장 큰것이 대각선 max()의 최적해가 아니라는 점.**

```python
def find_sum():
    ret = []
    # 가로
    for row in matrix:
        ret.append(sum(row))
    # 세로
    for col in zip(*matrix):
        ret.append(sum(col))
    # 대각선
    
    for y in range(10):
        tmp = 0
        x = 9-y
        tmp+=matrix[y][x]
        ret.append(tmp)
    for y in range(10):
        tmp = 0
        tmp+=matrix[y][y]
        ret.append(tmp)
    return max(ret)

if __name__ == '__main__':
    N = 10
    WIDTH = 100
    HEIGHT = 100
    for n in range(N):
        _ = input()
        matrix = [list(map(int,input().split())) for i in range(100)]
        result = find_sum()
        print("#"+str(n+1)+" "+str(result))
```

- **After try(회고)**
- time: `O(2*n^2 + 2*sqrt(n))` ~ `O(n^2)`
- space: `O(n^2)`
- python 대각선 계산하는 쉬운 방법 없을까?

# `2nd try`
- 대각선 간소화 시킴
```python
    # 대각선
    ret.append(sum([matrix[y][10-(y+1)] for y in range(10)]))
    ret.append(sum([matrix[y][y] for y in range(10)]))
```

```python
def find_sum():
    ret = []
    # 가로
    for row in matrix:
        ret.append(sum(row))
    # 세로
    for col in zip(*matrix):
        ret.append(sum(col))
    # 대각선
    ret.append(sum([matrix[y][10-(y+1)] for y in range(10)]))
    ret.append(sum([matrix[y][y] for y in range(10)]))
    
    return max(ret)

if __name__ == '__main__':
    N = 10
    for n in range(N):
        _ = input()
        matrix = [list(map(int,input().split())) for i in range(100)]
        result = find_sum()
        print("#"+str(n+1)+" "+str(result))
```

## 3rd try (200125)

```python
for tc in range(1,11):
    _ = input(); N = 100
    board = [list(map(int,input().split())) for _ in range(N)]

    ret = [0]*(2*100+2)
    for y in range(N):
        ret[y] = sum(board[y])
        for x in range(N):
            if y==x: ret[200]+=board[y][x] #우측 대각선
            if x==(N-1-y): ret[201]+=board[y][x] #좌측 대각선
            ret[x+N]+=board[y][x]
    
    print(f'#{tc} {max(ret)}')
```
- 기존 대각선 방법은 틀렸다. 10이아니라, 100으로 해야된다.

```java
    public static void main(String[] args) {
                //...중략...
                int[][] arr = new int[N][N];
                for (int y = 0; y < N; y++) {
                    String[] line = br.readLine().split(" ");
                    for (int x = 0; x < N; x++) {
                        arr[y][x] = Integer.parseInt(line[x]);
                    }
                }
```
- max 구하는 법을 몰라서, 함수 만들어서 구했다.
- 밑에 upgrade 버전 (`StringTokenizer`를 사용)
    - 20ms 시간 단축과 3,000kb 메모리 단축

```java
import java.io.*;
import java.util.StringTokenizer;

class Solution {

    public static final int T = 10;
    public static final int N = 100;

    public static int max(int[] arr) {
        int maxValue = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > maxValue) maxValue = arr[i];
        }
        return maxValue;
    }

    public static void main(String[] args) {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
             BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out))) {
            for (int tc = 1; tc <= T; tc++) {
                br.readLine(); // trash

                int[] rows = new int[N], cols = new int[N], diags = new int[2];
                for (int y = 0; y < N; y++) {
                    StringTokenizer st = new StringTokenizer(br.readLine());
                    for (int x = 0; x < N; x++) {
                        int num = Integer.parseInt(st.nextToken());
                        if (y == x) diags[0] += num;
                        if (y + x == N - 1) diags[1] += num;
                        rows[y] += num;
                        cols[x] += num;
                    }
                }
                int result = max(new int[]{max(rows), max(cols), max(diags)});
                bw.write("#" + tc + " " + result + "\n");
            }
            bw.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

## 공부할 java 소스코드

```java
import java.io.*;
import java.util.Arrays;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.StringTokenizer;
 
public class Solution {
     
    static int T;
    static int result;
 
    /**
     * @param args
     * @throws IOException 
     * @throws NumberFormatException 
     */
    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub
 
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = 10;
         
        for (int i = 0; i < T; i++)
        {
            br.readLine();
            int[] rowSum = new int[100];
            int[] colSum = new int[100];
            int[] diagonalSum = new int[2];
             
             
            for(int j=0; j<100; j++)
            {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for(int k=0; k<100; k++)
                {
                    int num = Integer.parseInt(st.nextToken());
                    rowSum[j] += num;
                    colSum[k] += num;
                    if((j-k) ==0)
                    {
                        diagonalSum[0] += num;
                    }
                    else if((j+k) ==100)
                    {
                        diagonalSum[1] += num;
                    }
                }
            }
             
            int maxSum = 0;
            for(int j=0; j<rowSum.length; j++)
            {   
                if(rowSum[j] > maxSum)
                {
                    maxSum = rowSum[j];
                }
            }
            for(int j=0; j<colSum.length; j++)
            {
                if(colSum[j] > maxSum)
                {
                    maxSum = colSum[j];
                }
            }
            for(int j=0; j<diagonalSum.length; j++)
            {
                if(diagonalSum[j] > maxSum)
                {
                    maxSum = diagonalSum[j];
                }
            }
             
            result = maxSum;
            System.out.println("#" + (i+1) + " " + result);
        }
    }
     

}
```
