def bfs(v):
    visited[v]=1
    print(v)
    L=[v]
    while len(L)!=0:
        v=deleteq(L)
        for j in range(1,n+1):
            if ([v,j] in edgelist) and visited[j]!=1:
                print(j)
                visited[j]=1
                L.append(j)


edgelist=[]
visited=[]

def deleteq(L):
    item=L[0]
    L.remove(item)
    return item

n=int(input("Enter no of vertices"))
for j in range (0,n+1):
    visited.append(0)
print(visited)
edges=int(input("Enter no of edges:"))
for i in range(edges):
    edgelist.append([])
print("Enter input edges:")
for i in range(edges):
    x=list(map(int,input().split()))
    edgelist[i]=x
m=int(input("Enter initial vertex:"))
bfs(m)
