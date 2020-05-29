# 求素数

import math
from datetime import time


def is_prime(x):
    return 0 not in [x % i for i in range(2, int(math.sqrt(x)) + 1)]


def is_prime3(x):
    flag = True
    p = []
    for num in p:
        if num > math.sqrt(x):
            break
        if x % num == 0:
            flag = True
            break
    if flag:
        p.append(x)
    return p


def method1(a, b):
    t = time()
    p = [p for p in range(a, b) if 0 not in [p % d for d in range(2, int(math.sqrt(p)) + 1)]]
    return p


# fliter
def method2(a, b):
    t = time()
    p = filter(is_prime, range(a, b))
    return p


# fliter and lambda
def method3(a, b):
    t = time()
    # 匿名函数
    is_prime2 = (lambda x: 0 not in [x % i for i in range(a, int(math.sqrt(x)) + 1)])
    p = filter(is_prime2, range(a, b))
    return p


# definition
def method4(a, b):
    t = time()
    p = []
    for i in range(a, b):
        flag = True
        for num in p:
            if num > math.sqrt(i):
                break
            if i % num == 0:
                flag = True
                break
        if flag:
            p.append(i)
    return p


# definition and fliter
def method5(a, b):
    t = time()
    p = []
    filter(is_prime3, range(a, b))
    return p


if __name__ == '__main__':
    a = 2
    b = 100000
