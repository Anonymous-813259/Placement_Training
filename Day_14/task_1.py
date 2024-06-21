"""
ip:-
    heights of the building will be given in the form of list. Rain waters are trapped between the buildings.
    2 5 2 3 6 7 1 0 5 7
    water storeed between:
    2-5->0;5-2->0;2-3->0;3-6->0;6-7->0;7-1->0;1-0->0-5->0;
    5-6->5(from height 5 to breadth 2 remove area of 2 and 3 buildings);
    7-7->15(from height 7 to breadth 3 remove area of 1,0 and 5 buildings)
    Total: 5+15=20;

        0| 15|
    0   ||   |
     |5 ||  ||
     | 0||  ||-----> 5+15=20
     |0|||  ||
    ||||||0 ||
    |||||||0||
    --------------------------------------------
op:-
    20
"""
l=list(map(int,input().split()))
i=0
j=len(l)-1
intermediate=sum(l)-l[i]-l[j]
mx_area=0
while(i<j):
    area=(min(l[i],l[j])*(j-i-1))-intermediate
    if area>mx_area:
        mx_area=area
    if l[i]<l[j]:
        i+=1
        intermediate-=l[i]
    else:
        j=-1
        intermediate-=l[j]
print(mx_area)

"""mx=l[0]
store=0
for i in range(1,len(l)):
    if mx>=l[i]:
        store+=(mx-l[i])
    else:
        mx=l[i]
print(store)"""