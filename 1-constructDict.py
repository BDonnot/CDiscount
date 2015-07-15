import sys
import os
import pandas as pd
from itertools import chain
import gc
print (sys.version)

if(sys.version == "2.7.6 (default, Jun 22 2015, 17:58:13) \n[GCC 4.8.2]") :
    os.chdir("/home/benjamin/Documents/CDiscount/")
else :
    os.chdir("D:/Users/Benjamin/Documents/Data Science/CDiscount/")
    
Train = pd.read_csv("data/trainingClean.csv",sep = ";",encoding = "utf-8")
Train.head
UniqueDescr = Train["Description"].dropna().unique().copy()

del(Train)
i = 0
gc.collect()

def flatten(listOfLists):
    return list(chain.from_iterable(listOfLists))

def flattenUniqueAux(res,UniqueDescr,start,end):
    sortedUniqueDescr = map(lambda x : x.split(),UniqueDescr[start:end])
    flatSort = flatten(sortedUniqueDescr)
    flatSort = pd.Series(flatSort)
    flatSort=pd.Series(flatSort.unique())
    res=pd.concat([res,flatSort])
    res=pd.Series(res.unique())
    return res
def flattenUnique(UniqueDescr,n):
    N = len(UniqueDescr)
    gap = int(len(UniqueDescr)/n)
    res = pd.Series()
    for i in range(n+1) :    
        res = flattenUniqueAux(res,UniqueDescr,(i*gap),((i+1)*gap))
    res = flattenUniqueAux(res,UniqueDescr,((i+1)*gap),N)
    res.sort()
    return res
sortedUniqueDescr=flattenUnique(UniqueDescr,8)
len(sortedUniqueDescr)
sortedUniqueDescr= pd.Series(sortedUniqueDescr)


sortedUniqueDescr.to_csv("data/SortedDescTraining.csv", sep = ";" ,index = 0 , encoding  = "utf-8") 


len(flattenUnique(UniqueDescr[0:11],8))
test=pd.Series(flatten(map(lambda x : x.split(),UniqueDescr[0:11]))).unique()
test.sort()
len(test)
sortedUniqueDescr[0].split()
sortedUniqueDescr = map(lambda x :x.split(),UniqueDescr[0:10])
len(UniqueDescr)[(9109768/(16000+32000)*2):(9109768/(16000))]

for el in UniqueDescr[(9109768/(16000+32000)*2):(9109768/(16000))] :
    print(el)
s1 = pd.Series([1,2,3])
s2 = pd.Series([1,2,3])
s3 = pd.concat([s1,s2])
s3.unique()


