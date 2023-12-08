import math
import numpy as np
from scipy import stats

#求sum内有多少2的倍数
#DocumentChunking
#A financial services company is upload docurrenc to a comp llnce tyoem foranuye3 They use a chunking mechaism as below

def isPowerofTwo(n):
    if n <= 0:
        return []
    else:
        return len([2 ** pos for (pos, value) in enumerate(list(bin(n)[-1:1:-1])) if value != '0'])


def minimumChunksRequired(totalPack, uploadedchunks):
    n=uploadedchunks.shape[0]
    findpack=np.zeros([totalPack,2])

    findpack[:,1]= list(range(1,totalPack+1))
    for i in range(n):
        findpack[uploadedchunks[i][0]-1:uploadedchunks[i][1],0]=1
    print(findpack)

    #提取出连续的小区间
    sum=0
    result=0

    for i in range(totalPack):
        if findpack[i][0]<1:

            sum+=1
            print(i, sum)
            if i+1==totalPack or findpack[i+1][0]==1:
                print("here",sum)
                result+=isPowerofTwo(n=sum)
        else:
            sum=0
            continue
    print(result)



totalPack=10
uploadedchunks=np.array([[1,2],[4,5]])
minimumChunksRequired(totalPack, uploadedchunks)

