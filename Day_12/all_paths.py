def all_path_dfs(node,path,end):
    path.append(node)
    #print(node,path)
    if node==end:
        print(path)
        path.pop()
        return
    for i in graph[node]:
        if i not in path:
            all_path_dfs(i,path,end)
    path.pop()
def all_path_cost_dfs(node,path,end,c):
    path.append(node)
    if node==end:
        print(path,c)
        path.pop()
        return
    for i in graph[node]:
        if i[0] not in path:
            all_path_cost_dfs(i[0],path,end,c+i[1])
    path.pop()
def min_path_cost_dfs(node,path,end,c,mn,short_path):
    path.append(node)
    if node==end:
        if c<mn:
            mn=c
            short_path=path.copy()
        path.pop()
        return short_path,mn
    for i in graph[node]:
        if i[0] not in path:
            short_path,mn=min_path_cost_dfs(i[0],path,end,c+i[1],mn,short_path)
    path.pop()
    return short_path,mn
        

graph={5:[(7,2),(3,1)],7:[(5,2),(4,3),(3,4)],4:[(7,3),(8,2),(2,6)],8:[(2,4),(3,1),(4,2)],3:[(5,2),(7,4),(8,1)],2:[(4,6),(8,4)]}
#graph={5:[7,3],7:[5,4,3],3:[5,7,8],4:[7,8,2],8:[3,4,2],2:[4,8]}
#all_path_dfs(5,[],2)
print("All possible paths from 5 to 2 with cost:-")
all_path_cost_dfs(5,[],2,0)
print()
print("Best Path from 5 to 2 (path,cost):-",min_path_cost_dfs(5,[],2,0,9999,[]))
print()
for i in graph:
    if i!=5:
        print(f"Best Path from 5 to {i} (path,cost):- {min_path_cost_dfs(5,[],i,0,9999,[])}")