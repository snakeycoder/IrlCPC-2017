def counting(i):
  counter=0
  leng=len(i)
  for k in appr:
    if len(k)>=leng and i==k[:leng]:
      counter+=1
  return(counter)
  
N,M=map(int,input().split())
part=[]
appr=[]
for i in range(N):
  part.append(input())
for i in range(M):
  appr.append(input())
for j in part:
  print(counting(j))
