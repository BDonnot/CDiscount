# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 19:29:35 2015

@author: Benjamin
"""

import sys
import os
import pandas as pd
import re
from itertools import chain
#import numpy as np
#import gc
#import Levenshtein
import difflib
print (sys.version)

if(sys.version == "2.7.6 (default, Jun 22 2015, 17:58:13) \n[GCC 4.8.2]") :
    os.chdir("/home/benjamin/Documents/CDiscount/")
else :
    os.chdir("D:/Users/Benjamin/Documents/Data Science/CDiscount/")

myDicDF = pd.read_csv("data/SortedDescTraining50+.csv",sep = ";",encoding = "utf-8",header = None,names = ["word"])
Dico = pd.read_csv("data/SortedDescTraining.csv",sep = ";",encoding = "utf-8",header = None,names = ["word"])
prog=re.compile(r"((ez)$)|((ons)$)|((eais)$)|((eait)$)|((ant)$)|((erai)$)|((era)$)|((eront)$)|((erez)$)|((erait)$)|((issons)$)|((issez)$)|((irais)$)|((irait)$)|((aient)$)")
verbs = []
for word in myDicDF["word"] :
    if prog.search(word) :
        verbs.append(word)
#print(verbs)
with open("data/dicVerbs.txt","w") as f :
    f.write('\n'.join(verbs))
#verbs_base = ['abrit','absorb','acced','accel','accentu','accept','accessoiris','acclimat','accompagn',
#              'accord','accroch','accroch','accueill','achet','acour',
#'compos','compr','compt','concern','concev','condui','confection','confer']
i = 1
import time
start_time = time.clock()
matches = {}
sortedDict = Dico["word"].dropna().copy()
sortedDict.sort()
for word in sortedDict :
    matches[word] = difflib.get_close_matches(word, sortedDict[i:(i+200)],cutoff=0.90,n=10)
    i +=1
print(time.clock() - start_time, "seconds")
   
matches['aimant']

start_time = time.clock()
matchesClean = {}
for key in matches :
    li = matches[key]
    li.append(key)
    li.sort()
    if li[0] in matchesClean :
        matchesClean[li[0]]+=li[1:]
    else :
        matchesClean[li[0]] = li[1:]
    for el in li[1:] :
        if el in matchesClean :
            matchesClean[li[0]]+=matchesClean[el]
            matchesClean.pop(el, None)
print(time.clock() - start_time, "seconds")
#2 s.     
for key in matchesClean :
    print(key)
    break

def flatten(listOfLists):
    return list(chain.from_iterable(listOfLists))
li = [[';'.join([key,el]) for el in value] for (key,value) in matchesClean.items() ]
li += [[';'.join([key,key])] for key in  matchesClean ]
with open("data/CorrespDico.txt","w") as f :
    f.write('\n'.join(flatten(li)))

#TO DO : assign the words with the higher frequency, instead of the first word




