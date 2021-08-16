# f). Generate the report for job and career satisfaction of developer based on their gender and continent?

data1['JobSat'].value_counts()
data1['JobSat']=data1['JobSat'].map({'Slight satisfied': 5,'Very satisfied':4,'Slight dissatisfied':2 ,'Neither satisfied nor dissatisfied':1})

plt.figure(figsize=(12,7))
sns.barplot(x = 'Gender', y='JobSat', hue='Contient', data= data1)
plt.grid()
N=3
ind=np.arange(N)
s=(data1['Gender'].value_counts().index)
plt.xticks(ind, s, rotation='vertical', fontsize=15)
plt.show()
plt.show()

