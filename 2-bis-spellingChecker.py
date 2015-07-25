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

#make the frequency of the words :
Train = pd.read_csv("data/trainingClean.csv",sep = ";",encoding = "utf-8")
sizes = {}
###remove the words seen less than 10 times
import time
start_time = time.clock()
for desc in Train["Description"].dropna() :
    if len(desc) > 0 :
        for word in desc.split() :
            if(word in sizes) :
                sizes[word] += 1
            else :
                sizes[word] = 1
print(time.clock() - start_time, "seconds")
#70s.

#import previous dictionnary
Dico = pd.read_csv("data/SortedDescTraining.csv",sep = ";",encoding = "utf-8",header = None,names = ["word"])

#build the spelling matches
i = 1
start_time = time.clock()
matches = {}
sortedDict = Dico["word"].dropna().copy()
sortedDict.sort()
for word in sortedDict :
#    matches[word] = difflib.get_close_matches(word, sortedDict[i:(i+200)],cutoff=0.90,n=10)
    matches[word] = []
    matcher = difflib.SequenceMatcher(None,word,"")
    for word2 in sortedDict[i:(i+300)] :
        matcher.set_seq2(word2)
        match = matcher.find_longest_match(0,len(word),0,len(word2))
        minSize = min(len(word),len(word2))
        maxSize = max(len(word),len(word2))
        if minSize > 5 :
            if (match[2]) > min(int(minSize*0.8),minSize-1) :
                 matches[word].append(word2)
    i +=1
print(time.clock() - start_time, "seconds")
#483 s.
#3679


#make the "clusters"
#idea : graph based would be better
#check the clusters : make links between words in cluster, and remove those that do not belong (aimer - aimanter par ex)
#matches = {"aa":["aa","bb","cc"],"bb":["dd","ee"]}
start_time = time.clock()
def getFrq(x) :
    return sizes[x]
matchesClean = {}
for key in matches :
    li = matches[key]
    li.append(key)
    li.sort(key = getFrq,reverse = True)
    if li[0] in matchesClean :
        matchesClean[li[0]]+= li
        matchesClean[li[0]] = list(set(matchesClean[li[0]]))
    else :
        matchesClean[li[0]] = list(set(li))
    for el in matches[key] :
        if el in matchesClean and el != li[0] :
            matchesClean[li[0]]+=matchesClean[el]
            matchesClean[li[0]] = list(set( matchesClean[li[0]]))
            matchesClean.pop(el, None)
print(time.clock() - start_time, "seconds")
#2 s. 

def flatten(listOfLists):
    return list(chain.from_iterable(listOfLists))
li = [[';'.join([key,el]) for el in set(value)] for (key,value) in matchesClean.items() ]
with open("data/CorrespDicoSubstringLength.txt","w") as f :
    f.write('\n'.join(flatten(li)))

########################################
########################################




import sys
import os
import pandas as pd
#import re
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

#make the frequency of the words :
Train = pd.read_csv("data/trainingClean.csv",sep = ";",encoding = "utf-8")
sizes = {}
###remove the words seen less than 10 times
import time
start_time = time.clock()
for desc in Train["Description"].dropna() :
    if len(desc) > 0 :
        for word in desc.split() :
            if(word in sizes) :
                sizes[word] += 1
            else :
                sizes[word] = 1
print(time.clock() - start_time, "seconds")
#70s.

#import previous dictionnary
Dico = pd.read_csv("data/SortedDescTraining.csv",sep = ";",encoding = "utf-8",header = None,names = ["word"])
d = {}
with open("data/CorrespDicoSubstringLength.txt","r",encoding="utf-8") as f :
    for line in f :
        lines = line.replace("\n","").split(';')
        if(lines[0] in d ) :
            d[lines[0]].append(lines[1])
        else :
            d[lines[0]] = [lines[1]]
d["longle"]

dtDict = pd.read_csv("data/CorrespDicoSubstringLength.txt",sep = ";",encoding = "utf-8",header = None,names = ["ref","word"])
dtDict.set_index("ref",inplace = True)

sizesClust = { key:sum([sizes[el] for el in value]) for (key,value) in d.items() }
sizesClust50 = [key for (key,value) in sizesClust.items() if value > 50]

dt50 = pd.DataFrame(data={"ref":sizesClust50})
dt50.set_index("ref",inplace = True)


dtDictClean = dt50.join(dtDict,how="left")
dtDictClean.reset_index(inplace = True)
#dtDictClean.set_index("word",inplace = True)
wordsOk = set(dtDictClean.index)
len(wordsOk)

dictClean = {}
start_time = time.clock()
i = 0
for word in dtDictClean["word"] :
    dictClean[word] = dtDictClean["ref"][i]
    i += 1
print(time.clock() - start_time, "seconds")
#5 s.

def extract_ref(word,ref = dictClean) :
    if word in  dictClean :
        res = dictClean[word]
        return res
    else :
        return ""

def clean_review(review,ref = dictClean) :
    if type(review) ==  type(u"") :
        rev = review.split()
        res = [extract_ref(word,ref) for word in rev]
        return " ".join(res)
    else :
        return "NAN"
    
import time
start_time = time.clock()
i = 0
for description in Train["Description"]:
#    Train["Description"][i] = clean_review(description)
    clean_review(description)
    i += 1
    if(i % 10000 == 0) :
        print("%d/%d" % (i,Train.shape[0]))
print(time.clock() - start_time, "seconds")
#96 s.

Train.to_csv("data/trainingSpellChecked.csv", sep = ";" ,index = 0 , encoding  = "utf-8") 








dt50.index[16874] in set(sizesClust50)

matchesClean["demagog"]
li[3]
#retourner le dico et modifier les mots dans Train
#filtrer les mots avec trop peu d'occurence
cleanDB = { el:key}












###########################
myDicDF = pd.read_csv("data/SortedDescTraining50+.csv",sep = ";",encoding = "utf-8",header = None,names = ["word"])
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



#TO DO : assign the words with the higher frequency, instead of the first word




