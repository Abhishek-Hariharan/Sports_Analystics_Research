#!/usr/bin/env python
# coding: utf-8

# 2008 - 2016 match stats  analysis
# In[1]:


import sqlite3
from sqlite3 import Error


# In[1]:


import pandas as pd


# In[3]:


database = 'G:/Fall 2020/Ireland/UCD/Modules/Summer/Sports Analytics/Research Project/Dataset/database.sqlite'


# In[4]:


conn = sqlite3.connect(database)
#conn


# In[5]:


cur= conn.cursor()


# In[7]:


cur.execute('SELECT * FROM COUNTRY')
country_table=cur.fetchall()


# In[8]:


cur.execute('SELECT * FROM LEAGUE')
league_table=cur.fetchall()


# In[9]:


cur.execute('SELECT * FROM Match')
Match_table=cur.fetchall()


# In[25]:


league_table.fetchall()


# In[84]:


# Seperate DataFrame created for each tables

#Country
country_df = pd.read_sql_query('SELECT * FROM COUNTRY', conn)
db_df.to_csv('Summer/Sports Analytics/Research Project/Dataset/Country_table.csv', index=False)

#League
league_df = pd.read_sql_query('SELECT * FROM LEAGUE', conn)
league_df.to_csv('Summer/Sports Analytics/Research Project/Dataset/League_table.csv', index=False)

#League
matches_df = pd.read_sql_query('SELECT * FROM Match', conn)
matches_df.to_csv('Summer/Sports Analytics/Research Project/Dataset/Match_table.csv', index=False)


# In[85]:





# In[86]:


league_df


# In[6]:


player_df = pd.read_sql_query('SELECT * FROM Player', conn)
player_df.to_csv('Summer/Sports Analytics/Research Project/Dataset/Player_table.csv', index=False)


# In[7]:


player_attributes_df = pd.read_sql_query('SELECT * FROM Player_Attributes', conn)
player_attributes_df.to_csv('Summer/Sports Analytics/Research Project/Dataset/Player_Attributes_table.csv', index=False)


# In[8]:


team_df = pd.read_sql_query('SELECT * FROM Team',conn)
team_df.to_csv('Summer/Sports Analytics/Research Project/Dataset/Team_table.csv', index=False)


# In[9]:


team_attributes_df = pd.read_sql_query('SELECT * FROM Team_Attributes',conn)
team_attributes_df.to_csv('Summer/Sports Analytics/Research Project/Dataset/Team_Attributes_table.csv', index=False)


# In[10]:


df_match_team=pd.read_csv('Summer/Sports Analytics/Research Project/Dataset/Tableau_Prep_Output/Match_Team_Combined.csv')


# In[11]:


df_match_team['home_team_name'] = df_match_team['team_long_name'].copy()


# In[12]:


df_match_team[['home_team_api_id','home_team_name','away_team_api_id']] 


# In[13]:


# To map the away team id to team names of existing id's
team_api=dict(zip(df_match_team.home_team_api_id,df_match_team.home_team_name))


# In[14]:


df_match_team['away_team_name']=df_match_team['away_team_api_id'].copy()


# In[15]:


df_match_team['away_team_name']=df_match_team['away_team_name'].map(team_api)


# In[16]:


df_match_team[['home_team_api_id','away_team_api_id','home_team_name','away_team_name']]


# In[17]:





# In[18]:


df_match_team.drop(['home_player_X1','home_player_X2','home_player_X3','home_player_X4','home_player_X5','home_player_X6','home_player_X7','home_player_X8','home_player_X9','home_player_X10','home_player_X11','away_player_X1','away_player_X2','away_player_X3','away_player_X4','away_player_X5','away_player_X6','away_player_X7','away_player_X8','away_player_X9','away_player_X10','away_player_X11','home_player_Y1','home_player_Y2','home_player_Y3','home_player_Y4','home_player_Y5','home_player_Y6','home_player_Y7','home_player_Y8','home_player_Y9','home_player_Y10','home_player_Y11','away_player_Y1','away_player_Y2','away_player_Y3','away_player_Y4','away_player_Y5','away_player_Y6','away_player_Y7','away_player_Y8','away_player_Y9','away_player_Y10','away_player_Y11'],axis=1,inplace=True)


# In[19]:


df_match_team.columns


# In[20]:


player_attributes_fifa=pd.read_csv(r'Summer\Sports Analytics\Research Project\Dataset\Tableau_Prep_Output\Player_Attributes_FIFA15_combined.csv')


# In[21]:


import numpy as np


# In[27]:





# In[22]:


