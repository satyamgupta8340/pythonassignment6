# a).Find the average age of developers when they wrote their first line of code.

data1['Age1stCode']
data1['Age1stCode'].isnull().sum()
data1.shape
data1['Age1stCode'].unique()
mask = data1['Age1stCode'] =='Older than 85'
data1.loc[mask,('Age1stCode')] =86
mask = data1['Age1stCode'] =='Younger than 5 years'
data1.loc[mask,('Age1stCode')] =4
data1['Age1stCode'].isnull().sum()
data1['Age1stCode']=data1['Age1stCode'].astype('float')
data1['Age1stCode'].unique()
data1['Age1stCode'].dtype


import numpy as np
np.mean(data1['Age1stCode'])
plt.figure(figsize=(18,5))
sns.countplot(x='Age1stCode',data = data1,order = data1['Age1stCode'].value_counts().iloc[:20].index)
