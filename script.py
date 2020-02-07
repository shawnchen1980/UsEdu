# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 09:48:17 2020

@author: shawn
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
import warnings

def heatPlot(df):
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(15, 15))
    sns.heatmap(corr, annot=True,
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)

def avgVsTotPlot(df):
    sns.jointplot("average_expenditure", "AVG_READING_4_SCORE", data=df, kind="reg")
    sns.jointplot("TOTAL_REVENUE", "AVG_READING_4_SCORE", data=df, kind="reg")

def generateXY(df):
    df1=df.drop(['PRIMARY_KEY','AVG_MATH_8_SCORE','AVG_READING_4_SCORE','AVG_READING_8_SCORE','ENROLL'],axis=1)
    df2=df1.dropna()
    z=df2.loc[:,'AVG_MATH_4_SCORE'].values.copy()
    df3 = pd.get_dummies(df2, columns=['STATE'],drop_first=True)
    df4=(df3-df3.mean())/df3.std()
    print(df3.shape)
    y=df4.loc[:,'AVG_MATH_4_SCORE'].values
    X=df4.drop(['AVG_MATH_4_SCORE'],axis=1).loc[:,:].values
    return X,y,z

def rfRegressor(df):
    X,y,z=generateXY(df)
    rf=RandomForestRegressor()

    parameters = {'n_estimators': [4, 6, 9], 
                  'max_features': ['log2', 'sqrt','auto'], 
                  'max_depth': [2, 3, 5, 10], 
                  'min_samples_split': [2, 3, 5],
                  'min_samples_leaf': [1,5,8]
                 }
    
    # Run the grid search
    grid_obj = GridSearchCV(rf, parameters, cv=5)
    grid_obj = grid_obj.fit(X, z)
    
    # Set the clf to the best combination of parameters
    rf = grid_obj.best_estimator_
    
    # Fit the best algorithm to the data. 
    print('Params ',rf)
    print('Score ',rf.score(X, z))

df=pd.read_csv('states_all.csv')
df.isna().sum()*100/df.shape[0]
df['average_reveneue']=df['TOTAL_REVENUE']/df['GRADES_ALL_G']
df['average_expenditure']=df['TOTAL_EXPENDITURE']/df['GRADES_ALL_G']

#画热力图
#heatPlot(df)

#平均投入与总投入对成绩的影响对比
#avgVsTotPlot(df
x,y,z=generateXY(df)
rfRegressor(df)