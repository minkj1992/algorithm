# https://leetcode.com/problems/interleaving-string

import pprint


def is_interleaved(s1: str, s2: str, s3: str) -> bool:
    n, m = len(s1), len(s2)
    if (n + m) != len(s3):
        return False
    board = [[False] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            # check edge
            if i == j == 0:
                board[i][j] = True
                continue
            if i == 0:
                if s2[j - 1] == s3[i + j - 1]:
                    board[i][j] = board[i][j - 1]
                continue
            if j == 0:
                if s1[i - 1] == s3[i + j - 1]:
                    board[i][j] = board[i - 1][j]
                continue
            # check except edge
            if s1[i - 1] == s3[i + j - 1]:
                if s2[j - 1] == s3[i + j - 1]:
                    board[i][j] = board[i - 1][j] or board[i][j - 1]
                else:
                    board[i][j] = board[i - 1][j]
            else:
                if s2[j - 1] == s3[i + j - 1]:
                    board[i][j] = board[i][j - 1]
    pprint.pprint(board)
    return board[n][m]


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

is_interleaved(s1, s2, s3)
