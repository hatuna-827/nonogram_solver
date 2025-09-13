def DFS(data,node):
  if node==2:
    print(*data)
    return
  for i in genlist():
    data[node]=i
    DFS(data,node+1)

def genlist():
  return [[1,0],[0,1]]

data=[[0,0],[0,0]]
DFS(data,0)
