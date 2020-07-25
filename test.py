# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 22:54:40 2020

@author: Fatema Akter
"""

SPY={}
i=0
PriceChange=[]

f=open("SPY1.csv", 'r')

for line in f:
    SPYList = line.split(',')
    SPY[i]={}
    SPY[i]["date"] = SPYList[0]
    SPY[i]["open"]=SPYList[1]
    SPY[i]["high"]=SPYList[2]
    SPY[i]["low"]=SPYList[3]
    SPY[i]["close"]=SPYList[4]
    SPY[i]["volume"]=SPYList[6]
   
    
    if i>0:
        closeDiff =float(SPY[i]['close']) - float(SPY[i-1]['close'])
        PriceChange.append(closeDiff)

    i+=1