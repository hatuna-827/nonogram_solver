def DFS(data,node):
  if node==3:
    print(*data)
    return
  for i in range(1,4):
    data[node]=i
    DFS(data,node+1)
  # DFS(data,node+1)

data=[0,0,0]
DFS(data,0)
