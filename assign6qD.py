# D). Based on this survey, what will be the most desired programming language forthe year 2020?

language_desired = data1[data1['LanguageDesireNextYear'].notnull()]
unique_lang={}
unique_lang

def plot_dimension_count (unique_dim_dict, plot_title):
    dim_count = pd.DataFrame.from_dict(unique_dim_dict, orient='index', dtype=None)
    dim_count.columns= ['Count']
    dim_count.sort_values('Count', ascending=True, inplace=True)
    dim_count.plot(kind = 'barh', figsize = (12,12), fontsize = 10, title =plot_title,color='c');

    plot_dimension_count(unique_lang, 'The Most Popular Languages')

    