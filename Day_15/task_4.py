"""
ip:-
    number
op:-
    if pal print number itself
    else print next nearest pal num
"""
def rec_fun(num):
    if str(num)==str(num)[::-1]:
        return num
    return rec_fun(num+1)

n=input()
l=[]

length=len(n)
if length%2==0:
    first_half=n[:length//2]
    second_half=n[length//2:]
    res=first_half+first_half[::-1]
    if res<n:
        first_half=str(int(first_half)+1)
        res=first_half+first_half[::-1]
else:
    first_half=n[:length//2]
    mid_ele=n[(length//2)]
    second_half=n[(length//2)+1:]
    res=first_half+mid_ele+first_half[::-1]
    if res<n:
        mid_ele=str(int(mid_ele)+1)
        res=first_half+mid_ele+first_half[::-1]
print(res)

"""list_len=len(l)


for i in n:
    l.append(i)
i=0
j=len(n)-1
while i<=j:
    if i+1==j:
        a=int(l[i])
        b=int(l[j])
        if a<b:
            a+=1
        b=a
        l[i]=str(a)
        l[j]=str(b)
    elif i==j:
        if l[i-1]<l[j+1]:
           l[i]=chr(ord(l[i])+1)
    else:
        l[j]=l[i]
    i+=1
    j-=1
print("".join(l))"""
print(rec_fun(int(n)))