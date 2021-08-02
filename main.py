from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('test_5.csv', index_col=0)
# X = df.values.tolist()
# X = np.array(X)
pca = PCA(n_components=2)
new_pca = pd.DataFrame(pca.fit_transform(df))
Y = new_pca.values.tolist()
Y = np.array(Y)


# 绘制数据分布图
estimator = KMeans(n_clusters=5)#构造聚类器
estimator.fit(Y)#聚类
label_pred = estimator.labels_ #获取聚类标签
#绘制k-means结果
x0 = Y[label_pred == 0]
x1 = Y[label_pred == 1]
x2 = Y[label_pred == 2]
x3 = Y[label_pred == 3]
x4 = Y[label_pred == 4]
plt.scatter(x0[:, 0], x0[:, 1], c = "red", marker='*', label='label0')
plt.scatter(x1[:, 0], x1[:, 1], c = "green", marker='*', label='label1')
plt.scatter(x2[:, 0], x2[:, 1], c = "blue", marker='*', label='label2')
plt.scatter(x3[:, 0], x3[:, 1], c = "black", marker='*', label='label3')
plt.scatter(x4[:, 0], x4[:, 1], c = "yellow", marker='*', label='label4')
# # plt.scatter(x5[:, 0], x2[:, 5], c = "orange", marker='+', label='label2')
#
plt.xlabel('')
plt.ylabel('')
plt.legend(loc=2)
plt.show()
