# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 17:30:24 2020

@author: shawn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
pd.pandas.set_option('display.max_columns', None)

score_col=['AVG_MATH_4_SCORE','AVG_MATH_8_SCORE','AVG_READING_4_SCORE','AVG_READING_8_SCORE']

col=['PRIMARY_KEY', 'STATE', 'YEAR', 'ENROLL', 'TOTAL_REVENUE',
       'FEDERAL_REVENUE', 'STATE_REVENUE', 'LOCAL_REVENUE',
       'TOTAL_EXPENDITURE', 'INSTRUCTION_EXPENDITURE',
       'SUPPORT_SERVICES_EXPENDITURE', 
       'CAPITAL_OUTLAY_EXPENDITURE',  'GRADES_KG_G',
       'GRADES_4_G',  'GRADES_1_8_G',
       'GRADES_9_12_G', 'GRADES_ALL_G','AVG_READING_4_SCORE']

data = pd.read_csv('states_all_extended.csv')

def dataDescribe(data):
    print("数据表格行列数：",data.shape)
    print("年份的个数：",len(data['YEAR'].unique()))
    print("地区的个数：",len(data['STATE'].unique()))
    print()
print(data.shape)

vars_with_na = [var for var in data.columns if data[var].isnull().sum()>1]
print(len(vars_with_na))
dict_missing = { var: np.round(data[var].isnull().mean()*100, 3) for var in vars_with_na}
sorted_dict = sorted(dict_missing.items(), key=lambda kv: kv[1], reverse=True)
print(sorted_dict)
col_to_drop=[item[0] for item in sorted_dict if(item[1]>70)]
print(col_to_drop)
data.drop(columns=col_to_drop,inplace=True)
for item in score_col:
    print(item,data[item].isnull().sum())
    
data=data.loc[~(data['AVG_READING_4_SCORE'].isnull()),col]
data=data.loc[data['YEAR']!=2017,:]
for item in data.columns:
    print(item,data[item].isnull().sum())
print(data.shape)
print(data['GRADES_KG_G']+data['GRADES_1_8_G']+data['GRADES_9_12_G']-data['GRADES_ALL_G'])
#for item in data.columns:
#    print(item,data[item].isnull().sum())
#data.drop(columns=['AVG_MATH_4_SCORE','AVG_MATH_8_SCORE','AVG_READING_8_SCORE'],inplace=True)
#print(data['STATE'].unique(),len(data['STATE'].unique()))
#arr1=data['STATE'].unique().copy()
#data.dropna(axis=0,inplace=True)
#print(data['STATE'].unique())
#arr2=data['STATE'].unique().copy()
#for item in arr1:
#    print(item,item in arr2)