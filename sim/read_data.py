#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:40:17 2020

@author: ttumuon
"""


import pandas as pd

df = pd.read_csv('debug2.txt')

df.columns = df.columns.str.strip() #important for accessing columns
#print(df.columns)
#print(df.info())

print(df)

#mu3 = df.query('mu_id==3')
#print(mu3.query('status==1'))

#print(mu3.loc)


#events = df.query('status!=1')
#events = df.query('status!=4') and df.query('status!=1')
"""
events = df[ (df.part!=4) & ((df.part!='mu+') & (df.part!='mu-')) ]
print(events)
"""
#print(df[(df.status != 4)])

#print(df.head(15))