wingers_only = player_attributes_fifa[(player_attributes_fifa['player_positions'].str.contains('ST')) | (player_attributes_fifa['player_positions'].str.contains('RW')) | (player_attributes_fifa['player_positions'].str.contains('LW')) | (player_attributes_fifa['player_positions'].str.contains('CF')) |  (player_attributes_fifa['player_positions'].str.contains('LM')) | (player_attributes_fifa['player_positions'].str.contains('RM')) | (player_attributes_fifa['player_positions'].str.contains('LS')) | (player_attributes_fifa['player_positions'].str.contains('RS'))]


# In[165]:



#wingers_only = player_attributes_fifa[(player_attributes_fifa['team_position'] == 'LW') | (player_attributes_fifa['team_position'] == 'RW') | (player_attributes_fifa['team_position'] == 'RAM') | (player_attributes_fifa['team_position'] == 'LAM') | (player_attributes_fifa['team_position'] == 'ST') | (player_attributes_fifa['team_position'] == 'CF') | (player_attributes_fifa['team_position'] == 'RM') | (player_attributes_fifa['team_position'] == 'LM')  ]


# In[23]:





# In[24]:


winger_id_names=dict(zip(wingers_only['player_api_id'],wingers_only['player_name']))


# In[25]:





# In[26]:





# In[29]:


winger_id_names


# In[33]:


#left_inverted_wingers = wingers_only[(wingers_only['preferred_foot-1'] == 'Right') & ((wingers_only['team_position'] == 'LW') | (wingers_only['team_position'] == 'SUB'))]


# In[34]:


#right_inverted_wingers = wingers_only[(wingers_only['preferred_foot-1'] == 'Left') & ((wingers_only['team_position'] == 'RW') | (wingers_only['team_position'] == 'SUB'))]


# In[35]:


#left_trad_wingers = wingers_only[(wingers_only['preferred_foot-1'] == 'Left') & ((wingers_only['team_position'] == 'LW') | (wingers_only['team_position'] == 'SUB'))]


# In[36]:


#right_trad_wingers= wingers_only[(wingers_only['preferred_foot-1'] == 'Right') & ((wingers_only['team_position'] == 'RW') | (wingers_only['team_position'] == 'SUB'))]


# In[37]:





# In[72]:


#dataframe for inverted foot wingers 
inverted_wingers = wingers_only[((wingers_only['preferred_foot-1'] == 'Right') & ((wingers_only['team_position'] == 'LW') | (wingers_only['team_position'] == 'LM'))) | ((wingers_only['preferred_foot-1'] == 'Left') & ((wingers_only['team_position'] == 'RW') | (wingers_only['team_position'] == 'RM')))]


# In[28]:


#dataframe for traditonal foot wingers 
traditional_wingers = wingers_only[((wingers_only['preferred_foot-1'] == 'Left') & ((wingers_only['team_position'] == 'LW') | (wingers_only['team_position'] == 'LM'))) | ((wingers_only['preferred_foot-1'] == 'Right') & ((wingers_only['team_position'] == 'RW') | (wingers_only['team_position'] == 'RM')))]


# In[73]:





# In[29]:


# Inverted Winger stats for the matches played
inv_winger_match_stats=df_match_team.copy()


# In[30]:


#traditional winger stats for the matches played
traditional_winger_match_stats=df_match_team.copy()


# In[31]:


# dictionary having inverted wingers player id and names
inverted_wingers_dict=dict(zip(inverted_wingers['player_api_id'],inverted_wingers['player_name']))


# In[32]:


# dictionary having traditional wingers player id and names
traditional_wingers_dict=dict(zip(traditional_wingers['player_api_id'],traditional_wingers['player_name']))


# In[33]:


inv_winger_match_stats['home_player_1']=inv_winger_match_stats['home_player_1'].map(inverted_wingers_dict)


# In[34]:


inv_winger_match_stats['home_player_2']=inv_winger_match_stats['home_player_2'].map(inverted_wingers_dict)


# In[35]:


inv_winger_match_stats['home_player_3']=inv_winger_match_stats['home_player_3'].map(inverted_wingers_dict)


# In[36]:


inv_winger_match_stats['home_player_4']=inv_winger_match_stats['home_player_4'].map(inverted_wingers_dict)


# In[37]:


inv_winger_match_stats['home_player_5']=inv_winger_match_stats['home_player_5'].map(inverted_wingers_dict)


# In[38]:


inv_winger_match_stats['home_player_6']=inv_winger_match_stats['home_player_6'].map(inverted_wingers_dict)


# In[39]:


