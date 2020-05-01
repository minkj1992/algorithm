# tmp

```python
# # from collections import deque
# # # t: min
# # # n:
# # def solution(n, t, m, timetable):
# #     # 시간에 관계없이 못타는 인원 삭제 (n*m-1)
# #     timetable = sorted(timetable)[:n*m-1]
# #     queue = deque(timetable)
# #     time = 9*60
# #     while queue:
# #
# #
# #
# #     answer = ''
# #     return answer
# #
# # # 1. timetable을 sort시킨다.
# # # 2. bus = dict(시간:life)
# # solution(1,1,5,['08:00', '08:01', '08:02', '08:03'])
#
# #
# # from math import ceil,floor
# # def solution(lines):
# #     new_lines = []
# #     for line in lines:
# #         time,dur = line[11:].split()
# #         h,m,s = time.split(':')
# #         new_lines.append([int(h),int(m),float(s),float(dur[:-1])])
# #
# #     times = [[[0 for _ in range(60)] for _ in range(60)] for _ in range(24)]
# #     for line in new_lines:
# #         print()
# #         print()
# #
# #         h,m,s,d = line
# #         d -= 0.001
# #         # (d의 소숫점이 더 크다면)
# #         # print(int(str(s).split('.')[1]),int(str(d).split('.')[1]))
# #         extra = 1 if int(str(s).split('.')[1][:3])<int(str(d).split('.')[1][:3]) else 0
# #         print(extra)
# #         k = int(d)+extra
# #         # k =  abs(floor(s-d)) if s<=d else int(s)-int(s-d)
# #         print("##########",k,s,d,"##########")
# #         total = 3600 * h + 60 * m + int(s)
# #         for mm in range(k+1):
# #             total-=mm
# #             tmp_total = total
# #             tmp_list = [0] * 3
# #             for i in range(3):
# #                 tmp_total, tmp = divmod(tmp_total, 60)
# #                 tmp_list[2 - i] = tmp
# #             nh,nm,ns = tmp_list
# #             total += mm
# #             print(nh,nm,ns)
# #             times[nh][nm][ns]+=1
# #     answer = 0
# #     for h in range(24):
# #         for m in range(60):
# #             for s in range(60):
# #                 if times[h][m][s]>answer:
# #                     # print(h,m,s,times[h][m][s])
# #                     answer =times[h][m][s]
# #     return answer
# # # "2016-09-15 21:00:02.066 2.62s" 이게 1로 뜬다 3으로 떠야되는데
# # # l = ["2016-09-15 20:59:58.233 1.181s"]
# # l = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
# # print(solution(l))
#
# # VISIT생성 -> 현재 depth 에서 부셔질 녀석들 ANSWER UPDATE-> 한번에 gravity()
# # 만약 부시지 못한다면 VISIT CHECK
# # UPDATE가 없다면 종료
#
# from collections import deque
# def solution(m, n, board):
#     def bfs(y,x,v,m,n):
#         queue = deque([(y,x)])
#         visited[y][x]=1
#         blocks = [(y,x),]
#         # 블록 shape 만들기
#         while queue:
#             y,x = queue.popleft()
#             for ny,nx in ((y,x+1),(y,x-1),(y+1,x),(y-1,x)):
#                 if (0<=ny<m and 0<=nx<n) and not visited[ny][nx] and board[ny][nx]==v:
#                     visited[ny][nx]=1
#                     queue.append((ny,nx))
#                     blocks.append((ny,nx))
#         cnt = 0
#         if len(blocks)>=4:
#             for block in sorted(blocks):
#                 y,x = block
#                 for ny,nx in ((y,x+1),(y,x-1),(y+1,x),(y-1,x)):
#                     down_y[x] = max(down_y[x], y)
#                 board[y][x]=''
#         return cnt if cnt>=4 else 0
#
#     def down(n):
#         for x in range(n):
#             v_stack = []
#             ny = down_y[x]
#             for y in range(ny,-1,-1):
#                 if board[y][x]:
#                     v_stack.append(board[y][x])
#                     board[y][x]=''
#             for v in  v_stack:
#                 board[ny][x]=v
#                 ny-=1
#     # 4각형 체크하는 방법
#     board = [list(row) for row in board]
#     visited = [[0 for _ in range(n)] for _ in range(m)]
#     answer = 0
#     while True:
#         down_y = [0 for _ in range(n)]
#         depth_cnt = 0
#         for y in range(m):
#             for x in range(n):
#                 if not visited[y][x] and board[y][x]:
#                     depth_cnt+=bfs(y,x,board[y][x],m,n)
#         down(n)
#         if depth_cnt==0:return answer
#         else:
#             answer+=depth_cnt
#             visited = [[0 if board[y][x] else 1 for x in range(n)] for y in range(m)]
#
# m =6
# n = 6
# b = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
# print(solution(m,n,b))
#

pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
def solution(word, pages):
    webpages = {}
    for i, page in enumerate(pages):
        # <meta property=\"og:url\" content=\"https://a.com\"/>
        pagetitle = page.split('<meta property=\"og:url\" content=\"')[1].split('\"')[0]
        print(pagetitle)
        print(page)
        exit()
solution('a',pages)
```