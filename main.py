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
  # create Hw & Ww
  Hw=[]
  Ww=[]
  for h in range(height):
    Hw.append(genlist(len(H[h])+1,width-sum(H[h])-len(H[h])+1))
  for w in range(width):
    Ww.append(genlist(len(W[w])+1,width-sum(W[w])-len(W[w])+1))
  # create Hb_sum & Wb_sum
  Hb_sum=[]
  for h in range(len(H)):
    Hb_sum.append([0])
    for i in H[h]:
      Hb_sum[-1].append(Hb_sum[-1][-1]+i)
  Wb_sum=[]
  for w in range(len(W)):
    Wb_sum.append([0])
    for i in W[w]:
      Wb_sum[-1].append(Wb_sum[-1][-1]+i)
  # with logic
  while True:
    before=grid[:]
    with_logic(grid,height,width,Hw,Hb_sum)
    grid=[list(x) for x in zip(*grid)]
    with_logic(grid,width,height,Ww,Wb_sum)
    grid=[list(x) for x in zip(*grid)]
    if before==grid:
      break
  print("="*(width*2-1))
  print_out(grid)
  print("="*(width*2-1))
  print("height",height,"width",width)
  for h in range(height):
    for w in range(width):
      if grid[h][w]=="?":
        break
    else:
      continue
    break
  else:
    exit()
  # without logic
  # without_logic(grid,height,width,H,W)

# def without_logic(grid,height,width,H,W):
#   stack=[grid]
#   while len(stack)!=0:
#     grid=stack.pop()
#     for h in range(height):
#       nothing=True
#       for i in grid[h]:
#         if i=="?":
#           nothing=False
#           break
#       if nothing:
#         continue

def with_logic(grid,height,width,w_list,b_sum):
  for h in range(height):
    nothing=True
    for i in grid[h]:
      if i=="?":
        nothing=False
        break
    if nothing:
      continue
    infoW=w_list[h]
    lines=[]
    for i in range(len(infoW)):
      line=[["?"]*width]
      line=fill_line(line,b_sum[h],infoW[i],0)
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

def fill_line(grid,Hb_sum,Hw,h):
  for i in range(1,len(Hw)-1):
    Hw[i]+=1
  fill(grid,h,0,h,Hw[0],".")
  Hw_sum=[0]
  for i in range(len(Hw)):
    Hw_sum.append(Hw_sum[-1]+Hw[i])
  for i in range(1,len(Hw)):
    fill(grid,h,Hw_sum[i]+Hb_sum[i-1],h,Hw_sum[i]+Hb_sum[i],"#")
    fill(grid,h,Hw_sum[i]+Hb_sum[i],h,Hw_sum[i+1]+Hb_sum[i],".")
  for i in range(1,len(Hw)-1):
    Hw[i]-=1
  return grid

def fill(grid,start_h,start_w,end_h,end_w,content):
  if start_w==-1:
    start_w=0
  for h in range(start_h,end_h+1):
    for w in range(start_w,end_w):
      grid[h][w]=content
  return grid

def print_out(grid):
  for line in grid:
    print(" ".join(line))
  return

if __name__=='__main__':
  main()
