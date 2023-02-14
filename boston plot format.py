# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:27:32 2023

@author: hank1
1. 研究動機
研究目的
使用方法
成果分析

結論與建議
未來展望
參考資料
"""

from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
# 圖形設定
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size']=20
boston=datasets.load_boston()
df=pd.DataFrame(boston.data,columns=boston.feature_names)
df["MEDV"]=boston.target # 新增資料組到df中
#print(df)


#使用plot method，這樣才能標示label
# 為了區分出在查爾斯河河畔與否，並使用顏色標注。因此這邊將之拆分成兩個資料組
CHAS0={"RM":[],"LSTAT":[],"NOX":[],"MEDV":[]} #字典內含串列
CHAS1={"RM":[],"LSTAT":[],"NOX":[],"MEDV":[]}
for i in range(len(df.MEDV)):
    if int(df.CHAS[i])==0: #值為浮點數，但因只有0與1。故先轉成整數來判斷
        CHAS0['RM'].append(df.RM[i])
        CHAS0['LSTAT'].append(df.LSTAT[i])
        CHAS0['NOX'].append(df.NOX[i])
        CHAS0['MEDV'].append(float(df.MEDV[i])) #避免後面size出問題
    else:
        CHAS1['RM'].append(df.RM[i])
        CHAS1['LSTAT'].append(df.LSTAT[i])
        CHAS1['NOX'].append(df.NOX[i])
        CHAS1['MEDV'].append(float(df.MEDV[i]))
        
plt.figure(figsize=(15,15))   
axes = plt.subplot(projection='3d')  #設定成三D
axes.plot(CHAS0['RM'],CHAS0['LSTAT'],CHAS0['NOX'],"x",label="CHAS 0",alpha=0.1,markersize=10)   
axes.plot(CHAS1['RM'],CHAS1['LSTAT'],CHAS1['NOX'],"o",label="CHAS 1",alpha=0.5,markersize=10)  

axes.set_xlabel("RM: 每棟住宅的房間數")
axes.set_ylabel("LSTAT: 地區中有多少房東是屬於低收入戶族群")
axes.set_zlabel("NOx: 氮氧化物(10ppm)")


axes.yaxis.labelpad=30 #label相對位置調整
axes.zaxis.labelpad=30
axes.xaxis.labelpad=30

plt.legend()
plt.savefig('波士頓房價與因子散佈圖(plot).png', bbox_inches='tight')
plt.show()

plt.figure(figsize=(17,17))  

axes = plt.axes(projection='3d')
#axes.set(xlim=(5,8),ylim=(5,30),zlim=(0.5,0.6))
"""
axes.set_xlim(5,8)
axes.set_ylim(5,30)
axes.set_zlim(0.5,0.6)
"""
axes.scatter(CHAS0['RM'],CHAS0['LSTAT'], CHAS0['NOX'],\
     s=5*np.array(CHAS0['MEDV']),c="blue",\
     marker="o",alpha=0.2,label="遠離查爾斯河畔")
axes.scatter(CHAS1['RM'],CHAS1['LSTAT'], CHAS1['NOX'],\
     s=5*np.array(CHAS1['MEDV']),c="red",\
     marker="o",alpha=0.6,label="接近查爾斯河畔")
axes.set_xlabel("RM: 每棟住宅的房間數")
axes.set_ylabel("LSTAT: 地區中有多少房東屬於低收入人群")
axes.set_zlabel("NOx: 氮氧化物(10ppm)")
#axes.dist = 10

axes.yaxis.labelpad=30 #label相對位置調整
axes.zaxis.labelpad=30
axes.xaxis.labelpad=30

plt.legend()
txt="點的大小與價格成正相關"
plt.figtext(0.5, 0.10, txt, wrap=True, horizontalalignment='center', fontsize=16)
plt.savefig('波士頓房價與因子散佈圖(scatter).png', bbox_inches='tight')
plt.show()
