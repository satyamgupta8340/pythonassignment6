#e). What is the distribution of people who code as a hobby based on gender and continent (hint: use your mapping of country to continent)?

data1['Gender'].unique()
df=data1[data1['Hobbyist']=='Yes']
data1['Hobbyist']=data1['Hobbyist'].map({'Yes':1,'No':0})
data1['Gender'].value_counts()


l = []
for i in data1[ 'Gender']:
    if i != 'Man' and i != 'Woman':
        l.append('others')
    else:
        l.append(i)


	data1['Gender'] = l

data1['Gender'].value_counts()

plt.figure(figsize=(12,7))
sns.barplot (x = 'Gender', y='Hobbyist', hue='Contient', data=data1)
plt.grid()
N=3
ind=np.arange(N)
s=(data1['Gender'].value_counts().index)
plt.xticks(ind, s, rotation="vertical", fontsize=15)
plt.show()
plt.show()
