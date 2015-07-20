# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 20:36:57 2015

@author: Benjamin
"""

import sys
import os
import pandas as pd
from itertools import chain
import numpy as np
#import gc
#import Levenshtein
import difflib
print (sys.version)

if(sys.version == "2.7.6 (default, Jun 22 2015, 17:58:13) \n[GCC 4.8.2]") :
    os.chdir("/home/benjamin/Documents/CDiscount/")
else :
    os.chdir("D:/Users/Benjamin/Documents/Data Science/CDiscount/")

Dico = pd.read_csv("data/SortedDescTraining.csv",sep = ";",encoding = "utf-8",header = None,names = ["word"])
Dico.shape
Dico.head
d = {key:0 for key in Dico["word"]}

Train = pd.read_csv("data/trainingClean.csv",sep = ";",encoding = "utf-8")

###remove the words seen less than 10 times
import time
start_time = time.clock()
for desc in Train["Description"].dropna() :
    if len(desc) > 0 :
        for word in desc.split() :
            if(word in d) :
                d[word] += 1
print(time.clock() - start_time, "seconds")
#around 1 min

dClean = {key : value for (key,value) in d.iteritems() if value > 50}
dClean = {key : value for (key,value) in d.items() if value > 50}
dCleanLi = [el for el in dClean]
dCleanLi.sort()
sortedUniqueDescr= pd.Series(dCleanLi)
sortedUniqueDescr.to_csv("data/SortedDescTraining50+.csv", sep = ";" ,index = 0 , encoding  = "utf-8") 

with open("data/CountInTrain.txt","w") as f :
    f.write('\n'.join([';'.join([key,value]) for (key,value) in d.items()]) )

#TO DO : merge script 2 and 2 bis : 
#take all the words
#make script 2-bis
#change the last loop with the condition : if(wordfreq < wordfreq2) [not mandatory, but can bee cool]
#remove the cluster where the most frequent word has a frenquency of less than 10 or 20
#merge the words from the dict created and the data base
#hope this is better in a true CV (script 4) :-)

#
####
#varA = 'plaimountain'
#varB = 'piaimauntain'
#varC = 'skymountain'
#varS = ['piaimauntain','sky','skymountain','dog','231']
#
##it parse varB by letters
#best = difflib.get_close_matches(varA, varB)
#print(best)
#
#best = difflib.get_close_matches(varA, [varB])
#print(best)
#
#best = difflib.get_close_matches(varA, [varB,varC])
#print(best)
#
#best = difflib.get_close_matches(varA, list(Dico["word"]) )
#print(best)
##http://spams-devel.gforge.inria.fr/downloads.html
####hierarchical clustering : niet !
#Nmax = len(Dico["word"])
#Nmax =10000
#import time
#start_time = time.clock()
#for i in range(Nmax) :
#    varA = Dico["word"][i]
#    for j in range(i+1,Nmax) :
#        varB= Dico["word"][j]
#        a = difflib.SequenceMatcher(None,varA,varB).quick_ratio()
#print(time.clock() - start_time, "seconds")