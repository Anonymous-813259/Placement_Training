"""
Unweighted graph
            5---7----4
            |  /     |\
            | /      | 2
            |/       |/
            3--------8
#total way to reach 2 from 5 = 8
{5:[7,3],7:[5,4,3],3:[5,7,8],4:[7,8,2],8:[3,4,2],2:[4,8]}
"""
graph={5:[7,3],7:[5,4,3],3:[5,7,8],4:[7,8,2],8:[3,4,2],2:[4,8]}
all_paths=[]
def dfs_path(graph,node,path,end):
    path.append(node)
    for i in graph[node]:
        if i==end:
            path.append(i)
            print(path)
            path.pop()
        elif i not in path:
            dfs_path(graph,i,path,end)
    path.pop()

for i in graph:
    if i!=5:
        print(f"All paths from {5} to {i}:-")
        dfs_path(graph,5,[],i)