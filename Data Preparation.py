# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 20:56:29 2023

@author: matth
"""

import pandas as pd
import numpy as np
import os

year = '2022'
path = os.getcwd() +"\\Results\\"+ year+".csv"
matches= pd.read_csv(path)


def printfull (dataframe):
   with pd.option_context('display.max_rows', None,
                          'display.max_columns', None,
                          'display.precision', 3,
                          ):
        print(dataframe)

##printfull(matches.head())



matches['HomexG']=matches['xG']
matches['AwayxG']=matches['xG.1']

matches=matches[['Wk','Day','Date','Time','Home','HomexG','Home Goals','Away','AwayxG','Away Goals']]


for i in range(0,len(matches)):
    if matches.at[i,'Home Goals'] > matches.at[i,'Away Goals']:
        matches.at[i, 'HomeResult']='W'
        matches.at[i, 'AwayResult']='L'
        matches.at[i, 'HomePoints']=3
        matches.at[i, 'AwayPoints']=0
    elif matches.at[i,'Home Goals'] < matches.at[i,'Away Goals']:
        matches.at[i, 'HomeResult']='L'
        matches.at[i, 'AwayResult']='W'
        matches.at[i, 'HomePoints']=0
        matches.at[i, 'AwayPoints']=3
    else:
        matches.at[i, 'HomeResult']='D'
        matches.at[i, 'AwayResult']='D'
        matches.at[i, 'HomePoints']=1
        matches.at[i, 'AwayPoints']=1
        
PlayedMatches=matches[np.invert(np.isnan(matches['Home Goals']))]
PlayedMatches.head()