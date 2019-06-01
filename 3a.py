def dfs(v):
    visited[v]=1
    print(v)
    L=[v]
    while len(L)!=0:
        L.pop()
        for j in range(1,n+1):
            if ([v,j] in edgelist or [j,v] in edgelist) and visited[j]!=1:
                L.append(j)
                dfs(j)

visited=[]
edgelist=[]

n=int(input("Enter the no of vertices:"))
for i in range(0,n+1):
    visited.append(0)
print(visited)
edges=int(input("Enter the no of edges:"))
for i in range(edges):
    edgelist.append([])
print("Input edges:")
for i in range(edges):
    k=list(map(int,input().split()))
    edgelist[i]=k
v=int(input("Enter initial vertex:"))
dfs(v)