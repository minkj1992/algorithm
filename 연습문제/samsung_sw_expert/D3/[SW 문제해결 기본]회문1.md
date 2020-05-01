# [S/W 문제해결 기본] 3일차 - 회문1

> [문제링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14QpAaAAwCFAYi)
## 1st try
```python
    for y in range(8-window+1):
        for x in range(8-window+1):
            result+=is_palindrome(y,x,1,window)
            result+=is_palindrome(y,x,0,window)
```
- 위에처럼 해버리면 놓치는 공간이 존재한다.

```python
def is_palindrome(y,x,d,w):
    # 가로: 0 세로: 1
    if d==0:
        arr = [boards[y][nx] for nx in range(x,x+w)]
    else:
        arr = [boards[ny][x] for ny in range(y,y+w)]

    for i in range(w//2):
        if arr[i]!=arr[w-i-1]: return False
    return True

for tc in range(1,2):
    window = int(input())
    boards = [list(input()) for _ in range(8)]

    result = 0
    for y in range(8):
        for x in range(8):
            if y<=8-window:result+=is_palindrome(y,x,1,window)
            if x<=8-window:result+=is_palindrome(y,x,0,window)
    print(f'#{tc} {result}')
```

```java
import java.io.*;

class Solution {
    static final int T = 10;
    static final int N = 8;
    static int window;
    static char[][] board = new char[N][N];


    public static boolean rowCheck(int y, int x) {
        for (int i = 0; i < window / 2; ++i) {
            if (board[y][x + i] != board[y][x + window - 1 - i]) {
                return false;
            }
        }
        return true;
    }

    public static boolean colCheck(int y, int x) {
        for (int i = 0; i < window / 2; ++i) {
            if (board[y + i][x] != board[y + window - 1 - i][x]) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        try (
                BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
                BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out))
        ) {

            for (int tc = 1; tc <= T; ++tc) {
                window = Integer.parseInt(br.readLine());

                for (int row = 0; row < N; ++row) {
                    board[row] = br.readLine().toCharArray();
                }

                int result = 0;
                for (int y = 0; y < N; ++y) {
                    for (int x = 0; x < N; ++x) {
                        if (y + window <= N) {
                            result += (colCheck(y, x) ? 1 : 0);
                        }

                        if (x + window <= N) {
                            result += (rowCheck(y, x) ? 1 : 0);
                        }
                    }
                }
                bw.append("#" + tc + " " + result + "\n");
            }
            bw.flush();
        }
    }

}
```

## 참고할 소스코드
```python
for t in range(1,11):
 
    length = int(input())
 
    board = []
 
    for _ in range(8):
        row = str(input())
        board.append([x for x in row])
        #board([x for x in row])
 
    board_length = 8
 
    count = 0
 
    ## 가로로 확인
    def check_horizontal(x,y):
        global count
 
        ## X가 범위 안에 있어야 없으면 return
        if x > board_length - length or y > board_length -1  :
            return False
 
        odd = length%2
        stack = board[y][x:x+length//2]
        start_idx = x + length // 2
 
        if odd :
            start_idx += 1
 
        for value in board[y][start_idx: x + length]:
            if value != stack.pop():
                return False
        #print("Found",y,x)
        #print(board[y][x:x+length])
 
        count += 1
 
        return True
 
    ## 세로 확인
    def check_vertical(x,y):
        global count
 
        ## X가 범위 안에 있어야 없으면 return
        if y > board_length - length or x > board_length - 1:
            return False
 
        odd = length % 2
 
        stack = []
 
        for idx in range(y, y + length//2):
            #print("index",idx)
            stack.append(board[idx][x])
 
        start_idx = y + length // 2
 
        if odd:
            start_idx += 1
 
        for idx in range(start_idx,y+length):
            value = board[idx][x]
            if value != stack.pop():
                return False
        count += 1
        #print("Found", y, x)
        #print([board[idx][x] for idx in range(y, y+length) ])
        return True
 
 
    for y in range(8):
        for x in range(8):
 
            check_horizontal(y,x)
            #print("Checking Vertically")
            check_vertical(y,x)
 
    if length == 1:
        count = count//2
     
    print("#{} {}".format(t,count))
```

```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
 
public class Solution {
    static char[][] chars = new char[8][8];
 
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int t = 1; t <=10; t++) {
        int n = Integer.parseInt(br.readLine());
            for (int i = 0; i < 8; i++) {
                String l = br.readLine();
                for (int j = 0; j < 8; j++) {
                    chars[i][j] = l.charAt(j);
                }
            }
            int cnt = 0;
            for (int i = 0; i < 8; i++) {
                for (int j = 0; j < 8; j++) {
                    // 세로
                    boolean flagC = true;
                    for (int k = 0; k <= n / 2 && flagC == true; k++) {
                        if (i + n <= 8) {
                            if (chars[i + k][j] != chars[i + n - 1 - k][j])
                                flagC = false;
                        } else
                            flagC = false;
                    }
 
                    if (flagC == true) {
                        cnt++;
                    }
 
                    boolean flagR = true;
                    for (int k = 0; k <= n / 2 && flagR == true; k++) {
                        if (j + n <= 8) {
                            if (chars[i][j + k] != chars[i][j + n - 1 - k])
                                flagR = false;
                        } else
                            flagR = false;
                    }
 
                    if (flagR == true) {
                        cnt++;
                    }
                }
            }
            bw.write("#" + t + " " + cnt+"\n");
            bw.flush();
        }
    }
}
```