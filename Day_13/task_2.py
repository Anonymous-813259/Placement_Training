"""
ip:-
    given 2 strings
    abcd
    axbdc
op:-
    print all the sub sequence
    abcd-a,ab,ac,ad,abc,abd,abcd,b,bc,bd,bcd,c,cd,d
"""
res=[]
def all_sub_sequence(s,res_s):
    if res_s not in res:
        res.append(res_s)
    if not s:
        return
    all_sub_sequence(s[1:],res_s+s[0])
    all_sub_sequence(s[1:],res_s)
def sub_sequence(s):
    for i in range(len(s)):
        all_sub_sequence(s[i+1:],s[i])
def tabulation(s1,s2):
    matrix=[[0 for i in range(len(s1)+1)]for j in range(len(s2)+1)]
    for j in range(1,len(s2)+1):
        for i in range(1,len(s1)+1):
            if s1[i-1]==s2[j-1]:
                matrix[j][i]=matrix[j-1][i-1]+1
            else:
                matrix[j][i]=max(matrix[j-1][i],matrix[j][i-1])
    for i in matrix:
        print(i)
    res=""
    i=len(s2)
    j=len(s1)
    print(i,j)
    while i>=0 and j>=0:
        if s1[j-1]==s2[i-1]:
            res+=s1[j-1]
            j-=1
            i-=1
        else:
            if(matrix[i][j]==matrix[i-1][j]):
                i-=1
            else:
                j-=1
    return matrix[-1][-1],res[::-1]


s="abcdx"
sub_sequence(s)
print(res)
s1="abcd"
s2="axbdc"
print(tabulation(s1,s2))