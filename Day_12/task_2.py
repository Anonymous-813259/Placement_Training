
#                2      4
#            5-------8-----6
#            |\      |      \ 
#            | \     |       \ 2
#           2|  \ 2  |3       \    2
#            |   \   |         9--------4
#            |    \  |        / 
#            |     \ |       /1
#            |      \|      /
#            2-------3-----7
#                1       3
"""
Dijkstras Algoritm
"""
def find_min(queue):
    mn=9999
    node=-1
    for i in queue:
        if cost_dict[i]<mn:
            mn=cost_dict[i]
            node=i
    return node

def dijkstra_rec(node,queue,visited):
    #print(node,queue,visited,cost_dict)
    if not queue:
        queue.append(node)
        cost_dict[n]=0
    for i in graph[node]:
        if i[0] not in visited:
            if i[0] not in queue:
                queue.append(i[0])
            cost=cost_dict[node]+i[1]
            if cost<cost_dict[i[0]]:
                cost_dict[i[0]]=cost
    visited.append(node)
    queue.remove(node)
    mn_node=find_min(queue)
    if queue:
        dijkstra(mn_node,queue,visited)
def dijkstra(node,queue,visited):
    queue.append(node)
    cost_dict[n]=0
    while queue:
        #print(node,queue,visited)
        for i in graph[node]:
            if i[0] not in visited:
                if i[0] not in queue:
                    queue.append(i[0])
                cost=cost_dict[node]+i[1]
                if cost_dict[i[0]]>cost:
                    cost_dict[i[0]]=cost
        visited.append(node)
        queue.remove(node)
        node=find_min(queue)

            

graph={2:[(5,2),(3,1)],3:[(2,1),(5,2),(7,3),(8,3)],4:[(9,2),],5:[(2,2),(3,2),(8,2)],6:[(8,4),(9,2)],7:[(3,3),(9,1)],8:[(5,2),(3,3),(6,4)],9:[(6,2),(7,1),(4,2)]}
cost_dict=dict()
for i in graph:
    cost_dict[i]=9999
n=int(input())
dijkstra(n,[],[])
print(cost_dict)
