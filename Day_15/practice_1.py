def is_valid(board, row, col, n,r,c):
        if row==r or col==c: 
            return False
        for i in range(col):# check horizontal
            if board[row][i] == 1 :
                return False
        i = row
        j = col
        while i>=0 and j >= 0: # upper left diag
            if  board[i][j] == 1:
                return False
            i -= 1 
            j -= 1 
        i = row
        j = col
        while i<n and j >=0: #bottom left diag
            if board[i][j] == 1:
                return False
            i += 1 
            j -= 1
            
        return True
def solve(n,r,c):
    board = [[0 for i in range(n)] for j in range(n)]
    def backtrack(col):
        if col == n:
            return True
        max1=0
        for i in range(n):
            if is_valid(board, i, col, n,r,c):
                board[i][col] = 1
                for row in board:
                    print(row)
                print()
                if backtrack(col+1):
                    return True
                board[i][col] = 0
        return False 
    if backtrack(0):
        for row in board:
            print(row)
    else:
        print("no")
n = 4
r,c=2,1
solve(n,r,c)