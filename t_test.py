
import pandas
from scipy import stats
url1 = 'C:\Users\U803802\Upload\pratiksha\Revenue\cagrpatentnopatentgrowing'
url2 = 'C:\Users\U803802\Upload\pratiksha\Revenue\cagr_without_patents.csv'

dataset1= pandas.read_csv(url1, sep=';')
dataset2= pandas.read_csv(url2, sep=';')

a=dataset1['REVENUE2016']
b=dataset2['REVENUE2016']


t,p=stats.ttest_ind(a, b)
print t
print p




url2= 'C:\Users\U803802\Upload\pratiksha\Gender\Female.csv'