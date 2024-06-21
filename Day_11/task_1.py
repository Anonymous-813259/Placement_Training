"""
DFS Algo:-
    1. place the current position in stack
    2. loop:-
    3. select the top of the stack element
    4. check the values of that element
    5. select the first element of the above list value
    6. if the element present in the stack then select other element
    7. else add to stack
    8. repeat 3,4,5,6,7
Unweighted graph
            5---7----4
            |  /     |\
            | /      | 2
            |/       |/
            3--------8
#total way to reach 2 from 5 = 8
{5:[7,3],7:[5,4,3],3:[5,7,8],4:[7,8,2],8:[3,4,2],2:[4,8]}
Visiting all nodes
"""

def dfs(graph,node,stack):
    stack.append(node)
    for i in graph[node]:
        if i not in stack:
            stack=dfs(graph,i,stack)
    return stack

graph={5:[7,3],7:[5,4,3],3:[5,7,8],4:[7,8,2],8:[3,4,2],2:[4,8]}
print(dfs(graph,5,[]))