def rec_fun(s,fi,li):
    if fi>=li:
        return True
    if s[fi]!=s[li]:
        return False
    return rec_fun(s,fi+1,li-1)

s=input()
print(rec_fun(s,0,len(s)-1))
    