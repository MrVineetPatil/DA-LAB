import heapq as hq
def djkstra(graph,start):
    n=len(graph)
    Q=[[0,start]]
    d=[999 for i in range(n)]
    d[start]=0
    while Q:
        Q.sort()
        [length,u]=Q.pop(0)
        for v in range (n):
            if d[v]>d[u]+graph[u][v]:
                d[v]=d[u]+graph[u][v]
                #hq.heappush(Q,[d[v],v])
                Q.append([d[v],v])
    return d

graph=[]
n=int(input("Enter no of nodes:"))
print("Enter weights of respective edges:")
for i in range(n):
    m=[]
    print("Next edge:")
    for k in range(n):
        print("From",i+1,"to",k+1)
        k=int(input())
        m.append(k)
    graph.append(m)
d=djkstra(graph,0)
print(d)