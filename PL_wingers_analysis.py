

#!/usr/bin/env python
# coding: utf-8

# Premier League event data  - Winger Analysis
# In[1]:


import pandas as pd


# In[3]:


# season -15
pl_15 = pd.read_csv(r'G:\Fall 2020\Ireland\UCD\Modules\Summer\Sports Analytics\Research Project\Dataset\Tableau_Prep_Output\PL_15_Final.csv')


# In[4]:


#season -20
pl_20 = pd.read_csv(r'G:\Fall 2020\Ireland\UCD\Modules\Summer\Sports Analytics\Research Project\Dataset\Tableau_Prep_Output\PL_20_Final.csv')


# In[5]:


pl_15.columns


# In[6]:


pl_15['Big chances created'].fillna(0,inplace=True)


# In[7]:


pl_20['Big chances created'].fillna(0,inplace=True)


# In[8]:


pl_15['Big chances missed'].fillna(0,inplace=True)


# In[9]:


pl_20['Big chances missed'].fillna(0,inplace=True)


# In[10]:


#pl_15[['Big chances created','Big chances missed']]


# In[11]:


pl_20[['Big chances created','Big chances missed']]


# In[12]:


pl_15['Total Big chances'] = pl_15['Big chances created'] + pl_15['Big chances missed']


# In[13]:


pl_20['Total Big chances'] = pl_20['Big chances created'] + pl_20['Big chances missed']


# In[14]:


# to have only the parameters / metrics

#pl_15
pl_15['Through balls per match'] = pl_15['Through balls']/pl_15['Appearances']
pl_15['Shots  per match'] = pl_15['Shots']/pl_15['Appearances']
pl_15['Big chances created per match'] = pl_15['Big chances created']/pl_15['Appearances']
pl_15['Crosses per match'] = pl_15['Crosses']/pl_15['Appearances']
pl_15['Assists per match'] = pl_15['Assists']/pl_15['Appearances']
pl_15['Penalties scored per match'] = pl_15['Penalties scored']/pl_15['Appearances']
pl_15['Freekicks scored per match'] = pl_15['Freekicks scored']/pl_15['Appearances']
pl_15['Interceptions per match'] = pl_15['Interceptions']/pl_15['Appearances']
pl_15['Tackles per match'] = pl_15['Tackles']/pl_15['Appearances']
pl_15['Successful 50/50s per match'] = pl_15['Successful 50/50s']/pl_15['Appearances']
pl_15['Headed goals per match'] = pl_15['Headed goals']/pl_15['Appearances']

#pl_20
pl_20['Through balls per match'] = pl_20['Through balls']/pl_20['Appearances']
pl_20['Shots  per match'] = pl_20['Shots']/pl_20['Appearances']
pl_20['Big chances created per match'] = pl_20['Big chances created']/pl_20['Appearances']
pl_20['Crosses per match'] = pl_20['Crosses']/pl_20['Appearances']
pl_20['Assists per match'] = pl_20['Assists']/pl_20['Appearances']
pl_20['Penalties scored per match'] = pl_20['Penalties scored']/pl_20['Appearances']
pl_20['Freekicks scored per match'] = pl_20['Freekicks scored']/pl_20['Appearances']
pl_20['Interceptions per match'] = pl_20['Interceptions']/pl_20['Appearances']
pl_20['Tackles per match'] = pl_20['Tackles']/pl_20['Appearances']
pl_20['Successful 50/50s per match'] = pl_20['Successful 50/50s']/pl_20['Appearances']
pl_20['Headed goals per match'] = pl_20['Headed goals']/pl_20['Appearances']


# In[15]:


wingers_pl_15=pl_15[(pl_15['player_positions'].str.contains('ST')) | (pl_15['player_positions'].str.contains('CF')) | (pl_15['player_positions'].str.contains('RW')) | (pl_15['player_positions'].str.contains('LW')) |  (pl_15['player_positions'].str.contains('LM')) | (pl_15['player_positions'].str.contains('RM')) | (pl_15['player_positions'].str.contains('LS')) | (pl_15['player_positions'].str.contains('RS'))]
#player_attributes_fifa[(player_attributes_fifa['player_positions'].str.contains('ST')) | (player_attributes_fifa['player_positions'].str.contains('RW')) | (player_attributes_fifa['player_positions'].str.contains('LW')) | (player_attributes_fifa['player_positions'].str.contains('CF'))]
wingers_pl_20=pl_20[(pl_20['player_positions'].str.contains('ST')) | (pl_20['player_positions'].str.contains('CF')) | (pl_20['player_positions'].str.contains('RW')) | (pl_20['player_positions'].str.contains('LW')) |  (pl_15['player_positions'].str.contains('LM')) | (pl_20['player_positions'].str.contains('RM')) | (pl_20['player_positions'].str.contains('LS')) | (pl_20['player_positions'].str.contains('RS'))]


# In[16]:





# In[17]:





# In[18]:


inv_wingers_pl_15 = wingers_pl_15[((wingers_pl_15['preferred_foot'] == 'Right') & ((wingers_pl_15['team_position'] == 'LW') | (wingers_pl_15['team_position'] == 'LM'))) | ((wingers_pl_15['preferred_foot'] == 'Left') & ((wingers_pl_15['team_position'] == 'RW') | (wingers_pl_15['team_position'] == 'RM')))]
#player_attributes_fifa[(player_attributes_fifa['player_positions'].str.contains('ST')) | (player_attributes_fifa['player_positions'].str.contains('RW')) | (player_attributes_fifa['player_positions'].str.contains('LW')) | (player_attributes_fifa['player_positions'].str.contains('CF'))]
inv_wingers_pl_20 = wingers_pl_20[((wingers_pl_20['preferred_foot'] == 'Right') & ((wingers_pl_20['team_position'] == 'LW') | (wingers_pl_20['team_position'] == 'LM'))) | ((wingers_pl_20['preferred_foot'] == 'Left') & ((wingers_pl_20['team_position'] == 'RW') | (wingers_pl_20['team_position'] == 'RM')))]


