import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import f_regression
import urllib
import random
import pandas

url = 'C:\Users\U803802\Upload\codes\RevenueByyears.csv'
dataset= pandas.read_csv(url,  sep=',')


cols = ['PARTNERNUMMER','REVENUE2009','REVENUE2010','REVENUE2011','REVENUE2012','REVENUE2013','REVENUE2014','REVENUE2015','REVENUE2016']

dt=dataset[cols]
np.all(np.isfinite(dt))


np.any(np.isnan(dt))


dt=dt.fillna(method='bfill',axis='columns')
dt=dt.fillna(method='pad',axis='columns')


dt['Indexed2011']=dt['REVENUE2011']/dt['REVENUE2010']
dt['Indexed2012']=dt['REVENUE2012']/dt['REVENUE2010']
dt['Indexed2013']=dt['REVENUE2013']/dt['REVENUE2010']
dt['Indexed2014']=dt['REVENUE2014']/dt['REVENUE2010']
dt['Indexed2015']=dt['REVENUE2015']/dt['REVENUE2010']
dt['Indexed2016']=dt['REVENUE2016']/dt['REVENUE2010']


dt.to_csv('C:\Users\U803802\Upload\codes\imputed_Revenues_1.csv')
