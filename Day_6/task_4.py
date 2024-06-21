"""
ip:-
    num=12 k=3
op:-
    Find factors of 12 and give k largest factor
"""
num=int(input())
k=int(input())
if k==1:
    print(num)
c=1
for i in range(num//2,0,-1):
    if num%i==0:
        c+=1
    if c==k:
        print(i)
        break




"""l=[1,]
for i in range(2,(num//2)+1):
    if num%i==0:
        l.append(i)
l.append(num)
print(l[k*-1])"""