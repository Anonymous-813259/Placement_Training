"""
BFS
"""
def visit_bfs_rec(node,queue,visited):
    if not queue:
        queue.append(node)
    #print(queue,visited)
    for i in graph[node]:
        if i not in queue and i not in visited:
            queue.append(i)
    #print(queue,visited)
    queue.pop(0)
    visited.append(node)
    #print(node,queue,visited)
    if queue:
        return visit_bfs_rec(queue[0],queue,visited)
    else:
        return visited
def visit_bfs(node,queue,visited):
    queue.append(node)
    while queue:
        for i in graph[queue[0]]:
            if i not in queue and i not in visited:
                queue.append(i)
        visited.append(queue[0])
        queue.pop(0)
    return visited

#graph={5:[7,3],7:[5,4,3],3:[5,7,8],4:[7,8,2],8:[3,4,2],2:[4,8]}
graph={1:[2,7],2:[1,3,9],3:[2,4],4:[3,5,6,10],5:[4,6,7],6:[4,5,7],7:[1,5,6,8],8:[7,],9:[2,],10:[4,]}
print(visit_bfs_rec(5,[],[]))
print(visit_bfs(5,[],[]))