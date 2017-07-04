data= pd.read_csv('C:\Users\U803802\Upload\sql pratiksha\smewithouttorublewithindustry.csv',header=None, sep=',',
                 names=['PARTNERNUMMER','APPLICANTS','YEAR','REVENUE','INDUSTRYTYPE'])

wordcount= vect.fit_transform(data[['INDUSTRYTYPE']])

