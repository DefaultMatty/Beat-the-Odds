# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 20:56:29 2023

@author: matth
"""

import pandas as pd
import numpy as np
import os

year = '2022'
path = os.getcwd() +"\\results\\"+ year+".csv"
matches= pd.read_csv("C:\\Users\\matth\\OneDrive\\Desktop\\Independant Research Project\\allgames.csv")




matches['HomexG']=matches['xG']
matches['AwayxG']=matches['xG.1']
matches['HomeGoals']=matches['Score'].str.split('\\|').str[0].astype(int)
matches['AwayGoals']=matches['Score'].str.split('\\|').str[-1].astype(int)

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")


