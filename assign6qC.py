# C). Generate a report for the average salary of developer based on continent.

import pycountry_convert as pc

def country_to_continent (country_name):
    if country_name != 'Other Country (Not Listed Above)':
         # print (country_name)
        try:
            country_alpha2 = pc.country_name_to_country_alpha2 (country_name) 
            country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2) 
            country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
            return country_continent_name
        except:
            return "unknown"
    else:
            return "unknown"

	    names=[country_to_continent(i) for i in data1['Country']]
data1['Contient']=names
data1['Contient']
salary_notnull=data1[data1['ConvertedComp'].notnull()]
a=salary_notnull.groupby(['Contient'])['ConvertedComp'].mean().sort_values(ascending=False)
a.index


plt.figure(figsize=(16,9))
plt.title('Salary countplot based on Continent',fontsize=20, fontweight='bold', y=1.05,)
plt.ylabel('Salary', fontsize=15)
plt.xlabel('Continent', fontsize=15)
a.plot(kind='bar')
