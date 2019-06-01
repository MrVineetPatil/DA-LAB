#include<iostream>
using namespace std;
int main()
{
  int i,j,n,min,mincost=0,parent[10]={0},cost[10][10],u,v,a,b,ne=1;
  cout<<"Enter no of vertices: ";
  cin>>n;
  for(i=1;i<=n;i++)
    for(j=1;j<=n;j++)
    {
      cout<<"Enter weight between vertex "<<i<<" and "<<j<<": ";
      cin>>cost[i][j];
    }
  while(ne<n)
  {
    min=999;
    for(i=1;i<=n;i++)
      for(j=1;j<=n;j++)
        if(cost[i][j]<min)
        {
          min=cost[i][j];
          a=u=i;
          b=v=j;
        }
    while(parent[u]!=0)
      u=parent[u];
    while(parent[v]!=0)
      v=parent[v];
    if(u!=v)
    {
      cout<<"Vertex "<<a<<" and "<<b<<": "<<min<<endl;
      parent[v]=u;
      ne+=1;
      mincost+=min;
    }
    cost[a][b]=cost[b][a]=999;
  }
  cout<<"Minimum cost: "<<mincost;
}
