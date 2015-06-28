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
#file = open("data/training.csv")
#
#for i in range(100): 
#    print(file.readline())
#    
#file.close()