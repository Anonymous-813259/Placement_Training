"""
ip:-
    Use Recurssions
    4x3 matrix
op:-
    total possible ways from first to last
"""
row=int(input("Enter Number of Rows:- "))
col=int(input("Enter Number of Columns:- "))
r,c=map(int,input().split())
res=0
matrix=[[1 for i in range(col)]for j in range(row)]
matrix[r][c]=0

def rec_fun(i,j,path):
    if i+1==row and j+1==col:
        print(path)
        return 1
    elif i==row or j==col or i<0 or j<0 or matrix[i][j]==0:
        return 0
    matrix[i][j]=0
    path.append((i,j))
    a=rec_fun(i+1,j,path)
    b=rec_fun(i,j+1,path)
    c=rec_fun(i-1,j,path)
    d=rec_fun(i,j-1,path)
    matrix[i][j]=1
    return a+b+c+d

print(rec_fun(0,0,[]))


#print(rec_fun1(0,0))

"""def rec_fun1(i,j):
    if i+1==row and j+1==col:
        return 1
    elif i==row or j==col:
        return 0
    return rec_fun(i+1,j)+rec_fun(i,j+1)"""