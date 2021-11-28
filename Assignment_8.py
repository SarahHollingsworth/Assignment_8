#!/usr/bin/env python
# coding: utf-8

# In[173]:


import pandas as pd
homegames_df = pd.read_csv('https://raw.githubusercontent.com/frankData612/data_612/master/baseballdatabank-master/core/HomeGames.csv')
parks_df = pd.read_csv('https://raw.githubusercontent.com/frankData612/data_612/master/baseballdatabank-master/core/Parks.csv')
combined_df = homegames_df.merge(parks_df, left_on='park.key', right_on='park.key')
combined_df = combined_df.fillna(method='ffill')
combined_df = combined_df.fillna(method='bfill')

combined_df.rename({'year.key':'year', 'league.key':'league', 'team.key':'team', 'park.key':'park_key', 
                    'span.first':'span_first','span.last':'span_last', 'games':'games', 'openings':'openings',
                    'attendance':'attendance', 'park.name':'park_name', 'park.alias':'park_alias', 'city':'city', 
                    'state':'state', 'country':'country'}, axis='columns', errors='raise', inplace=True)

def summarize_data(x):
    return (pd.Series({
            'avg_games': x.games.mean(),
            'min_games': x.games.min(),
            'max_games': x.games.max(),
            'std_dev_games': x.games.std(),
            '1st_quartile': x.games.quantile(q=0.25),
            '2nd_quartile': x.games.quantile(q=0.50),
            '3rd_quartile': x.games.quantile(q=0.75),
            'sample_count': len(x),
            'proportion': x.games.count()/combined_df.games.count()
        }))

combined_df.groupby('league').apply(summarize_data)


# In[172]:


def summarize_data(x):
    return (pd.Series({
            'sample_count': x.park_name.count(),
            'park_name (first alpha)': x.park_name.min(),
            'park_name (last alpha)': x.park_name.max(),       
            'proportion': x.league.count()/combined_df.league.count()
        }))

combined_df.groupby('league').apply(summarize_data)

