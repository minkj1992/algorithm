# 전형적인 dfs문제

```python
board = [[4,2,3,2],[2,1,2,4],[1,2,3,1],[4,1,4,3]] #-1
# board = [[3,2,3,2],[2,1,1,2],[1,1,2,1],[4,1,1,1]] # 7

def solution(board):
    visited = [[0] * 4 for _ in range(4)]
    result = [-1]
    N = 4

    def is_range(y,x): return (0<=y<4) and (0<=x<4)

    def is_ok(y,x,v):
        ret = []
        for ny,nx in (y,x+1),(y,x-1),(y+1,x),(y-1,x):
            if not is_range(ny,nx): continue
            if visited[ny][nx]: continue
            if board[ny][nx] == v:
                ret.append((ny,nx))
        return ret

    def dfs(y, x, val, r=1):
        ret = r
        visited[y][x] = 1

        for v in is_ok(y,x,val):
            ny,nx = v
            dfs(ny,nx,val,ret+1)

        visited[y][x] = 0
        if ret != 1 and ret>result[0]:
            result[0] = ret



    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                dfs(y,x,board[y][x])
    return result[0]

print(solution(board))

```
```java
class Solution {

    public static final int N = 4;
    public boolean[][] visited = new boolean[4][4];
    public int answer = -1;
    private static int[] dx = {1, -1, 0, 0};
    private static int[] dy = {0, 0, 1, -1};
    public int[][] arr = new int[4][4];


    public void dfs(int y, int x, int val, int ret) {
        visited[y][x] = true;

        for (int i = 0; i < N; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if (!(((0 <= ny) && (ny < N)) && ((0 <= nx) && (nx < N)))) continue;
            if (visited[ny][nx]) continue;
            if (arr[ny][nx] == val) dfs(ny, nx, val, ret + 1);
        }

        if ((ret != 1) && (ret > answer)) {
            answer = ret;
        }
        visited[y][x] = false;
    }

    public int solution(int[][] board) {

        for (int y = 0; y < N; ++y) {
            for (int x = 0; x < N; x++) {
                arr[y][x] = board[y][x];
            }
        }


        for (int y = 0; y < N; ++y) {
            for (int x = 0; x < N; x++) {
                if (!visited[y][x]) {
                    dfs(y, x, board[y][x], 1);
                }
            }
        }

        return answer;
    }

   public static void main(String[] args) {
       Solution sol = new Solution();
//        int[][] board = {{4,2,3,2},{2,1,2,4},{1,2,3,1},{4,1,4,3}};
       int[][] board = {{3,2,3,2},{2,1,1,2},{1,1,2,1},{4,1,1,1}};
       System.out.println(sol.solution(board));

   }
```