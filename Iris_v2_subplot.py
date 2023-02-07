# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 13:30:59 2023

@author: hank1
"""

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import cluster
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#整理資料
iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df.columns = ["sepal_length","sepal_width","petal_length","petal_width"]  #置換column name



y = iris.target
k = 4
kmeans = cluster.KMeans(n_clusters=k, random_state=0) # random_state為隨機種子碼 原範例為12
kmeans.fit(df) #將分群結果套用模型
kmeans_3group = cluster.KMeans(n_clusters=3, random_state=0)
kmeans_3group.fit(df)
"""
print("K-means Classification:")
print(kmeans.labels_)  # 標示分群結果
print(type(kmeans))
print(kmeans)
"""


#pred_y = np.choose(kmeans.labels_, [0,1,2,3]).astype(np.int64)  
#代號取代，int64涵義參考https://ithelp.ithome.com.tw/articles/10279899
# as type是轉換格式
"""
print("K-means Fix Classification:")
print(pred_y) 
print("Real Classification:")
print(y)
"""
# 現在已經確認分群分好了，現在要進行資料整
# 假定預測完的資料數據與原本的一樣，借此用來整理資料
# 整理資料的目的是為了方便標示顏色
#iris_dict={'g0':{},'g1':{},'g2':{},'g3':{}}
iris_dict_4group={'g0':{'sepal_length':[],'sepal_width':[],'petal_length':[],'petal_width':[]},\
        'g1':{'sepal_length':[],'sepal_width':[],'petal_length':[],'petal_width':[]},\
        'g2':{'sepal_length':[],'sepal_width':[],'petal_length':[],'petal_width':[]},\
        'g3':{'sepal_length':[],'sepal_width':[],'petal_length':[],'petal_width':[]}}
iris_dict_3group={'g0':{'sepal_length':[],'sepal_width':[],'petal_length':[],'petal_width':[]},\
        'g1':{'sepal_length':[],'sepal_width':[],'petal_length':[],'petal_width':[]},\
        'g2':{'sepal_length':[],'sepal_width':[],'petal_length':[],'petal_width':[]}}
#dict要定義清楚，不然塞資料會出問題
pred_index_4group=kmeans.labels_.tolist()
pred_index_3group=kmeans_3group.labels_.tolist()


iris_dict_diffgroup={'sepal_length':[],'sepal_width':[],'petal_length':[],'petal_width':[]}


pred_y = np.choose(kmeans_3group.labels_, [1,0,2]).astype(np.int64)

for i in range(len(pred_y)):
    if pred_y[i]!=iris.target[i]:
        #print(i,pred_y[i],iris.target[i])
        iris_dict_diffgroup['sepal_length'].append(df['sepal_length'][i])
        iris_dict_diffgroup['sepal_width'].append(df['sepal_width'][i])
        iris_dict_diffgroup['petal_length'].append(df['petal_length'][i])
        iris_dict_diffgroup['petal_width'].append(df['petal_width'][i])

for i in range(len(pred_index_4group)):
    #(list_dfspecies[i])
    if pred_index_4group[i]==0:
        
        iris_dict_4group['g0']['sepal_length'].append(df['sepal_length'][i])
        iris_dict_4group['g0']['sepal_width'].append(df['sepal_width'][i])
        iris_dict_4group['g0']['petal_length'].append(df['petal_length'][i])
        iris_dict_4group['g0']['petal_width'].append(df['petal_width'][i])        


    elif pred_index_4group[i]==1:

        iris_dict_4group['g1']['sepal_length'].append(df['sepal_length'][i])
        iris_dict_4group['g1']['sepal_width'].append(df['sepal_width'][i])
        iris_dict_4group['g1']['petal_length'].append(df['petal_length'][i])
        iris_dict_4group['g1']['petal_width'].append(df['petal_width'][i]) 
    elif pred_index_4group[i]==2:

        iris_dict_4group['g2']['sepal_length'].append(df['sepal_length'][i])
        iris_dict_4group['g2']['sepal_width'].append(df['sepal_width'][i])
        iris_dict_4group['g2']['petal_length'].append(df['petal_length'][i])
        iris_dict_4group['g2']['petal_width'].append(df['petal_width'][i]) 
    elif pred_index_4group[i]==3:
        iris_dict_4group['g3']['sepal_length'].append(df['sepal_length'][i])
        iris_dict_4group['g3']['sepal_width'].append(df['sepal_width'][i])
        iris_dict_4group['g3']['petal_length'].append(df['petal_length'][i])
        iris_dict_4group['g3']['petal_width'].append(df['petal_width'][i]) 
    else:
        print("ERROR")        
for i in range(len(pred_index_3group)):
    #(list_dfspecies[i])
    if pred_index_3group[i]==0:
        
        iris_dict_3group['g0']['sepal_length'].append(df['sepal_length'][i])
        iris_dict_3group['g0']['sepal_width'].append(df['sepal_width'][i])
        iris_dict_3group['g0']['petal_length'].append(df['petal_length'][i])
        iris_dict_3group['g0']['petal_width'].append(df['petal_width'][i])        


    elif pred_index_3group[i]==1:

        iris_dict_3group['g1']['sepal_length'].append(df['sepal_length'][i])
        iris_dict_3group['g1']['sepal_width'].append(df['sepal_width'][i])
        iris_dict_3group['g1']['petal_length'].append(df['petal_length'][i])
        iris_dict_3group['g1']['petal_width'].append(df['petal_width'][i]) 
    elif pred_index_3group[i]==2:

        iris_dict_3group['g2']['sepal_length'].append(df['sepal_length'][i])
        iris_dict_3group['g2']['sepal_width'].append(df['sepal_width'][i])
        iris_dict_3group['g2']['petal_length'].append(df['petal_length'][i])
        iris_dict_3group['g2']['petal_width'].append(df['petal_width'][i]) 

    else:
        print("ERROR")  

## 驗證真實資料
iris_realsp_dict={'s0':{'sepal_length':[],'sepal_width':[],'petal_length':[],'petal_width':[]},\
        's1':{'sepal_length':[],'sepal_width':[],'petal_length':[],'petal_width':[]},\
        's2':{'sepal_length':[],'sepal_width':[],'petal_length':[],'petal_width':[]}}    
        
list_dfspecies=iris.target.tolist()     
for i in range(len(list_dfspecies)):
    #(list_dfspecies[i])
    if list_dfspecies[i]==0:
        
        iris_realsp_dict['s0']['sepal_length'].append(df['sepal_length'][i])
        iris_realsp_dict['s0']['sepal_width'].append(df['sepal_width'][i])
        iris_realsp_dict['s0']['petal_length'].append(df['petal_length'][i])
        iris_realsp_dict['s0']['petal_width'].append(df['petal_width'][i])        


    elif int(list_dfspecies[i])==1:

        iris_realsp_dict['s1']['sepal_length'].append(df['sepal_length'][i])
        iris_realsp_dict['s1']['sepal_width'].append(df['sepal_width'][i])
        iris_realsp_dict['s1']['petal_length'].append(df['petal_length'][i])
        iris_realsp_dict['s1']['petal_width'].append(df['petal_width'][i]) 
    else:

        iris_realsp_dict['s2']['sepal_length'].append(df['sepal_length'][i])
        iris_realsp_dict['s2']['sepal_width'].append(df['sepal_width'][i])
        iris_realsp_dict['s2']['petal_length'].append(df['petal_length'][i])
        iris_realsp_dict['s2']['petal_width'].append(df['petal_width'][i]) 
        
###畫圖時間

        ## https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 16

fig=plt.figure(figsize=(20,20))
fig.subplots_adjust(hspace=0.1, wspace=0.1) # 調整圖形間距
ax = fig.add_subplot(221, projection='3d')  # 這邊更改為add_subplot   原有的subplot無法支援scatter markersize

ax.scatter(iris_realsp_dict['s1']['sepal_width'],\
                 iris_realsp_dict['s1']['petal_length'], \
                 iris_realsp_dict['s1']['petal_width'],\
     s=200*(np.array(iris_realsp_dict['s1']['sepal_length'])-4),c="blue",\
     marker=">",alpha=0.5,label="iris versicolor")

ax.scatter(iris_realsp_dict['s2']['sepal_width'],\
                 iris_realsp_dict['s2']['petal_length'], \
                 iris_realsp_dict['s2']['petal_width'],\
     s=200*(np.array(iris_realsp_dict['s2']['sepal_length'])-4),c="red",\
     marker=">",alpha=0.5,label="iris virginica")
ax.scatter(iris_realsp_dict['s0']['sepal_width'],\
                 iris_realsp_dict['s0']['petal_length'], \
                 iris_realsp_dict['s0']['petal_width'],\
     s=200*(np.array(iris_realsp_dict['s0']['sepal_length'])-4),c="green",\
     marker=">",alpha=0.5,label="iris setosa")
ax.set_xlabel("sepal width (cm)")
ax.set_ylabel("petal length (cm)")
ax.set_zlabel("petal width (cm)")
ax.set_xlim(2,4.5)
ax.set_ylim(1,7)
ax.set_zlim(0,2.5)
ax.yaxis.labelpad=30 #label相對位置調整
ax.zaxis.labelpad=30
ax.xaxis.labelpad=30
ax.legend()
#ax.title("Real Classification")
#scatters.legend(("iris setosa","iris setosa2","iris setosa3"))
#txt="點的大小與sepal length成正相關"
#plt.figtext(0.5, 0.10, txt, wrap=True, horizontalalignment='center', fontsize=16)


ax_predict = fig.add_subplot(224, projection='3d')
ax_predict.scatter(iris_dict_4group['g1']['sepal_width'],\
                 iris_dict_4group['g1']['petal_length'], \
                 iris_dict_4group['g1']['petal_width'],\
     s=200*(np.array(iris_dict_4group['g1']['sepal_length'])-4),c="blue",\
     marker=">",alpha=0.5,label="group 2")

ax_predict.scatter(iris_dict_4group['g2']['sepal_width'],\
                 iris_dict_4group['g2']['petal_length'], \
                 iris_dict_4group['g2']['petal_width'],\
     s=200*(np.array(iris_dict_4group['g2']['sepal_length'])-4),c="red",\
     marker=">",alpha=0.5,label="group 3")
ax_predict.scatter(iris_dict_4group['g0']['sepal_width'],\
                 iris_dict_4group['g0']['petal_length'], \
                 iris_dict_4group['g0']['petal_width'],\
     s=200*(np.array(iris_dict_4group['g0']['sepal_length'])-4),c="green",\
     marker=">",alpha=0.5,label="group 1")
ax_predict.scatter(iris_dict_4group['g3']['sepal_width'],\
                 iris_dict_4group['g3']['petal_length'], \
                 iris_dict_4group['g3']['petal_width'],\
     s=200*(np.array(iris_dict_4group['g3']['sepal_length'])-4),c="purple",\
     marker=">",alpha=0.5,label="group 4")
ax_predict.set_xlabel("sepal width (cm)")
ax_predict.set_ylabel("petal length (cm)")
ax_predict.set_zlabel("petal width (cm)")
ax_predict.set_xlim(2,4.5)
ax_predict.set_ylim(1,7)
ax_predict.set_zlim(0,2.5)
ax_predict.yaxis.labelpad=10 #label相對位置調整
ax_predict.zaxis.labelpad=20
ax_predict.xaxis.labelpad=10
ax_predict.legend()



ax_predict = fig.add_subplot(222, projection='3d')
ax_predict.scatter(iris_dict_3group['g1']['sepal_width'],\
                 iris_dict_3group['g1']['petal_length'], \
                 iris_dict_3group['g1']['petal_width'],\
     s=200*(np.array(iris_dict_3group['g1']['sepal_length'])-4),c="blue",\
     marker=">",alpha=0.5,label="group 2")

ax_predict.scatter(iris_dict_3group['g2']['sepal_width'],\
                 iris_dict_3group['g2']['petal_length'], \
                 iris_dict_3group['g2']['petal_width'],\
     s=200*(np.array(iris_dict_3group['g2']['sepal_length'])-4),c="red",\
     marker=">",alpha=0.5,label="group 3")
ax_predict.scatter(iris_dict_3group['g0']['sepal_width'],\
                 iris_dict_3group['g0']['petal_length'], \
                 iris_dict_3group['g0']['petal_width'],\
     s=200*(np.array(iris_dict_3group['g0']['sepal_length'])-4),c="green",\
     marker=">",alpha=0.5,label="group 1")

ax_predict.set_xlabel("sepal width (cm)")
ax_predict.set_ylabel("petal length (cm)")
ax_predict.set_zlabel("petal width (cm)")
ax_predict.set_xlim(2,4.5)
ax_predict.set_ylim(1,7)
ax_predict.set_zlim(0,2.5)
ax_predict.yaxis.labelpad=30 #label相對位置調整
ax_predict.zaxis.labelpad=20
ax_predict.xaxis.labelpad=30
ax_predict.legend()













"""

