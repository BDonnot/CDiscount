# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 23:06:05 2015

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

Dico = pd.read_csv("data/SortedDescTraining50+.csv",sep = ";",encoding = "utf-8",header = None,names = ["word"])
d = {key:{} for key in Dico['word']}
Train = pd.read_csv("data/trainingClean.csv",sep = ";",encoding = "utf-8")

import time
start_time = time.clock()
for i in range(Train.shape[0]) :
    desc = Train["Description"][i]
    if type(desc) != type(u"") :
        continue
    cat = Train["Categorie3"][i]
    for word in desc.split() :
            if(word in d) :
                if (cat in d[word]) :
                    d[word][cat] += 1
                else :
                    d[word][cat] = 1
print(time.clock() - start_time, "seconds")


TrainS = Train.loc[0:100000,:].copy()
desc = TrainS["Description"][0]

dShort = {el:dic for (el,dic) in d.iteritems() if len(dic) > 0}
