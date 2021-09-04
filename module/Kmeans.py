#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# # 라이브러리
from yellowbrick.cluster import KElbowVisualizer
from sklearn.cluster import KMeans
from sklearn import cluster
import pandas as pd
import warnings
warnings.filterwarnings(action='ignore')

### 전역변수 선언 ###
global data
data = None
global df
df = None
global X
X = None
global k
k = None
global centroids
centroids = None
#####################

############## mainFunction ##########################
def mainFunction(getInputData):
    global data
    data = getInputData

    # initial setting #
    # df setting
    global df
    df = pd.json_normalize(data["data"])
    #위경도
    df.rename(columns = {'location.latitude' : 'latitude'}, inplace = True)
    df.rename(columns = {'location.longitude' : 'longitude'}, inplace = True)
    # X setting
    global X
    X = df[["latitude", "longitude"]]
    # k setting
    global k
    k = elbow(X)
    # Add df ['labels'] && centroids setting
    global centroids
    df, centroids = Kmeans(k)

    ###### 최종값 return #####
    return createDataList()
########################################################

### k값 설정 ###
def elbow(location):
    model = KElbowVisualizer(KMeans(), k=10)
    model.fit(location)
    k = int(model.elbow_value_)
    return k

### Kmeans 수행 ###
def Kmeans(k):
    kmeans = cluster.KMeans(init = 'k-means++',n_clusters = k, n_init=10)
    kmeans.fit(X)
    cluster_labels = kmeans.labels_
    df['labels'] = cluster_labels
    centroids = kmeans.cluster_centers_
    return df, centroids


### create dataList (최종 return) ###
def createDataList(): 
    dataList=[i for i in range(k)]
    for i in range(k):
        dataList[i] = {}
        dataList[i]['id']= i
        dataList[i]['centroids'] = CentroidFunc(k)[i][0]
        dataList[i]['population'] = Population(k)[i]
        dataList[i]['resultData'] = resultData()[i]        
    return dataList

# centroids_list setting
def CentroidFunc(k):
    centroids_list=[i for i in range(k)]
    for i in range(k):
        centroids_list[i] = []
        centroids_list[i].append({'lat' : centroids[i][0], 'lon' : centroids[i][1]})
    
    return centroids_list

# population_list setting
def Population(k):
    _list=[]
    for i in range(k):
        population = len(df[df['labels']==i])
        _list.append(population)

    return _list

# resultData setting
def resultData():
    resultData = [i for i in range(k)]
    for i in range(k):
        resultData[i] = {}
    for i in range(k):
        for attr in data["orderSetting"].keys():
                resultData[i][attr] = {}
                j=0
                for orderIndex in data["orderSetting"][attr]:
                    resultData[i][attr][orderIndex] = orderSetting(attr)[i][j]
                    j+=1
    return resultData

### 주문에 따라서 어떤 함수를 실행할지 설정 ###
def orderSetting(attr):
    # 칼럼명 변경
    df.rename(columns = {'detailInfo.'+attr : attr}, inplace = True)
    
    # 변경한 칼럼명으로 데이터프레임 그룹화(counting)
    group = pd.DataFrame(df.groupby(['labels', attr]).size()).reset_index()

    returnList = [i for i in range(k)]
    for i in range(k):
        returnList[i] = []
        
    # count, sort, rsort
    for orderIndex in data["orderSetting"][attr]:
        
        if orderIndex == 'count':
            for i in range(k):
                returnList[i].append(CountFunc(group,k)[i][0])
        if orderIndex == 'sort':
            for i in range(k):
                returnList[i].append(SortFunc(group,k)[i][0])
        if orderIndex =='rsort':
            for i in range(k):
                returnList[i].append(RSortFunc(group,k)[i][0])
        if orderIndex == 'average':
            for i in range(k):
                returnList[i].append(AveFunc(group,k)[i][0])
    return returnList




##### order에 따른 데이터 가공 #####

def CountFunc(Group,k):
    _list=[i for i in range(k)]

    for i in range(k):
        _list[i] = []
        _dict={}
        _Group = Group[Group['labels'] == i].reset_index()

        data_0 = _Group[Group.columns[1]].tolist()
        data_1 = _Group[0].tolist()
        for j in range(len(_Group)):
            _dict[data_0[j]] = data_1[j]
        _list[i].append(_dict)

    return _list


def SortFunc(Group,k):
    _list=[i for i in range(k)]

    for i in range(k):
        _list[i] = []
        _Group = Group[Group['labels'] == i].reset_index()
        data_0 = _Group[Group.columns[1]].tolist()
        _list[i].append(data_0)

    return _list


def RSortFunc(Group,k):
    _list=[i for i in range(k)]

    for i in range(k):
        _list[i] = []
        _Group = Group[Group['labels'] == i].reset_index().sort_values('salary',ascending = False)      
        data_0 = _Group[Group.columns[1]].tolist()
        _list[i].append(data_0)

    return _list

    
def AveFunc(Group,k):
    _list=[i for i in range(k)]

    for i in range(k):
        _list[i] = []
        _Group = Group[Group['labels'] == i].reset_index()
        if len(_Group) != 0:
            ave = sum(_Group[Group.columns[1]])/len(_Group)
        else:
            ave = 0
        _list[i].append(ave)
        
    return _list


# ## JSON파일로 만들기 ##
# with open("./resultJSON.json", "w") as jsonFile:
#     json.dump(mainFunction(), jsonFile)

