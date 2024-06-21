"""
ip:-
    abdbsdabca
op:-
    bdb
"""
s=input()
res=s[0]
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i:j]==s[i:j][::-1] and len(res)<len(s[i:j]):
            res=s[i:j]
print(res)