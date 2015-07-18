# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 20:13:54 2015

@author: Benjamin
"""
import sys
import os
import pandas as pd
if(sys.version == "2.7.6 (default, Jun 22 2015, 17:58:13) \n[GCC 4.8.2]") :
    os.chdir("/home/benjamin/Documents/CDiscount/")
else :
    os.chdir("D:/Users/Benjamin/Documents/Data Science/CDiscount/")
    
from sklearn.svm import LinearSVC
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
pipeline = Pipeline([('tfidf', TfidfTransformer()),
                      ('chi2', SelectKBest(chi2, k=1000)),
                      ('nb', MultinomialNB())])
classifNB = SklearnClassifier(pipeline)

pipeline = Pipeline([('tfidf', TfidfTransformer()),
                      ('chi2', SelectKBest(chi2, k=1000)),
                      ('svm', LinearSVC())])
classifSVM = SklearnClassifier(pipeline)
Train = pd.read_csv("data/training_Dict50+.csv",sep = ";",encoding = "utf-8")
Train.head
myDicDF = pd.read_csv("data/SortedDescTraining50+.csv",sep = ";",encoding = "utf-8",header = None,names = ["word"])
Dico = {key:{} for key in myDicDF['word']}

def getFeatures(descr,voc=Dico) :
    if (type(descr) != type(u"")) :    
        return {'a':1}
    mySet = descr.split()
    return {x:1 for x in mySet}

import time
import random
nTrain = 100000
nTest = 10000
sampTest = random.sample(range(nTrain),nTest)
sampTrain = random.sample(range(Train.shape[0]),nTrain)

start_time = time.clock() 
train_set = []
for i in sampTrain :
    train_set.append( (getFeatures(Train["Description"][i]),Train["Categorie3"][i]) )
print(time.clock() - start_time, "seconds")
#13.6 for 1000
#4.49 for 1000
#460 for 100000
#3.3 for 100000


start_time = time.clock() 
classifNB.train(train_set)
print(time.clock() - start_time, "seconds")
#0.32
#15.61 for nTrain = 100000
start_time = time.clock() 
res = classifNB.classify_many( [ getFeatures(descr) for descr in Train["Description"][sampTest] ] )
print(time.clock() - start_time, "seconds")
answer = res == Train["Categorie3"][sampTest]
print("multinomialNB : %f" % len(answer[answer])/nTest) #0.82 for cat1 / 0.0014 for cat3

start_time = time.clock() 
classifSVM.train(train_set)
print(time.clock() - start_time, "seconds")
#400

start_time = time.clock() 
res = classifSVM.classify_many( [ getFeatures(descr) for descr in Train["Description"][sampTest] ] )
print(time.clock() - start_time, "seconds")
answer = res == Train["Categorie3"][sampTest]
print("SVM : %d" % len(answer[answer])/nTest) #87% for cat1 / 0.0076% for cat3