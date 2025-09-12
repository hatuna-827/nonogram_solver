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

  # make H_temp & W_temp
  # H_temp=[]
  # for h in range(height):
  #   H_temp.append(genlist(len(H[h])+1,width-sum(H[h])-len(H[h])+1))
  # W_temp=[]
  # for w in range(width):
  #   W_temp.append(genlist(len(W[w])+1,height-sum(W[w])-len(W[w])+1))
  # print("H_temp",H_temp)
  # print("W_temp",W_temp)

  # fill line
  # for h in range(height):
  #   Hb=H[h]
  #   Hw=H_temp[h]
  #   if len(Hw)==1:
  #     Hw=Hw[0]
  #     fill(grid,h,0,h,Hw[0]-1,".")
  #     for i in range(1,len(Hw)):
  #       fill(grid,h,sum(Hw[0:i])+sum(Hb[0:i-1])-1,h,sum(Hw[0:i])+sum(Hb[0:i])-1,"#")
  #       fill(grid,h,sum(Hw[0:i])+sum(Hb[0:i]),h,sum(Hw[0:i+1])+sum(Hb[0:i]),".")

  # fill line DFS
  H_temp=[]
  for h in range(height):
    new_list=[0]*(len(H[h])+1)
    new_list[-1]=width-sum(H[h])-len(H[h])+1
    H_temp.append(new_list[:])
  DFS(grid,height,width,H,H_temp,0)

  print("height",height,"width",width)
  print("H",H)
  print("W",W)
  print_out(grid)

def DFS(grid,height,width,Hb_,Hw_,node):
  if node==height:
    print("unu ans")
    print_out(grid)
    return
  Hb=Hb_[node]
  Hw=Hw_[node]
  for i in range(1,len(Hw)-1):
    Hw[i]+=1
  fill(grid,node,0,node,Hw[0]-1,".")
  for i in range(1,len(Hw)):
    fill(grid,node,sum(Hb[:i-1])+sum(Hw[:i]),node,sum(Hb[:i])+sum(Hw[:i])-1,"#")
    fill(grid,node,sum(Hb[:i])+sum(Hw[:i]),node,sum(Hb[:i])+sum(Hw[:i+1])-1,".")
  for i in range(1,len(Hw)-1):
    Hw[i]-=1
  if Hw[0]!=sum(Hw):
    i=-1
    while Hw[i]==0:
      i-=1
    Hw[i-1]+=1
    Hw[-1]=Hw[i]-1
    if i!=-1:
      Hw[i]=0
    DFS(grid,height,width,Hb_,Hw_,node)
  DFS(grid,height,width,Hb_,Hw_,node+1)


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
  # if start_w==-1:
  #   start_w=0
  for h in range(start_h,end_h+1):
    for w in range(start_w,end_w+1):
      # if grid[h][w]=="?":
      grid[h][w]=content
  # print("fill",[start_h,start_w],[end_h,end_w],content)
  # print_out(grid)
  return grid

def print_out(grid):
  for i in range(len(grid)):
    print("".join(grid[i]))

if __name__=='__main__':
  main()