ax_mix = fig.add_subplot(225, projection='3d')    


ax_mix.scatter(iris_realsp_dict['s1']['sepal_width'],\
                 iris_realsp_dict['s1']['petal_length'], \
                 iris_realsp_dict['s1']['petal_width'],\
     s=200*(np.array(iris_realsp_dict['s1']['sepal_length'])-4),c="green",\
     marker="*",alpha=0.3,label="iris versicolor")

ax_mix.scatter(iris_realsp_dict['s2']['sepal_width'],\
                 iris_realsp_dict['s2']['petal_length'], \
                 iris_realsp_dict['s2']['petal_width'],\
     s=200*(np.array(iris_realsp_dict['s2']['sepal_length'])-4),c="green",\
     marker="p",alpha=0.3,label="iris virginica")
ax_mix.scatter(iris_realsp_dict['s0']['sepal_width'],\
                 iris_realsp_dict['s0']['petal_length'], \
                 iris_realsp_dict['s0']['petal_width'],\
     s=200*(np.array(iris_realsp_dict['s0']['sepal_length'])-4),c="green",\
     marker="P",alpha=0.3,label="iris setosa")
ax_mix.scatter(iris_dict_4group['g1']['sepal_width'],\
                 iris_dict_4group['g1']['petal_length'], \
                 iris_dict_4group['g1']['petal_width'],\
     s=200*(np.array(iris_dict_4group['g1']['sepal_length'])-4),c="purple",\
     marker=">",alpha=0.3,label="group 2")

