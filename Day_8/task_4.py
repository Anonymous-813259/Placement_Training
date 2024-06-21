"""
ip:-
    6
    0 1 1 1 0 1
    0 1 0 1 0 0
    1 0 1 1 0 0 
    0 0 0 1 1 1
    1 1 0 0 0 1
    1 1 1 0 1 0
    4 6
    that means ath row 6th column tree will catch the fire that will spread the fire top, bottom, left, right. Finally print number of trees unburned
    1's -> trees
    0's -> barlands
op:-
    8
"""
n=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
row,col=map(int,input().split())
row-=1
col-=1
def rec_fun(row,col):
    if (row<0 or row>=len(matrix)) or (col<0 or  col>=len(matrix[row])) or matrix[row][col]==0:
        return
    matrix[row][col]=0
    rec_fun(row-1,col)
    rec_fun(row+1,col)
    rec_fun(row,col-1)
    rec_fun(row,col+1)
rec_fun(row,col)
for i in matrix:
    print(i)
count=0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]==1:
            count+=1
print(count)