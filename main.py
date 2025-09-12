def main():
  # get size
  height,width=map(int,input().split())
  # create grid
  grid=[]
  for h in range(height):
    grid.append([])
    for w in range(width):
      grid[h].append("?")
  # create H & H_sum
  H=[]
  H_sum=0
  for h in range(height):
    H.append(list(map(int,input().split())))
    H_sum+=sum(H[h])
  # create W & W_sum
  W=[]
  W_sum=0
  for w in range(width):
    W.append(list(map(int,input().split())))
    W_sum+=sum(W[w])
  # sum check
  if H_sum!=W_sum:
    print("No solution")
    print("Height Sum",H_sum)
    print("Width Sum",W_sum)
    exit()

  # fill line DFS
  DFS(grid,height,width,H,0)

  print("height",height,"width",width)
  print("H",H)
  print("W",W)
  print_out(grid)

def DFS(grid,height,width,Hb_,node):
  if node==height:
    print("---------------------")
    print_out(grid)
    return
  Hb=Hb_[node]
  for Hw in genlist(len(Hb)+1,width-sum(Hb)-len(Hb)+1):
    for i in range(1,len(Hw)-1):
      Hw[i]+=1
    fill(grid,node,0,node,Hw[0]-1,".")
    for i in range(1,len(Hw)):
      fill(grid,node,sum(Hb[:i-1])+sum(Hw[:i]),node,sum(Hb[:i])+sum(Hw[:i])-1,"#")
      fill(grid,node,sum(Hb[:i])+sum(Hw[:i]),node,sum(Hb[:i])+sum(Hw[:i+1])-1,".")
    for i in range(1,len(Hw)-1):
      Hw[i]-=1
    DFS(grid,height,width,Hb_,node+1)



def genlist(len:int,sum:int):
  result=[]
  list=[0]*len
  list[-1]=sum
  result.append(list[:])
  while list[0]!=sum:
    i=-1
    while list[i]==0:
      i-=1
    list[i-1]+=1
    list[-1]=list[i]-1
    if i!=-1:
      list[i]=0
    result.append(list[:])
  return result

def fill(grid,start_h,start_w,end_h,end_w,content):
  for h in range(start_h,end_h+1):
    for w in range(start_w,end_w+1):
      grid[h][w]=content
  # print("fill",[start_h,start_w],[end_h,end_w],content)
  # print_out(grid)
  return grid

def print_out(grid):
  for i in range(len(grid)):
    print("".join(grid[i]))

if __name__=='__main__':
  main()
