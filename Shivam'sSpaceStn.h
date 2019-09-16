int small(int i,vector<int> c)
{int s;
s=fabs(i-c[0]);
for(int j=1;j<c.size();j++)
{if(fabs(i-c[j])<s)
s=fabs(i-c[j]);
}
return s;
}
vector<string> split_string(string);

// Complete the flatlandSpaceStations function below.
int flatlandSpaceStations(int n, vector<int> c) {int i,j,max,g[n];
for(i=0;i<n;++i)
{      for(j=0;j<c.size();j++)
              {if(i==c[j]) 
                   { g[i]=0;
                   break;
              }
              else
              g[i]=small(i,c);
               }
}
max=g[0];
for(int k=1;k<n;k++)
{if(g[k]>max) 
max=g[k];
}
return max;
}