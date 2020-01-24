# [S/W 문제해결 기본] 1일차 - View
> [Brute force, search], [Link](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV134DPqAA8CFAYh&probBoxId=AV6kld8aiskDFASb&type=PROBLEM&problemBoxTitle=%EC%82%BC%EC%84%B1%EC%8B%9C%ED%97%98%EB%8C%80%EB%B9%84+%EA%B8%B0%EB%B3%B8%EB%AC%B8%EC%A0%9C%EB%AA%A8%EC%9D%8C%28%EB%82%9C%EC%9D%B4%EB%8F%84+1~3%29&problemBoxCnt=15) 

# `1th try`
- **`Before try`(`접근법`)**
    - `condition(주의할 문제조건)`
        - `cond1`
            - 맨 왼쪽 두 칸과 맨 오른쪽 두 칸에는 건물이 지어지지 않는다. 
                - piv 기준 오른쪽 2개 search 한다면 `[2:n-4]`
    - `input:` 0<=정수<=255
    - `output:` sum(조망세대)
    - `variables(변수: 데이터타입)`
        - `height` : 높이저장 list
        - `dp` : 최적 조망세대 값저장 list
        - `find_match_height()`: return sum(dp)
    - `algorithm`
        - `for i in [2:n-4]`를 돌면서 `sorted(height[i],height[i+1],height[i+2])`
        - `if height[i]==max_height`
            - `dp[i+mov] = min(기존값,max_height-2번째 큰값)`
        - `else`
            - `dp[i+mov] = min(dp[i+mov],max(0,height[i+mov]-max_height))`


  

```python
def find_match_height(length):
    for i in range(2,length-4):
        sort_value = sorted([height[i],height[i+1],height[i+2]])
        max_height = sort_value[-1]
        # update
        for mov in range(3):
            exrta_value = height[i+mov]-max_height
            if exrta_value == 0:
                dp[i+mov] = min(dp[i+mov],max_height-sort_value[1])
            else:
                dp[i+mov] = min(dp[i+mov],max(0,exrta_value))
    return sum(dp)

if __name__ == '__main__':
    N = 10
    for n in range(N):
        length = int(input())
        height = list(map(int,input().split()))
        dp = height[:]
        result = find_match_height(length)
        print("#"+str(n+1)+" "+str(result))
```

- **`After try(회고)`**
    - time: `O((N-6)*3)`
    - space: `O(2N)`


## 2nd try (200124)
```python
for tc in range(1,11):    
    N = int(input())
    height_arr = list(map(int,input().split()))
    result = height_arr[:]
    
    for i in range(2,N-4):
        mid = sorted(height_arr[i:i+3])[1]
        for j in range(3):
            result[i+j] = max(0,min(result[i+j],height_arr[i+j]- mid))
    print(f'#{tc} {sum(result)}')
```

```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class Solution {

    public static void main(String[] args){
        try (
                BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
                BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ) {

            for (int tc = 1; tc <= 10; ++tc) {
                int N = Integer.parseInt(br.readLine());
                int[] heightArr = new int[N];
                String[] line = br.readLine().split(" ");
                for (int i = 0; i < N; ++i) {
                    heightArr[i] = Integer.parseInt(line[i]);
                }

                int result = 0;
                for (int j = 2; j < N - 2; j++) {
                    if (heightArr[j] > heightArr[j - 2] && heightArr[j] > heightArr[j - 1]
                            && heightArr[j] > heightArr[j + 1] && heightArr[j] > heightArr[j + 2]) {
                        int max = Integer.max(heightArr[j - 2], Integer.max(heightArr[j - 1], Integer.max(heightArr[j + 1], heightArr[j + 2])));
                        result += heightArr[j] - max;
                    }
                }
                bw.write("#" + tc + " " + result + "\n");
            }
            bw.flush();
        } catch (
                IOException e) {
            e.printStackTrace();
        }
    }

}
```
- bw.append 보다 bw.write가 더 현명하다. ( append return overhead )

- mem 1등, time 4등