inv_winger_match_stats['home_player_7']=inv_winger_match_stats['home_player_7'].map(inverted_wingers_dict)


# In[40]:


inv_winger_match_stats['home_player_8']=inv_winger_match_stats['home_player_8'].map(inverted_wingers_dict)


# In[41]:


inv_winger_match_stats['home_player_9']=inv_winger_match_stats['home_player_9'].map(inverted_wingers_dict)


# In[42]:


inv_winger_match_stats['home_player_10']=inv_winger_match_stats['home_player_10'].map(inverted_wingers_dict)


# In[43]:


inv_winger_match_stats['home_player_11']=inv_winger_match_stats['home_player_11'].map(inverted_wingers_dict)


# In[44]:


inv_winger_match_stats['away_player_1']=inv_winger_match_stats['away_player_1'].map(inverted_wingers_dict)


# In[45]:


inv_winger_match_stats['away_player_2']=inv_winger_match_stats['away_player_2'].map(inverted_wingers_dict)


# In[46]:


inv_winger_match_stats['away_player_3']=inv_winger_match_stats['away_player_3'].map(inverted_wingers_dict)


# In[47]:


inv_winger_match_stats['away_player_4']=inv_winger_match_stats['away_player_4'].map(inverted_wingers_dict)


# In[48]:


inv_winger_match_stats['away_player_5']=inv_winger_match_stats['away_player_5'].map(inverted_wingers_dict)


# In[49]:


inv_winger_match_stats['away_player_6']=inv_winger_match_stats['away_player_6'].map(inverted_wingers_dict)


# In[50]:


inv_winger_match_stats['away_player_7']=inv_winger_match_stats['away_player_7'].map(inverted_wingers_dict)


# In[51]:


inv_winger_match_stats['away_player_8']=inv_winger_match_stats['away_player_8'].map(inverted_wingers_dict)


# In[52]:


inv_winger_match_stats['away_player_9']=inv_winger_match_stats['away_player_9'].map(inverted_wingers_dict)


# In[53]:


inv_winger_match_stats['away_player_10']=inv_winger_match_stats['away_player_10'].map(inverted_wingers_dict)


# In[54]:


inv_winger_match_stats['away_player_11']=inv_winger_match_stats['away_player_11'].map(inverted_wingers_dict)


# In[62]:





# In[55]:


inv_winger_match_stats.to_csv(r'Summer\Sports Analytics\Research Project\Dataset\inv_winger_match_stats.csv',index=False)


# In[61]:





# In[57]:


traditional_winger_match_stats['home_player_1']=traditional_winger_match_stats['home_player_1'].map(traditional_wingers_dict)
traditional_winger_match_stats['home_player_2']=traditional_winger_match_stats['home_player_2'].map(traditional_wingers_dict)
traditional_winger_match_stats['home_player_3']=traditional_winger_match_stats['home_player_3'].map(traditional_wingers_dict)
traditional_winger_match_stats['home_player_4']=traditional_winger_match_stats['home_player_4'].map(traditional_wingers_dict)
traditional_winger_match_stats['home_player_5']=traditional_winger_match_stats['home_player_5'].map(traditional_wingers_dict)
traditional_winger_match_stats['home_player_6']=traditional_winger_match_stats['home_player_6'].map(traditional_wingers_dict)
traditional_winger_match_stats['home_player_7']=traditional_winger_match_stats['home_player_7'].map(traditional_wingers_dict)
traditional_winger_match_stats['home_player_8']=traditional_winger_match_stats['home_player_8'].map(traditional_wingers_dict)
traditional_winger_match_stats['home_player_9']=traditional_winger_match_stats['home_player_9'].map(traditional_wingers_dict)
traditional_winger_match_stats['home_player_10']=traditional_winger_match_stats['home_player_10'].map(traditional_wingers_dict)
traditional_winger_match_stats['home_player_11']=traditional_winger_match_stats['home_player_11'].map(traditional_wingers_dict)
traditional_winger_match_stats['away_player_1']=traditional_winger_match_stats['away_player_1'].map(traditional_wingers_dict)
traditional_winger_match_stats['away_player_2']=traditional_winger_match_stats['away_player_2'].map(traditional_wingers_dict)
traditional_winger_match_stats['away_player_3']=traditional_winger_match_stats['away_player_3'].map(traditional_wingers_dict)
traditional_winger_match_stats['away_player_4']=traditional_winger_match_stats['away_player_4'].map(traditional_wingers_dict)
traditional_winger_match_stats['away_player_5']=traditional_winger_match_stats['away_player_5'].map(traditional_wingers_dict)
traditional_winger_match_stats['away_player_6']=traditional_winger_match_stats['away_player_6'].map(traditional_wingers_dict)
traditional_winger_match_stats['away_player_7']=traditional_winger_match_stats['away_player_7'].map(traditional_wingers_dict)
traditional_winger_match_stats['away_player_8']=traditional_winger_match_stats['away_player_8'].map(traditional_wingers_dict)
traditional_winger_match_stats['away_player_9']=traditional_winger_match_stats['away_player_9'].map(traditional_wingers_dict)
traditional_winger_match_stats['away_player_10']=traditional_winger_match_stats['away_player_10'].map(traditional_wingers_dict)
traditional_winger_match_stats['away_player_11']=traditional_winger_match_stats['away_player_11'].map(traditional_wingers_dict)


