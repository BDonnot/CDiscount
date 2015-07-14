import sys
import os
import pandas as pd
print (sys.version)

if(sys.version == "2.7.6 (default, Jun 22 2015, 17:58:13) \n[GCC 4.8.2]") :
    os.chdir("/home/benjamin/Documents/CDiscount/")
else :
    os.chdir("D:/Users/Benjamin/Documents/Data Science/CDiscount/")
    
Train = pd.read_csv("data/trainingClean-Words.csv",sep = ";",encoding = "utf-8")