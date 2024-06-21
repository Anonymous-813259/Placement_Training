res=["",]
d=dict()
def rec_fun(s):
    if len(s)>1 and (s not in d):
        print(s)
        if s==s[::-1]:
            if len(res[0])<len(s):
                res[0]=s
                if s not in d:
                    d[s]=1
                return s
            else:
                return ""
        elif len(res[0])>len(s):
            return ""
        else:
            s1=rec_fun(s[1:])
            s2=rec_fun(s[:-1])
            s3=rec_fun(s[1:-1])
            if len(s1)>=len(s2) and len(s1)>=len(s3):
                if len(res[0])<len(s1):
                    res[0]=s1
                    if s1 not in d:
                        d[s1]=1
                    return s1
                else:
                    return ""
            elif len(s2)>=len(s1) and len(s2)>=len(s3):
                if len(res[0])<len(s2):
                    res[0]=s2
                    if s2 not in d:
                        d[s2]=1
                    return s2
                else:
                    return ""
            else:
                if len(res[0])<len(s3):
                    res[0]=s3
                    if s3 not in d:
                        d[s3]=1
                    return s3
                else:
                    return ""
    else:
        return ""
s="bababbccb"
ans=rec_fun(s)
if not ans:
    ans=s[0]
print(d)
print("ans:-",ans)
#abbcccbbbcaaccbababcbcabca