#include<iostream>
using namespace std;
int main()
{
  int i,j,n,cost[10][10],a,b,u,v,min,mincost=0,visited[10]={0},ne=1;
  cout<<"Enter no of vertices: ";
  cin>>n;
  for(i=1;i<=n;i++)
    for(j=1;j<=n;j++)
    {
      cout<<"Enter weight between "<<i<<" and "<<j<<" vertex: ";
      cin>>cost[i][j];
    }
  visited[1]=1;
  while(ne<n)
  {
    min=999;
    for(i=1;i<=n;i++)
      for(j=1;j<=n;j++)
        if(cost[i][j]<min)
          if(visited[i]!=0)
          {
            min=cost[i][j];
            a=u=i;
            b=v=j;
          }
        if(visited[u]==0 || visited[v]==0)
        {
          cout<<"Vertex "<<a<<" and vertex "<<b<<": "<<min<<endl;
          ne=ne+1;
          mincost=mincost+min;
          visited[b]=1;
        }
      cost[a][b]=cost[b][a]=999;
      }
  cout<<"Minimum cost: "<<mincost;
}
