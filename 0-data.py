# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:23:58 2015

@author: Benjamin
"""
import os
import numpy as np
import pandas as pd
import sklearn
import re
import nltk
from bs4 import BeautifulSoup 
from unidecode import unidecode
#some french stop words
stopwords = ['au', 'aux', 'avec',
'ce', 'ces', 'dans', 'de', 'des',
'du', 'elle', 'en', 'et', 'eux',
'il', 'je', 'la', 'le', 'leur',
'lui', 'ma', 'mais', 'me', 'même',
'mes', 'moi', 'mon', 'ne', 'nos', 'notre',
'nous', 'on', 'ou', 'par', 'pas', 'pour',
'qu', 'que', 'qui', 'sa', 'se', 'ses',
'son', 'sur', 'ta', 'te', 'tes', 'toi',
'ton', 'tu', 'un', 'une', 'vos', 'votre',
'vous', 'c', 'd', 'j', 'l', 'à', 'm', 'n',
's', 't', 'y', 'été', 'étée', 'étées',
'étés', 'étant', 'étante', 'étants',
'étantes', 'suis', 'es', 'est', 'sommes',
'êtes', 'sont', 'serai', 'seras', 'sera',
'serons', 'serez', 'seront', 'serais', 'serait',
'serions', 'seriez', 'seraient', 'étais', 'était',
'étions', 'étiez', 'étaient', 'fus', 'fut',
'fûmes', 'fûtes', 'furent', 'sois', 'soit',
'soyons', 'soyez', 'soient', 'fusse', 'fusses',
'fût', 'fussions', 'fussiez', 'fussent', 'ayant',
'ayante', 'ayantes', 'ayants', 'eu', 'eue', 'eues',
'eus', 'ai', 'as', 'avons', 'avez', 'ont', 'aurai',
'auras', 'aura', 'aurons', 'aurez', 'auront',
'aurais', 'aurait', 'aurions', 'auriez', 'auraient',
'avais', 'avait', 'avions', 'aviez', 'avaient', 'eut',
'eûmes', 'eûtes', 'eurent', 'aie', 'aies', 'ait',
'ayons', 'ayez', 'aient', 'eusse', 'eusses', 'eût',
'eussions', 'eussiez', 'eussent']
stopwords = set(stopwords) 

from nltk.corpus import brown
brown.words()

os.chdir("D:/Users/Benjamin/Documents/Data Science/CDiscount/")
Train = pd.read_csv("data/training.csv",sep = ";",encoding = "utf-8")

Train.head
Train.columns.values.tolist()

#1. predire la categorie1
Train['Categorie1'].unique()
Train['Categorie1']==340
for cat1 in Train['Categorie1'].unique() :
    print(cat1)
    print(Train.loc[Train['Categorie1']==cat1].shape)
    print(len(Train.loc[Train['Categorie1']==cat1]['Categorie2'].unique()))
    print("___________________________")



def normalize_review( review,stopwords=stopwords):
    # 1. Remove HTML
    review = BeautifulSoup(review).get_text() 
    # 2. range everything in ascii
    review = unidecode(review)
    # 3. Remove non-letters letters_onlyCC
    letters_only = re.sub("[^a-zA-Z]", " ", review) 
    # 4. Convert to lower case, split into individual words
    words = letters_only.lower().split()
    # 5. Remove stop words
    meaningful_words = [w for w in words if not w in stopwords]   
    # 6. Join the words back into one string separated by space, 
    # and return the result.
    return( " ".join( meaningful_words ))   
    
for description in Train["Description"] :
    Train["Description"] = normalize_review(description)
    
Train.save("data/trainingClean.csv") 


normalize_review(Train["Description"][0])
Train["Description"][0] = Train["Description"][0]
Train["DescriptionClean"] = 0
Train["DescriptionClean"][3546]
#file = open("data/training.csv")
#
#for i in range(100): 
#    print(file.readline())
#    
#file.close()