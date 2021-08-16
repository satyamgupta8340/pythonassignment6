# b). Deduce the percentage of developers who know python in each country.


data1['Country'].nunique()
languages=data1[data1['LanguageWorkedWith'].notnull()]
languages.head()
countries=languages['Country'].unique()
country_python={}
languages.groupby(['Country'])['LanguageWorkedWith'].value_counts()

for country in countries:
    for i in lang.groupby(['Country'])['LanguageWorkedWith'].value_counts()[country].index:
        l=[]
        l.append(i.split(';'))
        for j in l:
            if 'Python' in j:
                if country not in country_python.keys():
                    country_python[country]=1
                else:
                    country_python[country]+=1


country_python


def plot_dimension_count(unique_dim_dict,plot_title):
    dim_count=pd.DataFrame.from_dict(unique_dim_dict,orient='index',dtype=None)
    dim_count.columns=['Count']
    dim_count.sort_values('Count',ascending=False,inplace=True)
    
    dim_count[:10].plot(kind='pie',figsize=(12,12),fontsize=10,title=plot_title,subplots=True,autopct='%1.1f%%');
    print(dim_count[:10])


    plot_dimension_count(country_python,'The Most popular languages')
    