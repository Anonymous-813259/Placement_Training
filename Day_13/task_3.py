"""
ip:-
    5
    0 1 0 0 1
    1 0 0 1 1
    0 0 0 0 0
    1 0 0 0 0
    1 0 0 0 1
    Island Question
    1->land
    0->water
    a land is connected if it is present top, left, right, bottom
op:-
    print count of all the lands and largest area land
    5
    3
"""
def backtrack(earth,i,j):
    if i<0 or j<0 or i>=len(earth) or j>=len(earth) or earth[i][j]==0:
        return 0
    earth[i][j]=0
    return 1+backtrack(earth,i-1,j)+backtrack(earth,i,j-1)+backtrack(earth,i+1,j)+backtrack(earth,i,j+1)
n=int(input())
earth=[]
for i in range(n):
    earth.append(list(map(int,input().split())))
count=0
largest_area=0
for i in range(len(earth)):
    for j in range(len(earth[i])):
        if earth[i][j]==1:
            count+=1
            area=backtrack(earth,i,j)
            if area>largest_area:
                largest_area=area
print("Total Islands:-",count)
print("Largest Area:-",largest_area)