pList=[2,3,5,7]
def checker(i):
    for j in pList:
        if j>int(np.sqrt(i)+1):
            break
        if i%j==0:
            return(False)
    pList.append(i)
    return(True)

for i in range(8,200):
    checker(i)
initDict={}

for j in range(2,200,2):
    counter=0
    k=0
    while pList[k]<=(j//2):
        #if pList[k]>=j-pList[k]:
        #    print("oopsy!")
        k+=1
        if j-pList[k] in pList:
            counter+=1
            print(j,pList[k],j-pList[k])
    initDict[j]=counter
print(initDict)
