import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from numpy import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
 
#data = np.loadtxt('kmeans.txt')
data=np.random.randint(0,100,size=[100,3])
k=7
estimator = KMeans(n_clusters=k)
estimator.fit(data)
label_pred = estimator.labels_
 
Color = 'rbgyckm'

fig = plt.figure(figsize=(7, 7))#1, figsize=(7, 6))
plt.clf()
ax = Axes3D(fig)
ax.view_init(30, 22)#让图像上下旋转、左右旋转。可以是负数。
for i in range(k):
    clusterData = data[label_pred == i]
    #plt.scatter(clusterData[:,0],clusterData[:,1],color=Color[i])
    
    ax.scatter(clusterData[:,0],clusterData[:,1],clusterData[:,2], c=Color[i])   
    
plt.show()