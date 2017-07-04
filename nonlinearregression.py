import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import f_regression
import urllib
import random
import pandas
import scipy.optimize
from scipy.optimize import least_squares

def generate_data(x,t):
    return x[0] * np.exp(-x[1] * t) * np.sin(x[2] * t)



def fun(x, t, y):
    return (x[0] * np.exp(-x[1] * t) * np.sin(x[2] * t)) - y


x0 = np.ones(3)


train,test = train_test_split(df1,test_size=0.30)
res_lsq = least_squares(fun, x0, args=(train['PATENT_COUNT'], train['CAGR']))
res_robust = least_squares(fun, x0, loss='soft_l1', f_scale=0.1, args=(train['PATENT_COUNT'], train['CAGR']))



y_lsq = generate_data(res_lsq.x, test['PATENT_COUNT'])
y_robust= generate_data(res_robust.x, test['PATENT_COUNT'])


plt.scatter(test['PATENT_COUNT'],test['CAGR'],label='true')
plt.plot(test['PATENT_COUNT'],y_lsq,label='lsq')
plt.plot(test['PATENT_COUNT'],y_robust,label='robust')


popt, pcov = scipy.optimize.curve_fit(generate_data, train['PATENT_COUNT'], train['CAGR'])



xp = np.linspace(-2, 6, 100)

##polyfit

p6 = np.poly1d(np.polyfit(df1['PATENT_COUNT'], df1['CAGR'], 6))

plt.plot(df1['PATENT_COUNT'], df1['CAGR'],'.',xp,p6(xp),'-',xp,p15(xp),'--')

plt.plot(test['PATENT_COUNT'],test['CAGR'],'.',xp,y_lsq,'-',xp,y_robust,'--')


df2=df1['CAGR']
qd=df2.quantile([low, high])
df1=df1[df1['CAGR']<.222261]
df1=df1[df1['CAGR']>-.211719]
df1=df1[df1['PATENT_COUNT']<15]

