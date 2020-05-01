def solution(board, moves):
    stack = []
    answer = 0
    N = len(board)
    visited = [0]*N
    for x in moves:
        x-=1
        if visited[x]:continue
        for y in range(N):
            if board[y][x]:
                if stack and stack[-1]==board[y][x]:
                    answer+=2
                    stack.pop()
                else:
                    stack.append(board[y][x])
                board[y][x]=0
                break
        else:
            visited[x]=1
    return answer