# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 09:14:40 2019

# Enrollment
https://nces.ed.gov/ccd/stnfis.asp
# Financials
https://www.census.gov/programs-surveys/school-finances/data/tables.html
# Academic Achievement
https://www.nationsreportcard.gov/ndecore/xplore/NDE


@author: shawn
"""

import numpy as np
import pandas as pd

df=pd.read_csv("states_all.csv",index_col=0)

#如何知道df是几维函数，每个维度的长度是多少，元素类型是什么，
#每个元素占用字节多少，元素个数是多少个，总共占用内存多少字节
print(df.ndim,df.shape,df.values.itemsize,df.size,df.values.dtype)
print(df.dtypes)

#如何查看df的列标签和行标签
print(df.index,df.columns)

#如何看2016年的数据
print(df[df.YEAR==2016])

#如何获取前三行数据，前三列数据，前三行和前三列数据
print(df.iloc[:3],df.iloc[:,:3],df.iloc[:3,:3])


#如何看2002年犹他州的一些数据
print(df.loc["2002_UTAH","STATE":"GRADES_ALL_G"])

#如何看美国有哪些州,如何选出正常的州
print(df.STATE.unique(),df.STATE.unique()[:51])

#如何筛选出正常州的数据
states=df.STATE.unique()[:51]
print(df.shape)
df=df.loc[df["STATE"].isin(states)]
print(df.shape,df.STATE)