# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 23:06:05 2015

@author: Benjamin
"""

import sys
import os
import pandas as pd
#from itertools import chain
#import numpy as np
#import gc
#import Levenshtein
#import difflib
print (sys.version)

if(sys.version == "2.7.6 (default, Jun 22 2015, 17:58:13) \n[GCC 4.8.2]") :
    os.chdir("/home/benjamin/Documents/CDiscount/")
else :
    os.chdir("D:/Users/Benjamin/Documents/Data Science/CDiscount/")

myDicDF = pd.read_csv("data/SortedDescTraining50+.csv",sep = ";",encoding = "utf-8",header = None,names = ["word"])
Dico = {key:{} for key in myDicDF['word']}
Train = pd.read_csv("data/trainingClean.csv",sep = ";",encoding = "utf-8")

def extractWordsInDic(descr,dico = Dico) :
    if type(descr) != type(u"") :
        return ""
    split = descr.split()
    split = filter(lambda x : x in dico, split)
    return ' '.join(split)

import time
start_time = time.clock()
i = 0
for description in Train["Description"]:
    Train["Description"][i] = extractWordsInDic(description)
    i += 1
    if(i % 10000 == 0) :
        print("%d/%d" % (i,Train.shape[0]))
print(time.clock() - start_time, "seconds")
##284 s.

Train.to_csv("data/training_Dict50+.csv", sep = ";" ,index = 0 , encoding  = "utf-8") 

Train["Description"][791]

############################################
import time
start_time = time.clock()
for i in range(Train.shape[0]) :
    desc = Train["Description"][i]
    if type(desc) != type(u"") :
        continue
    cat = Train["Categorie3"][i]
    for word in desc.split() :
            if(word in Dico) :
                if (cat in Dico[word]) :
                    Dico[word][cat] += 1
                else :
                    Dico[word][cat] = 1
print(time.clock() - start_time, "seconds")
sumPerWord = { key:sum([value for (cat,value) in x.items()]) for (key,x) in Dico.items()}

dRatio = { word:{cat:value/sumPerWord[word] for (cat,value) in x.items()} for (word,x) in Dico.items() }
dRatio['delicieusement']

sumPerWord.__init__()

TrainS = Train.loc[0:100000,:].copy()
desc = TrainS["Description"][0]

dShort = {el:dic for (el,dic) in Dico.items() if len(dic) > 0}

sumPerWord[1]