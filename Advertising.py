import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso, Ridge
# 交叉验证
from sklearn.model_selection import GridSearchCV

if __name__ == "__main__":
    data = pd.read_csv('Advertising.csv')
    x = data[['TV', 'Radio', 'Newspaper']]
    # 待预测的值
    y = data['Sales']
    # 建模: 训练数据 + 测试数据
    # 伪随机数，需要seed, random_state = seed = 1 从1开始取
    # train_size 训练数据的比例是0.75
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, train_size=0.75)
    model = Lasso()
    # model = Ridge()
    alpha_can = np.logspace(-3, 2, 10)
    # 不使用科学计数法，默认是False
    np.set_printoptions(suppress=True)
    # 5折验证
    lasso_model = GridSearchCV(model, param_grid={'alpha': alpha_can},cv=5)
    lasso_model.fit(x_train, y_train)
    # 超参数：lasso_model.best_params_

    # 按照真实的数据进行排序，按照y的测试数据做递增, argsort 第几个在哪一位
    order = y_test.argsort(axis=0)
    y_test = y_test.values[order]
    # 对应将x也进行排序
    x_test = x_test.values[order, :]
    # 在测试数据上看训练好的结果
    y_hat = lasso_model.predict(x_test)
    # R^2
    print(lasso_model.score(x_test, y_test))
    mse = np.average((y_hat-np.array(y_test))**2)
    rmse = np.sqrt(mse)

    t = np.arange(len(x_test))
    mpl.rcParams['font.sans-serif'] = [u'simHei']