ax_mix.scatter(iris_dict_4group['g2']['sepal_width'],\
                 iris_dict_4group['g2']['petal_length'], \
                 iris_dict_4group['g2']['petal_width'],\
     s=200*(np.array(iris_dict_4group['g2']['sepal_length'])-4),c="purple",\
     marker="<",alpha=0.3,label="group 3")
ax_mix.scatter(iris_dict_4group['g0']['sepal_width'],\
                 iris_dict_4group['g0']['petal_length'], \
                 iris_dict_4group['g0']['petal_width'],\
     s=200*(np.array(iris_dict_4group['g0']['sepal_length'])-4),c="purple",\
     marker="^",alpha=0.3,label="group 1")
ax_mix.scatter(iris_dict_4group['g3']['sepal_width'],\
                 iris_dict_4group['g3']['petal_length'], \
                 iris_dict_4group['g3']['petal_width'],\
     s=200*(np.array(iris_dict_4group['g3']['sepal_length'])-4),c="purple",\
     marker="v",alpha=0.3,label="group 4")
ax_mix.set_xlabel("sepal width (cm)")
ax_mix.set_ylabel("petal length (cm)")
ax_mix.set_zlabel("petal width (cm)")
ax_mix.set_xlim(2,4.5)
ax_mix.set_ylim(1,7)
ax_mix.set_zlim(0,2.5)
ax_mix.yaxis.labelpad=30 #label相對位置調整
ax_mix.zaxis.labelpad=30

ax_mix.xaxis.labelpad=10
ax_mix.legend()

"""
ax_diff = fig.add_subplot(223, projection='3d') 

ax_diff.scatter(iris_dict_diffgroup['sepal_width'],\
                 iris_dict_diffgroup['petal_length'], \
                 iris_dict_diffgroup['petal_width'],\
     s=200*(np.array(iris_dict_diffgroup['sepal_length'])-4),c="green",\
     marker="*",alpha=0.3,label="與真實物種分類結果不同的點")   
ax_diff.set_xlabel("sepal width (cm)")
ax_diff.set_ylabel("petal length (cm)")
ax_diff.set_zlabel("petal width (cm)")
ax_diff.set_xlim(2,4.5)
ax_diff.set_ylim(1,7)
ax_diff.set_zlim(0,2.5)
ax_diff.yaxis.labelpad=30 #label相對位置調整
ax_diff.zaxis.labelpad=30

ax_diff.xaxis.labelpad=10
ax_diff.legend()
plt.show()