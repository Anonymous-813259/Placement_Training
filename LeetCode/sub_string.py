fp=open("substrings.txt","w")
def rec_fun(s):
    if len(s)>1:
        s1=rec_fun(s[:-1])
        fp.write(s1+"\n")
        s2=rec_fun(s[1:])
        fp.write(s2+"\n")
        s3=rec_fun(s[1:-1])
        fp.write(s3+"\n")
    else:
        return s
rec_fun("ab")
