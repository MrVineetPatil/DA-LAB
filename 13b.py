def bf(adj_list,n,s):
    distance=[999 for i in range(n+1)]
    distance[s]=0
    for i in range (n-1):
        for pair in adj_list:
            distance[pair[1]]=min(distance[pair[1]],distance[pair[0]+pair[2]])
    del(distance[0])
    print(distance)

adj_list=[]
n=int(input("enter the no of vertices:"))
e=int(input("Enter the no of edges:"))
for i in range(e):
    u=int(input("Enter the input u:"))
    v=int(input("Enter the input v:"))
    w=int(input("Enter the corresponding weights"))
    l=[u,v,w]
    adj_list.append(l)
print(adj_list)
source=int(input("Enter a source:"))
bf(adj_list,n,source)