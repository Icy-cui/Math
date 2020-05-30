import numpy as np
# 可以直接调用待交叉验证的版本 CV
from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV, ElasticNetCV
# 预处理
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.pipeline import Pipeline
# 强制不要报出 warning
from sklearn.exceptions import ConvergenceWarning

if __name__ == "__main__":
    warnings.fliterwarnings(actions='ignore', category=ConvergenceWarning)
    np.random.seed(0)
    # 为了输出：不要每80个就换行
    np.set_printoptions(linewidth=300)
    N = 9
    # 添加一点噪声
    x = np.linspace(0, 6, N) + np.random.random(N)
    x = np.sort(x)
    y = x ** 2 - 4 * x - 3 + np.random.random(N)
    x.shape = -1, 1
    y.shape = -1, 1

    # 最关键的部分
    models = [Pipeline([
        ('ploy', PolynomialFeatures()),
        ('linear', LinearRegression(fit_intercept=False))]),
        Pipeline([
            ('ploy', PolynomialFeatures()),
            ('linear', RidgeCV(alphas=np.logspace(-3, 2, 50), fit_intercept=False))]),
        Pipeline([
            ('ploy', PolynomialFeatures()),
            ('linear', ElasticNetCV(alphas=np.logspace(-3, 2, 50), l1_ratio=[.1, .5, .7, .9, .95, .99, 1],
                                    fit_intercept=False))])
    ]
    mpl.rcParams['font.sans-serif'] = [u'simHei']
    mpl.rcParams['axes.unicode_minus'] = False
    np.set_printoptions(suppress=False)

    plt.figure(figsize=(18, 12), facecolor='w')
    d_pool = np.arange(1, N, 1)  # 阶
    m = d_pool.size
    colors = []
    for c in np.linspace(16711680, 255, m):
        colors.append('#%06x' % c)
    line_width = np.linspace(5, 2, m)
    rss_list = []
    tss_list = []
    ess_list = []
    ess_rss_list = []
    for t in range(4):
        model = models[t]
        plt.subplot(2, 2, t + 1)
        plt.plot(x, y, 'ro', ms=10, zorder=N)
        for i, d in enumerate(d_pool):
            model.set_params(poly__degree=d)
            # ravel 拉成直线
            model.fit(x, y.ravel())
            # 获得线
            lin = model.get_params('linear')['linear']
            output = u'%s:%d'
