# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:23:58 2015

@author: Benjamin
"""
import os
import numpy as np
import pandas as pd
import sklearn

os.chdir("D:/Users/Benjamin/Documents/Data Science/CDiscount/")
Train = pd.read_csv("data/training.csv",sep = ";",encoding = "utf-8")

Train.head
Train.columns.values.tolist()

#1. predire la categorie1
#
Train['Categorie1'].unique()
Train['Categorie1']==340
for cat1 in Train['Categorie1'].unique() :
    print(cat1)
    print(Train.loc[Train['Categorie1']==cat1].shape)
    print(len(Train.loc[Train['Categorie1']==cat1]['Categorie2'].unique()))
    print("___________________________")


#file = open("data/training.csv")
#
#for i in range(100): 
#    print(file.readline())
#    
#file.close()