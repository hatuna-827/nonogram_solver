def factorial(n):
  if n==0:
    return 1
  result=n
  for i in range(1,n):
    result*=i
  return result

def max_cases(m,n):
  return int(factorial(m-n+1)/factorial(m-2*n+1)/factorial(n))

def main():
  for m in range(1,60):
    max=0
    n=0
    while True:
      n+=1
      cases=max_cases(m,n)
      if max<cases:
        max=cases
      else:
        break
    print(m,max,n-1)
    print(m,max**m)

if __name__=='__main__':
  main()
