def mapper(N,M,bigList):
    emptyList=['']*N
    for i in range(N):
        for j in range(M):
            emptyList[i]+=numinator(N,M,i,j,bigList)

    for i in emptyList:
        print(i.strip())
        

def numinator(N,M,i,j,bigList):
    if bigList[i][j]=='x':
        return('x ')
    counter=0
    for k in range(3):
        for l in range(3):
            if i-1+k>=0 and j-1+l>=0 and i-1+k<N and j-1+l<M:
                if bigList[i-1+k][j-1+l]=='x':
                    counter+=1
    return(str(counter)+' ')


def toExec():
    N, M = map(int,input().split())
    bigList=[]
    for i in range(N):
        bigList.append(input().replace(' ',''))
    mapper(N,M,bigList)

toExec()
