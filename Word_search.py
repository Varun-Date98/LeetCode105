from typing import List


'''
79. Word Search | Medium
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once.
--------------------------------------------------------------------------------------------------

'''


def exist(board: List[List[str]], word: str) -> bool:
    starts, ends = [], []
    cardinals = [0, 1, 0, -1, 0]
    m, n = len(board), len(board[0])

    def dfs(x: int, y: int, Idx: int) -> bool:
        if Idx == len(word) - 1:
            return board[x][y] == word[-1]
        
        copy, board[x][y] = board[x][y], '#'

        for i in range(4):
            nr, nc = x + cardinals[i], y + cardinals[i + 1]

            if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == word[Idx + 1]:
                if dfs(nr, nc, Idx + 1):
                    return True
        
        board[x][y] = copy
        return False


    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                starts.append((i, j))
            
            if board[i][j] == word[-1]:
                ends.append((i, j))
    
    # No need to check if ends exists as if ends is empty the word does not appear in the board
    origins = starts if len(starts) < len(ends) else ends

    if origins == ends:
        word = word[::-1]
    
    for x, y in origins:
        if dfs(x, y, 0):
            return True
    
    return False
