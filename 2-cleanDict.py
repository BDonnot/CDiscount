# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 20:36:57 2015

@author: Benjamin
"""

import sys
import os
import pandas as pd
from itertools import chain
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




###
varA = 'plaimountain'
varB = 'piaimauntain'
varC = 'skymountain'
varS = ['piaimauntain','sky','skymountain','dog','231']

#it parse varB by letters
best = difflib.get_close_matches(varA, varB)
print(best)

best = difflib.get_close_matches(varA, [varB])
print(best)

best = difflib.get_close_matches(varA, [varB,varC])
print(best)

best = difflib.get_close_matches(varA, list(Dico["word"]) )
print(best)
#http://spams-devel.gforge.inria.fr/downloads.html
###hierarchical clustering : niet !
Nmax = len(Dico["word"])
Nmax =10000
import time
start_time = time.clock()
for i in range(Nmax) :
    varA = Dico["word"][i]
    for j in range(i+1,Nmax) :
        varB= Dico["word"][j]
        a = difflib.SequenceMatcher(None,varA,varB).quick_ratio()
print(time.clock() - start_time, "seconds")