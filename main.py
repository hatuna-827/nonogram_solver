def main():
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
    print(list(map(int,input().split())))
    # H.append(list(map(int,input().split())))
    # H_sum+=sum(H[h])
  exit()
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
  # H_temp=[]
  # for h in range(height):
  #   H_temp.append(genlist(len(H[h])+1,width-sum(H[h])-len(H[h])+1))
  # W_temp=[]
  # for w in range(width):
  #   W_temp.append(genlist(len(W[w])+1,height-sum(W[w])-len(W[w])+1))
  # print("H_temp",H_temp)
  # print("W_temp",W_temp)

  # for h in range(height):
  #   if sum(H[h])+len(H[h])-1==width:
  #     fill(grid,h,0,h,H[h][0]-1,"#")
  #     for i in range(1,len(H[h])):
  #       fill(grid,h,sum(H[h][0:i])+i,h,sum(H[h][0:i+1])+i-1,"#")
  #       fill(grid,h,sum(H[h][0:i])+i-1,h,sum(H[h][0:i])+i-1,".")
  # for w in range(width):
  #   if sum(W[w])+len(W[w])-1==height:
  #     fill(grid,0,w,W[w][0]-1,w,"#")
  #     for i in range(1,len(W[w])):
  #       fill(grid,sum(W[w][0:i])+i,w,sum(W[w][0:i+1])+i-1,w,"#")
  #       fill(grid,sum(W[w][0:i])+i-1,w,sum(W[w][0:i])+i-1,w,".")

  # for h in range(height):
  #   Hb=H_temp[h]
  #   Hf=H[h]
  #   if len(Hb)==1:
  #     Hb=Hb[0]
  #     fill(grid,h,0,h,Hb[0]-1,".")
  #     for i in range(1,len(Hb)):
  #       fill(grid,h,sum(Hb[0:i])+sum(Hf[0:i-1])-1,h,sum(Hb[0:i])+sum(Hf[0:i])-1,"#")
  #       fill(grid,h,sum(Hb[0:i])+sum(Hf[0:i]),h,sum(Hb[0:i+1])+sum(Hf[0:i]),".")

  H_temp=[]
  for h in range(height):
    list=[0]*len(H[h])+1
    list[-1]=width-sum(H[h])-len(H[h])+1
    H_temp.append(list[:])
  print("H_temp",H_temp)
  # DFS(grid,height,width,H,H_temp,0)

  print("height",height,"width",width)
  print("H",H)
  print("W",W)
  print_out(grid)

def DFS(grid,height,width,Hf,Hb,node):
  Hb=Hb[0]
  fill(grid,node,0,node,Hb[0]-1,".")
  for i in range(1,len(Hb)):
    fill(grid,node,sum(Hb[0:i])+sum(Hf[0:i-1])-1,node,sum(Hb[0:i])+sum(Hf[0:i])-1,"#")
    fill(grid,node,sum(Hb[0:i])+sum(Hf[0:i]),node,sum(Hb[0:i+1])+sum(Hf[0:i]),".")

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
  print("fill",start_h,start_w,end_h,end_w,content)
  for h in range(start_h,end_h+1):
    for w in range(start_w,end_w+1):
      if grid[h][w]=="?":
        grid[h][w]=content
  # print_out(grid)
  return grid

def print_out(grid):
  for i in range(len(grid)):
    print("".join(grid[i]))

if __name__=='__main__':
  main()