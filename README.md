# 勞動部勞動力發展署雲嘉南分署 雲端運算Python與數位媒體行銷班 (伽碩企業有限公司代辦)
# Table of contents
1. [概述](#概述)
2. [專案說明](#專案說明)</br>
    a. [波士頓](#波士頓)</br>
    b. [鳶尾花](#鳶尾花)</br>


雲端運算Python與數位媒體行銷班  課程所製作的code

# 概述
此儲藏庫為勞動部勞動力發展署雲嘉南分署舉辦、伽碩企業協辦之111年雲端運算Python與數位媒體行銷班之python專題結果。
此結果儲藏的是
1.code
2.程式執行結果
3.報告總結之投影片

This repository is the results of the python project of 2022 class for python cloud computing and digital media marketing, which was handle by <b>Yunlin-Chiayi-Tainan Regional Branch</b> of <b>Workforcedevelopment Agency, Minstry of Labor </b> and <b>jiashuo Co., Ltd</b>.
The content of this repository include:
1. code
2. result of program
3. Summary of project (ppt)

# 專案說明
本專案是使用sklearn模組所附帶之鳶尾花與波士頓資料集來進行分析
This project is to use the Iris and Boston datasets from the sklearn model for analysis

## 波士頓
依據老師指示，取RM: 每棟住宅的房間數、LSTAT: 地區中有多少房東是屬於低收入戶族群、NOx: 氮氧化物(10ppm)、CHAS:在查爾斯河畔與否與MEDV:房價中位數等這五個因子來進行3D圖繪製
其中在查爾斯河畔與否分別用紅藍點標示
房價中位數則是用點的大小呈現
剩下的則分別繪製於XYZ三軸

note:此資料集共506筆資料

According to the teacher's instructions, take 5 factors to draw 3D graphs: 
1. RM: the number of rooms in each house
2. LSTAT: how many landlords in the area belong to the low-income household group
3. NOx: nitrogen oxides (10ppm)
4. CHAS: whether it is near the Charles River or not
5. MEDV: the median of house price Count
Among them, whether on the side of the Charles River or not are marked with red and blue dots respectively
The median house price is represented by the size of the dot
The rest are drawn on the XYZ axes respectively

note: This dataset contains 506 records.

![BOSTON](result/波士頓房價與因子散佈圖(scatter).png "波士頓房價與因子散佈圖(scatter)")


## 鳶尾花
資料集內有五個資訊：
1. 花萼長
2. 花萼寬
3. 花瓣長
4. 花瓣寬
5. 實際物種分類(<I>Iris Setosa</I>、<I>Iris Versicolour</I>、<I>Iris Virginica</I>)
共150筆資料

在本分析中，首先使用Kmean cluster分群法將資料分成3群與4群(分別對應3個物種與4個特徵)
然後繪製成3D圖，其中群/物種用顏色區分、花萼長用點的大小來辨別、剩下的則是分別繪製成XYZ軸
此外依據分類的結果不同，分別會有
1. 真實物種分布
2. Kmean cluster result (3 group)
3. 真實物種與分成3群的比較結果
4. Kmean cluster result (4 group)


There are five factor of information in the data set:
1. Sepal length
2. Sepal width
3. Petal length
4. Petal width
5. Species 
Total 150 records

In this analysis, the Kmean clustering method to divide the data into 3 groups and 4 groups (corresponding to 3 species and 4 characteristics respectively) at first.
Then it is drawn into a 3D map, in which the group/species are distinguished by color, the length of the sepal is distinguished by the size of the dot, and the rest are drawn on the XYZ axis respectively
In addition, depending on the classification results, there will be
1. Species Distribution
2. Kmean cluster result (3 group)
3. Comparison results of real species and grouping into 3 groups
4. Kmean cluster result (4 group)

![IRIS subplot](result/鳶尾花物種分群(subplog).png "鳶尾花物種分群(subplog)")
