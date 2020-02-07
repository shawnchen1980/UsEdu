# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:16:39 2020

@author: shawn
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler,MinMaxScaler
import seaborn as sns #for plotting
from sklearn.ensemble import RandomForestClassifier #for the model
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz #plot tree
from sklearn.metrics import roc_curve, auc #for model evaluation
from sklearn.metrics import classification_report #for model evaluation
from sklearn.metrics import confusion_matrix #for model evaluation
from sklearn.model_selection import train_test_split #for data splitting
import eli5 #for purmutation importance
from eli5.sklearn import PermutationImportance
import shap #for SHAP values
from pdpbox import pdp, info_plots #for partial plots
np.random.seed(123) #ensure reproducibility
scaler=MinMaxScaler()
arr1=[2000,2003,2005,2007,2009,2011,2013,2015,2017]
files=["fedRevPercentOfTotalRev",
       "fullTimeTeacher",
       "instruExpenPerPupil",
       "instruExpenSalary",
       "instruPercentCurrentExpen",
       "localRevAsPercentTotalRev",
       "localTuitionFee",
       "pupilTeacherRatio",
       "totalCurrentExpendituresPerPupil",
       "totalRevenuePerPupil",
       "totalSalaryExpen",
       "totalStudents"]
print(f"naep{arr1[0]}mathg4.csv")
df=pd.read_csv(f"naep{arr1[0]}mathg4.csv")

def generateMarkDf():
    arr=list()
    
    for i in arr1:
        df=pd.read_csv(f"naep{i}mathg4.csv")
        df.insert(0,'Year',i)
        df["State Name"]=[i.upper() for i in df["Jurisdiction"]]
        arr.append(df)
        
    df=pd.concat(arr)
    return df

def plotDf(file):
    df2=pd.read_csv(f"{file}.csv")
    fig,ax=plt.subplots()
    df2.iloc[:,[1]].hist(ax=ax)
    df2.iloc[:,[1]].plot.kde(ax=ax)


def generateSingleColumn(file):
#    df2=pd.read_csv("pupilTeacherRatio.csv")
    df2=pd.read_csv(f"{file}.csv")
    df2.iloc[:,1:]=scaler.fit_transform(df2.iloc[:,1:])
#    states=df2["State Name"].unique().tolist()
#    #df=df.loc[df["State Name"].isin(states)]
    arr=list()
    for i in range(1,len(df2.columns)):
        df3=df2.iloc[:,[0,i]]
        df3.columns=['State Name',file]
        df3.insert(0,'Year',df2.columns[i][-7:-3])
        arr.append(df3)
    df3=pd.concat(arr)
    return df3

#df4=generateSingleColumn("pupilTeacherRatio")
def generateColumns(files):
    dfs=[generateSingleColumn(f) for f in files]
    s=dfs[0]
    for i in range(1,len(files)):
        s=pd.merge(s,dfs[i])
    return s
def generateFinalData():
    dfd=generateColumns(files)
    dfd['Year']=dfd['Year'].astype('int64')
    df=generateMarkDf()
    dfd=pd.merge(dfd,df.loc[:,['Year','State Name','SigSymbol']])
    dfd['SigSymbol'].value_counts().plot(kind='bar')
    dfd=dfd.dropna()
    dfd=pd.get_dummies(dfd,columns=['State Name'])
    return dfd

df=generateFinalData()
#plotDf(files[5])