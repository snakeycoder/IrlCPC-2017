import math
pList=[2,3,5,7]
def checker(i):
    for j in pList:
        if j>int(math.sqrt(i)+1):
            break
        if i%j==0:
            return(False)
    pList.append(i)
    return(True)

for i in range(pList[-1]+1,200):
    checker(i)


n,w=map(int,input().split())
j=0
counter2=0
while counter2<n:
    k=0
    counter=0
    ways=[]
    while pList[k]<=(j//2+1):
        ways.append(pList[k])
        k+=1
        if j-pList[k] in pList and j-pList[k] not in ways:
            counter+=1
        if counter>w+1:
            break
    if counter==w:
        counter2+=1
    if counter2==n:
        print(j)
    j+=1
