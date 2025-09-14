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
  # with logic
  for i in range(4):
    with_logic(grid,height,width,H)
    grid=[list(x) for x in zip(*grid)]
    with_logic(grid,width,height,W)
    grid=[list(x) for x in zip(*grid)]

  # without logic
  # while True:
  #   if check(grid,W,node):
  #     return
  #   if node==height:
  #     print("----------------------------")
  #     print_out(grid)
  #     print("----------------------------")
  #     return
  #   Hb=Hb_[node]
  #   for Hw in genlist(len(Hb)+1,width-sum(Hb)-len(Hb)+1):
  #     for i in range(1,len(Hw)-1):
  #       Hw[i]+=1
  #     fill(grid,node,0,node,Hw[0]-1,".")
  #     for i in range(1,len(Hw)):
  #       fill(grid,node,sum(Hb[:i-1])+sum(Hw[:i]),node,sum(Hb[:i])+sum(Hw[:i])-1,"#")
  #       fill(grid,node,sum(Hb[:i])+sum(Hw[:i]),node,sum(Hb[:i])+sum(Hw[:i+1])-1,".")
  #     for i in range(1,len(Hw)-1):
  #       Hw[i]-=1
  #     DFS(grid,height,width,Hb_,W,node+1)
  #   break

  print_out(grid)
  print("height",height,"width",width)
  print("H",H)
  print("W",W)

def with_logic(grid,height,width,H):
  for h in range(height):
    Hb=H[h]
    Hw=genlist(len(Hb)+1,width-sum(Hb)-len(Hb)+1)
    H_lines=[]
    for i in range(len(Hw)):
      H_line=[["?"]*width]
      H_line=fill_line(H_line,Hb,Hw[i],0)
      H_lines.append(H_line[0])
      for w in range(width):
        if grid[h][w]!="?" and H_line[0][w]!=grid[h][w]:
          Hw[i]="@"
          H_lines[i]="@"
    Hw=[i for i in Hw if i!="@"]
    H_lines=[i for i in H_lines if i!="@"]
    grid[h]=dup(H_lines)
  return grid

def dup(o):
  O=o[0]
  for i in range(1,len(o)):
    for w in range(len(O)):
      if O[w]!="?" and O[w]!=o[i][w]:
        O[w]="?"
  return O

def check(grid,W,height):
  for w in range(len(W)):
    w_count=0
    b_count=0
    b_sum=sum(W[w])
    w_sum=len(grid)-b_sum
    con=0
    index=-1
    for h in range(height):
      if grid[h][w]=="?":
        break
      elif grid[h][w]==".":
        w_count+=1
        if w_count>w_sum:
          # print("check out w_count",w,h,height)
          # print_out(grid)
          return True
        if index!=-1 and con!=0 and W[w][index]>con:
          # print("check out con less",w,h,height)
          # print_out(grid)
          return True
        con=0
      elif grid[h][w]=="#":
        b_count+=1
        if b_count>b_sum:
          # print("check out b_count",w,h,height)
          # print_out(grid)
          return True
        if con==0:
          index+=1
        con+=1
        if W[w][index]<con:
          # print("check out con over",w,h,height)
          # print_out(grid)
          return True
  return False

def genlist(len,sum):
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

def fill_line(grid,Hb,Hw,h):
  for i in range(1,len(Hw)-1):
    Hw[i]+=1
  fill(grid,h,0,h,Hw[0]-1,".")
  for i in range(1,len(Hw)):
    fill(grid,h,sum(Hw[0:i])+sum(Hb[0:i-1]),h,sum(Hw[0:i])+sum(Hb[0:i])-1,"#")
    fill(grid,h,sum(Hw[0:i])+sum(Hb[0:i]),h,sum(Hw[0:i+1])+sum(Hb[0:i])-1,".")
  for i in range(1,len(Hw)-1):
    Hw[i]-=1
  return grid

def fill(grid,start_h,start_w,end_h,end_w,content):
  if start_w==-1:
    start_w=0
  for h in range(start_h,end_h+1):
    for w in range(start_w,end_w+1):
      grid[h][w]=content
  # print("fill",start_h,start_w,end_h,end_w,content)
  return grid

def print_out(grid):
  for i in range(len(grid)):
    print("".join(grid[i]))

if __name__=='__main__':
  main()
