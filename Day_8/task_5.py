"""
ip:-
    input n from user that is nxn matrix
    4
    tued
    fwow
    roer
    drui
    
    word -> search this word is in matrix or not
op:-
    yes
"""
n=int(input())
matrix=[]
for i in range(n):
    matrix.append(input())
word=input()

def rec_fun(row,col,ind):
    if ind==len(word):
        return True
    if row<0 or row>=len(matrix) or col<0 or col>=len(matrix[row]) or matrix[row][col]!=word[ind]:
        return False
    matrix[row]=matrix[row][:col]+'0'+matrix[row][col+1:]
    return rec_fun(row-1,col,ind+1) or rec_fun(row+1,col,ind+1) or rec_fun(row,col-1,ind+1) or rec_fun(row,col+1,ind+1)
flag=False
print()
for i in range(n):
    for j in range(n):
        if matrix[i][j]==word[0]:
            print(matrix)
            if rec_fun(i,j,0):
                flag=True
                break
print(flag)
#print(rec_fun(0,0,0))