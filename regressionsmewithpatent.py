import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import f_regression
import urllib
import random
import pandas

url = 'C:\Users\U803802\Upload\Neuer Ordner\title.xls'
dataset= pandas.read_csv(url, sep=',')

train,test = train_test_split(dataset,test_size=0.30)

cols = ['REVENUE2008','REVENUE2009','REVENUE2010','REVENUE2011','REVENUE2012','REVENUE2013','REVENUE2014','REVENUE2015']

regr= linear_model.LinearRegression()
regr.fit(train[cols],train['REVENUE2016'])

print(regr.coef_)
pred_revenue=regr.predict(test[cols])
rmse = (regr.predict(test[cols]) - test['REVENUE2016'])**2
print rmse

plt.scatter(test['REVENUE2015'], test['REVENUE2016'], color='black')
plt.plot(test['REVENUE2015'],regr.predict(test[cols]), color='blue')


cols1= ['REVENUE2015']
regr1= linear_model.LinearRegression()
regr1.fit(train[cols1],train['REVENUE2016'])
print(regr1.coef_)
pred_revenue=regr1.predict(test[cols])
rmse1 = (regr1.predict(test[cols1]) - test['REVENUE2016'])**2

plt.scatter(test['REVENUE2015'], test['REVENUE2016'], color='black')
plt.plot(test['REVENUE2015'],regr1.predict(test[cols1]), color='blue')
plt.show()





url2 = 'C:\Users\U803802\Upload\sql pratiksha\SMEwithPatentrevenuebyyearwithPatentcnt.csv'
dataset2= pandas.read_csv(url2, sep=';')

train2,test2 = train_test_split(dataset2,test_size=0.30)

cols2 = ['REVENUE2010','REVENUE2011','REVENUE2012','REVENUE2013','REVENUE2014','REVENUE2015','PATENT_COUNT']

regr2= linear_model.LinearRegression()
regr2.fit(train2[cols2],train2['REVENUE2016'])

print(regr2.coef_)
pred_revenue2=regr2.predict(test2[cols2])
rmse2 = (regr2.predict(test2[cols2]) - test2['REVENUE2016'])**2
print rmse2

plt.scatter(test2['PATENT_COUNT'], test2['REVENUE2016'], color='black')
plt.plot(test2['PATENT_COUNT'],regr2.predict(test2[cols2]), color='blue')


cols3= ['PATENT_COUNT']
regr3= linear_model.LinearRegression()
regr3.fit(train2[cols3],train2['REVENUE2016'])
print(regr3.coef_)
pred_revenue=regr3.predict(test2[cols3])
rmse3 = (regr3.predict(test2[cols3]) - test2['REVENUE2016'])**2

plt.scatter(test['REVENUE2015'], test['REVENUE2016'], color='black')
plt.plot(test['REVENUE2015'],regr1.predict(test[cols1]), color='blue')
plt.show()


regr.score(test[cols],test['REVENUE2016'])  #all years as features  0.88646462093721201
regr1.score(test[cols1],test['REVENUE2016'])  #2015 #  as features  0.99423619593167589
regr2.score(test2[cols2],test2['REVENUE2016']) #all years as features plus patent count as 0.97728510304687677
regr3.score(test2[cols3],test2['REVENUE201df16'])  #patent count as sole features -0.031462271421622168


cols4= ['PATENT_COUNT','REVENUE2015']
regr4= linear_model.LinearRegression()
regr4.fit(train2[cols4],train2['REVENUE2016'])
print(regr4.coef_)
pred_revenue=regr3.predict(test2[cols3])
rmse4 = (regr4.predict(test2[cols4]) - test2['REVENUE2016'])**2
regr4.score(test2[cols4],test2['REVENUE2016'])    #0.97969331670838011

cat= pandas.get_dummies(dataset2['A_BETR_ART'])




url = 'C:\Users\U803802\Upload\pratiksha\regression\companies_without_patents.csv'


np.any(np.isnan(df1))
np.all(np.isfinite(df1))


#fill null values
df1=df1.fillna(method='bfill',axis='columns')
df1=df1.fillna(method='pad',axis='columns')