# In[58]:


traditional_winger_match_stats.to_csv(r'Summer\Sports Analytics\Research Project\Dataset\trad_winger_match_stats.csv',index=False)


# In[66]:


inv_winger_match_stats_1=pd.read_csv(r'Summer\Sports Analytics\Research Project\Dataset\Tableau_Prep_Output\Inverted_Wingers_Match_Stats_filtered.csv')


# In[67]:


traditional_winger_match_stats_1=pd.read_csv(r'Summer\Sports Analytics\Research Project\Dataset\Tableau_Prep_Output\Traditional_Wingers_Match_Stats_filtered.csv')


# In[68]:


inv_winger_match_stats_1.home_team_goal


# In[74]:


inv_winger_match_stats_1.columns


# In[75]:





# In[76]:


traditional_winger_match_stats_1[['home_team_goal','away_team_goal']]


# In[77]:


inv_winger_match_stats_1['home_team_win'] =np.where(inv_winger_match_stats_1['home_team_goal'] > inv_winger_match_stats_1['away_team_goal'],'Win','Lose/Draw')

#pd['irr'] = np.where(pd['cs']*0.63 > pd['irr'], 1.0, 0.0)


# In[78]:


inv_winger_match_stats_1['away_team_win'] =np.where(inv_winger_match_stats_1['home_team_goal'] < inv_winger_match_stats_1['away_team_goal'],'Win','Lose/Draw')


# In[79]:


traditional_winger_match_stats_1['home_team_win'] =np.where(traditional_winger_match_stats_1['home_team_goal'] > traditional_winger_match_stats_1['away_team_goal'],'Win','Lose/Draw')
traditional_winger_match_stats_1['away_team_win'] =np.where(traditional_winger_match_stats_1['home_team_goal'] < traditional_winger_match_stats_1['away_team_goal'],'Win','Lose/Draw')


# In[80]:


# HOME TEAM WINS FOR INVERTED WINGERS
round(len(inv_winger_match_stats_1[inv_winger_match_stats_1['home_team_win'] == 'Win'])/len(inv_winger_match_stats_1),2)


# In[81]:


# AWAY TEAM WINS FOR INVERTED WINGERS
round(len(inv_winger_match_stats_1[inv_winger_match_stats_1['away_team_win'] == 'Win'])/len(inv_winger_match_stats_1),2)


# In[82]:


# HOME TEAM WINS FOR TRADITIONAL WINGERS
round(len(traditional_winger_match_stats_1[traditional_winger_match_stats_1['home_team_win'] == 'Win'])/len(traditional_winger_match_stats_1),2)


# In[83]:


# AWAY TEAM WINS FOR TRADITIONAL WINGERS
round(len(traditional_winger_match_stats_1[traditional_winger_match_stats_1['away_team_win'] == 'Win'])/len(traditional_winger_match_stats_1),2)


# In[84]:


# Inv wingers-> total goals in home and away matches
inv_winger_match_stats_1.home_team_goal.sum(),inv_winger_match_stats_1.away_team_goal.sum()


# In[85]:


# Trad wingers-> total goals in home and away matches
traditional_winger_match_stats_1.home_team_goal.sum(),traditional_winger_match_stats_1.away_team_goal.sum()


# In[86]:


#Goals per match -> Inv Wingers Contribution
inv_winger_match_stats_1.home_team_goal.sum()/len(inv_winger_match_stats_1),inv_winger_match_stats_1.away_team_goal.sum()/len(inv_winger_match_stats_1) 


# In[87]:


#Goals per match -> trad Wingers Contribution
traditional_winger_match_stats_1.home_team_goal.sum()/len(traditional_winger_match_stats_1),traditional_winger_match_stats_1.away_team_goal.sum()/len(traditional_winger_match_stats_1)






