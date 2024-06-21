"""
ip:-
    consider year has 360 days month as 30 days week has 6 days
    total number of days 65476
op:-
    ?y ?m ?w ?d
"""
days=int(input())
y=0
m=0
w=0
if days>=360:
    y=days//360
    days=days%360
if days>=30:
    m=days//30
    days=days%30
if days>=6:
    w=days//6
    days=days%6
print(f"{y}Years {m}Months {w}Weeks {days}Days")