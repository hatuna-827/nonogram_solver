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
  while True:
    before=grid[:]
    with_logic(grid,height,width,H)
    grid=[list(x) for x in zip(*grid)]
    with_logic(grid,width,height,W)
    grid=[list(x) for x in zip(*grid)]
    if before==grid:
      break
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

def with_logic(grid,height,width,info):
  for h in range(height):
    nothing=True
    for i in grid[h]:
      if i=="?":
        nothing=False
        break
    if nothing:
      continue
    infoB=info[h]
    infoW=genlist(len(infoB)+1,width-sum(infoB)-len(infoB)+1)
    lines=[]
    for i in range(len(infoW)):
      line=[["?"]*width]
      line=fill_line(line,infoB,infoW[i],0)
      lines.append(line[0])
      for w in range(width):
        if grid[h][w]!="?" and line[0][w]!=grid[h][w]:
          lines[i]="@"
          break
    lines=[i for i in lines if i!="@"]
    grid[h]=dup(lines)
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
          return True
        if con!=0 and index!=-1 and W[w][index]>con:
          return True
        con=0
      elif grid[h][w]=="#":
        b_count+=1
        if b_count>b_sum:
          return True
        if con==0:
          index+=1
        con+=1
        if W[w][index]<con:
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
  return grid

def print_out(grid):
  for i in range(len(grid)):
    print(" ".join(grid[i]))
  return

if __name__=='__main__':
  main()