# In[19]:


trad_wingers_pl_15 = wingers_pl_15[((wingers_pl_15['preferred_foot'] == 'Right') & ((wingers_pl_15['team_position'] == 'RW') | (wingers_pl_15['team_position'] == 'RM'))) | ((wingers_pl_15['preferred_foot'] == 'Left') & ((wingers_pl_15['team_position'] == 'LW') | (wingers_pl_15['team_position'] == 'LM')))]
#player_attributes_fifa[(player_attributes_fifa['player_positions'].str.contains('ST')) | (player_attributes_fifa['player_positions'].str.contains('RW')) | (player_attributes_fifa['player_positions'].str.contains('LW')) | (player_attributes_fifa['player_positions'].str.contains('CF'))]
trad_wingers_pl_20 = wingers_pl_20[((wingers_pl_20['preferred_foot'] == 'Left') & ((wingers_pl_20['team_position'] == 'LW') | (wingers_pl_20['team_position'] == 'LM'))) | ((wingers_pl_20['preferred_foot'] == 'Right') & ((wingers_pl_20['team_position'] == 'RW') | (wingers_pl_20['team_position'] == 'RM')))]




# 2015 Stats Inv Wingers/ Trad Wingers
print ('goals per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_15['Goals per match'].mean(),2),round(trad_wingers_pl_15['Goals per match'].mean(),2)))
print ('Through balls per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_15['Through balls per match'].mean(),2),round(trad_wingers_pl_15['Through balls per match'].mean(),2)))
print ('Shots per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_15['Shots  per match'].mean(),2),round(trad_wingers_pl_15['Shots  per match'].mean(),2)))
print ('Shooting accuracy %: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_15['Shooting accuracy %'].mean(),2),round(trad_wingers_pl_15['Shooting accuracy %'].mean(),2)))
print ('Passes per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_15['Passes per match'].mean(),2),round(trad_wingers_pl_15['Passes per match'].mean(),2)))
print ('Big chances per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_15['Big chances created per match'].mean(),2),round(trad_wingers_pl_15['Big chances created per match'].mean(),2)))
print ('Crosses per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_15['Crosses per match'].mean(),2),round(trad_wingers_pl_15['Crosses per match'].mean(),2)))
print ('Assists per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_15['Assists per match'].mean(),2),round(trad_wingers_pl_15['Assists per match'].mean(),2)))
print ('Penalties per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_15['Penalties scored per match'].mean(),2),round(trad_wingers_pl_15['Penalties scored per match'].mean(),2)))
print ('Freekicks per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_15['Freekicks scored per match'].mean(),2),round(trad_wingers_pl_15['Freekicks scored per match'].mean(),2)))
print ('Interceptions per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_15['Interceptions per match'].mean(),2),round(trad_wingers_pl_15['Interceptions per match'].mean(),2)))
print ('Tackles per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_15['Tackles per match'].mean(),2),round(trad_wingers_pl_15['Tackles per match'].mean(),2)))
print ('Successful 50/50s per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_15['Successful 50/50s per match'].mean(),2),round(trad_wingers_pl_15['Successful 50/50s per match'].mean(),2)))
print ('Headed goals per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_15['Headed goals per match'].mean(),2),round(trad_wingers_pl_15['Headed goals per match'].mean(),2)))


# In[24]:


# 2020 Stats Inv Wingers/ Trad Wingers
print ('goals per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_20['Goals per match'].mean(),2),round(trad_wingers_pl_20['Goals per match'].mean(),2)))
print ('Through balls per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_20['Through balls per match'].mean(),2),round(trad_wingers_pl_20['Through balls per match'].mean(),2)))
print ('Shots per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_20['Shots  per match'].mean(),2),round(trad_wingers_pl_20['Shots  per match'].mean(),2)))
print ('Shooting accuracy %: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_20['Shooting accuracy %'].mean(),2),round(trad_wingers_pl_20['Shooting accuracy %'].mean(),2)))
print ('Passes per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_20['Passes per match'].mean(),2),round(trad_wingers_pl_20['Passes per match'].mean(),2)))
print ('Big chances per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_20['Big chances created per match'].mean(),2),round(trad_wingers_pl_20['Big chances created per match'].mean(),2)))
print ('Crosses per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_20['Crosses per match'].mean(),2),round(trad_wingers_pl_20['Crosses per match'].mean(),2)))
print ('Assists per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_20['Assists per match'].mean(),2),round(trad_wingers_pl_20['Assists per match'].mean(),2)))
print ('Penalties per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_20['Penalties scored per match'].mean(),2),round(trad_wingers_pl_20['Penalties scored per match'].mean(),2)))
print ('Freekicks per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_20['Freekicks scored per match'].mean(),2),round(trad_wingers_pl_20['Freekicks scored per match'].mean(),2)))
print ('Interceptions per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_20['Interceptions per match'].mean(),2),round(trad_wingers_pl_20['Interceptions per match'].mean(),2)))
print ('Tackles per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_20['Tackles per match'].mean(),2),round(trad_wingers_pl_20['Tackles per match'].mean(),2)))
print ('Successful 50/50s per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_20['Successful 50/50s per match'].mean(),2),round(trad_wingers_pl_20['Successful 50/50s per match'].mean(),2)))
print ('Headed goals per match: Inv wingers:{}, Trad wingers:{}'.format(round(inv_wingers_pl_20['Headed goals per match'].mean(),2),round(trad_wingers_pl_20['Headed goals per match'].mean(),2)))


