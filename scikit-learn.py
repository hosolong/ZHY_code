import numpy as np
import matplotlib.pyplot as plt
#from sklearn.datasets import make_gaussian_quantiles
from sklearn.mixture import GaussianMixture

#生成2维正态分布，生成的数据300个样本
X1 = np.random.multivariate_normal([3, 1], [[1, -0.5], [-0.5, 1]], size=300)
X2 = np.random.multivariate_normal([8, 10], [[2, 0.8], [0.8, 2]], size=300)
X3 = np.random.multivariate_normal([12, 2], [[1, 0], [0, 1]], size=300)
X = np.vstack((X1, X2))
X = np.vstack((X, X3))
X1, Y1 = np.split(X, 2, axis=1)
plt.scatter(X1, Y1)

#高斯混合
models = [GaussianMixture(n_components=i, random_state=0, covariance_type='full').fit(X) for i in range(1, 21)]
aic = [m.aic(X) for m in models]
bic = [m.bic(X) for m in models]
plt.figure(figsize=(10, 10))
plt.plot(range(1, 21), aic, label='AIC')
plt.plot(range(1, 21), bic, label='BIC')
plt.legend(loc='upper right')  # 图例在右上角
plt.title("GMM's AIC and BIC")
plt.show()

gm = GaussianMixture(n_components=3, random_state=0).fit(X)
print(gm.means_, gm.covariances_)