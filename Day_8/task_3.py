"""
ip:-
    take input of the string
    abfgresagtyuiofde
op:-
    print longest sub string without repeating character
    12 resagtyuiofd
"""
s=input()
d=dict()
d[s[0]]=0
mx=-1
j=0
n=len(s)
i=1
while i<n:
    if s[i] not in d:
        d[s[i]]=i
    else:
        if mx<i-j:
            mx=i-j
        if d[s[i]]>j:
            j=d[s[i]]+1
        d[s[i]]=i
    i+=1
if mx<(i-j):
    mx=i-j
print(mx)