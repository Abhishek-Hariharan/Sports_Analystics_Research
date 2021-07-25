#!/usr/bin/env python
# coding: utf-8
# FIFA Ratings - Wingers Analysis

# In[1]:


import pandas as pd


# In[3]:


#fifa15 data
fifa_15=pd.read_csv(r'G:\Fall 2020\Ireland\UCD\Modules\Summer\Sports Analytics\Research Project\Dataset\FIFA_Dataset\FIFA\players_15.csv')


# In[4]:


#fifa21 data
fifa_21=pd.read_csv(r'G:\Fall 2020\Ireland\UCD\Modules\Summer\Sports Analytics\Research Project\Dataset\FIFA_Dataset\FIFA\players_21.csv')


# In[5]:


fifa_15=fifa_15[['sofifa_id', 'short_name', 'long_name', 'age', 'height_cm', 'weight_kg',
       'overall', 'potential', 'value_eur', 'wage_eur', 'player_positions',
       'preferred_foot', 'weak_foot', 'skill_moves', 'team_position', 'pace',
       'shooting', 'passing', 'dribbling', 'defending', 'physic',
       'attacking_crossing', 'attacking_finishing',
       'attacking_heading_accuracy', 'attacking_short_passing',
       'attacking_volleys', 'skill_dribbling', 'skill_curve',
       'skill_long_passing', 'skill_ball_control', 'movement_sprint_speed',
       'movement_agility', 'movement_balance', 'power_shot_power',
       'power_jumping', 'power_stamina', 'power_strength', 'power_long_shots',
       'mentality_aggression', 'mentality_interceptions',
       'mentality_positioning', 'mentality_vision', 'mentality_penalties',
       'mentality_composure']]

fifa_21=fifa_21[['sofifa_id', 'short_name', 'long_name', 'age', 'height_cm', 'weight_kg',
       'overall', 'potential', 'value_eur', 'wage_eur', 'player_positions',
       'preferred_foot', 'weak_foot', 'skill_moves', 'team_position', 'pace',
       'shooting', 'passing', 'dribbling', 'defending', 'physic',
       'attacking_crossing', 'attacking_finishing',
       'attacking_heading_accuracy', 'attacking_short_passing',
       'attacking_volleys', 'skill_dribbling', 'skill_curve',
       'skill_long_passing', 'skill_ball_control', 'movement_sprint_speed',
       'movement_agility', 'movement_balance', 'power_shot_power',
       'power_jumping', 'power_stamina', 'power_strength', 'power_long_shots',
       'mentality_aggression', 'mentality_interceptions',
       'mentality_positioning', 'mentality_vision', 'mentality_penalties',
       'mentality_composure']]


# In[6]:


len(fifa_15),len(fifa_21)


# In[7]:


#player_attributes_fifa[(player_attributes_fifa['player_positions'].str.contains('ST')) | (player_attributes_fifa['player_positions'].str.contains('RW')) | (player_attributes_fifa['player_positions'].str.contains('LW')) | (player_attributes_fifa['player_positions'].str.contains('CF'))]
wingers_15=fifa_15[(fifa_15['player_positions'].str.contains('ST')) | (fifa_15['player_positions'].str.contains('CF')) | (fifa_15['player_positions'].str.contains('RW')) | (fifa_15['player_positions'].str.contains('LW')) | (fifa_15['player_positions'].str.contains('LM')) | (fifa_15['player_positions'].str.contains('RM')) | (fifa_15['player_positions'].str.contains('LS')) | (fifa_15['player_positions'].str.contains('RS'))]
wingers_21=fifa_21[(fifa_21['player_positions'].str.contains('ST')) | (fifa_21['player_positions'].str.contains('CF')) | (fifa_21['player_positions'].str.contains('RW')) | (fifa_21['player_positions'].str.contains('LW')) | (fifa_21['player_positions'].str.contains('LM')) | (fifa_21['player_positions'].str.contains('RM')) | (fifa_21['player_positions'].str.contains('LS')) | (fifa_21['player_positions'].str.contains('RS'))]


# In[8]:


#wingers_only[((wingers_only['preferred_foot-1'] == 'Right') & ((wingers_only['team_position'] == 'LW') | (wingers_only['team_position'] == 'SUB'))) | ((wingers_only['preferred_foot-1'] == 'Left') & ((wingers_only['team_position'] == 'RW') | (wingers_only['team_position'] == 'SUB')))]

inverted_wingers_15 = wingers_15[((wingers_15['preferred_foot'] == 'Right') & ((wingers_15['team_position'] == 'LW') | (wingers_15['team_position'] == 'LM'))) | ((wingers_15['preferred_foot'] == 'Left') & ((wingers_15['team_position'] == 'RW') | (wingers_15['team_position'] == 'RM')))]
inverted_wingers_21 = wingers_21[((wingers_21['preferred_foot'] == 'Right') & ((wingers_21['team_position'] == 'LW') | (wingers_21['team_position'] == 'LM'))) | ((wingers_21['preferred_foot'] == 'Left') & ((wingers_21['team_position'] == 'RW') | (wingers_21['team_position'] == 'RM')))]


# In[9]:


trad_wingers_15 = wingers_15[((wingers_15['preferred_foot'] == 'Left') & ((wingers_15['team_position'] == 'LW') | (wingers_15['team_position'] == 'LM'))) | ((wingers_15['preferred_foot'] == 'Right') & ((wingers_15['team_position'] == 'RW') | (wingers_15['team_position'] == 'RM')))]
trad_wingers_21 = wingers_21[((wingers_21['preferred_foot'] == 'Left') & ((wingers_21['team_position'] == 'LW') | (wingers_21['team_position'] == 'LM'))) | ((wingers_21['preferred_foot'] == 'Right') & ((wingers_21['team_position'] == 'RW') | (wingers_21['team_position'] == 'RM')))]



inverted_wingers_15['overall'].mean(),trad_wingers_15['overall'].mean()


# In[17]:


inverted_wingers_21['overall'].mean(),trad_wingers_21['overall'].mean()


# In[18]:


inverted_wingers_15['potential'].mean(),trad_wingers_15['potential'].mean()


# In[19]:


inverted_wingers_21['potential'].mean(),trad_wingers_21['potential'].mean()


# In[20]:


inverted_wingers_15['wage_eur'].mean(),trad_wingers_15['wage_eur'].mean()


# In[21]:


inverted_wingers_21['wage_eur'].mean(),trad_wingers_21['wage_eur'].mean()


# In[22]:


round(inverted_wingers_15['value_eur'].mean()),round(trad_wingers_15['value_eur'].mean())


# In[23]:


round(inverted_wingers_21['value_eur'].mean()),round(trad_wingers_21['value_eur'].mean())


# In[ ]:





# In[24]:


inverted_wingers_15['potential'].mean(),trad_wingers_15['potential'].mean()


# In[25]:


inverted_wingers_21['potential'].mean(),trad_wingers_21['potential'].mean()


# In[26]:


round(inverted_wingers_15['height_cm'].mean()),round(trad_wingers_15['height_cm'].mean())


# In[27]:


inverted_wingers_15['age'].mean(),trad_wingers_15['age'].mean()


# In[28]:


inverted_wingers_15['weak_foot'].mean(),trad_wingers_15['weak_foot'].mean()


# In[29]:


inverted_wingers_21['weak_foot'].mean(),trad_wingers_21['weak_foot'].mean()


# In[30]:


inverted_wingers_15['skill_moves'].mean(),trad_wingers_15['skill_moves'].mean()


# In[31]:


inverted_wingers_21['skill_moves'].mean(),trad_wingers_21['skill_moves'].mean()


# In[32]:


inverted_wingers_15['dribbling'].mean(),trad_wingers_15['dribbling'].mean()


# In[33]:


inverted_wingers_21['dribbling'].mean(),trad_wingers_21['dribbling'].mean()


# In[34]:


inverted_wingers_15['pace'].mean(),trad_wingers_15['pace'].mean()


# In[35]:


inverted_wingers_21['pace'].mean(),trad_wingers_21['pace'].mean()


# In[36]:


inverted_wingers_15['shooting'].mean(),trad_wingers_15['shooting'].mean()


# In[37]:


inverted_wingers_21['shooting'].mean(),trad_wingers_21['shooting'].mean()


# In[38]:


inverted_wingers_15['passing'].mean(),trad_wingers_15['passing'].mean()


# In[39]:


inverted_wingers_21['passing'].mean(),trad_wingers_21['passing'].mean()


# In[40]:


inverted_wingers_15['defending'].mean(),trad_wingers_15['defending'].mean()


# In[41]:


inverted_wingers_21['defending'].mean(),trad_wingers_21['defending'].mean()


# In[42]:


inverted_wingers_15['attacking_crossing'].mean(),trad_wingers_15['attacking_crossing'].mean()


# In[43]:


inverted_wingers_21['attacking_crossing'].mean(),trad_wingers_21['attacking_crossing'].mean()


# In[44]:


inverted_wingers_15['attacking_finishing'].mean(),trad_wingers_15['attacking_finishing'].mean()


# In[45]:


inverted_wingers_21['attacking_finishing'].mean(),trad_wingers_21['attacking_finishing'].mean()


# In[46]:


inverted_wingers_15['attacking_heading_accuracy'].mean(),trad_wingers_15['attacking_heading_accuracy'].mean()


# In[47]:


inverted_wingers_21['attacking_heading_accuracy'].mean(),trad_wingers_21['attacking_heading_accuracy'].mean()


# In[48]:


inverted_wingers_15['attacking_short_passing'].mean(),trad_wingers_15['attacking_short_passing'].mean()


# In[49]:


inverted_wingers_21['attacking_short_passing'].mean(),trad_wingers_21['attacking_short_passing'].mean()


# In[50]:


inverted_wingers_15['skill_dribbling'].mean(),trad_wingers_15['skill_dribbling'].mean()


# In[51]:


inverted_wingers_21['skill_dribbling'].mean(),trad_wingers_21['skill_dribbling'].mean()


# In[52]:


inverted_wingers_15['skill_curve'].mean(),trad_wingers_15['skill_curve'].mean()


# In[53]:


inverted_wingers_21['skill_curve'].mean(),trad_wingers_21['skill_curve'].mean()


# In[54]:


inverted_wingers_15['skill_long_passing'].mean(),trad_wingers_15['skill_long_passing'].mean()


# In[55]:


inverted_wingers_21['skill_long_passing'].mean(),trad_wingers_21['skill_long_passing'].mean()


# In[56]:


inverted_wingers_15['skill_ball_control'].mean(),trad_wingers_15['skill_ball_control'].mean()


# In[57]:


inverted_wingers_21['skill_ball_control'].mean(),trad_wingers_21['skill_ball_control'].mean()


# In[58]:


inverted_wingers_15['movement_sprint_speed'].mean(),trad_wingers_15['movement_sprint_speed'].mean()


# In[64]:


inverted_wingers_21['movement_sprint_speed'].mean(),trad_wingers_21['movement_sprint_speed'].mean()


# In[62]:


inverted_wingers_15['movement_agility'].mean(),trad_wingers_15['movement_agility'].mean()


# In[63]:


inverted_wingers_21['movement_agility'].mean(),trad_wingers_21['movement_agility'].mean()


# In[65]:


inverted_wingers_15['power_shot_power'].mean(),trad_wingers_15['power_shot_power'].mean()


# In[66]:


inverted_wingers_21['power_shot_power'].mean(),trad_wingers_21['power_shot_power'].mean()


# In[67]:


inverted_wingers_15['movement_balance'].mean(),trad_wingers_15['movement_balance'].mean()


# In[68]:


inverted_wingers_21['movement_balance'].mean(),trad_wingers_21['movement_balance'].mean()


# In[70]:


inverted_wingers_15['power_jumping'].mean(),trad_wingers_15['power_jumping'].mean()


# In[71]:


inverted_wingers_21['power_jumping'].mean(),trad_wingers_21['power_jumping'].mean()


# In[72]:


inverted_wingers_15['power_stamina'].mean(),trad_wingers_15['power_stamina'].mean()


# In[73]:


inverted_wingers_21['power_stamina'].mean(),trad_wingers_21['power_stamina'].mean()


# In[74]:


inverted_wingers_15['power_strength'].mean(),trad_wingers_15['power_strength'].mean()


# In[75]:


inverted_wingers_21['power_strength'].mean(),trad_wingers_21['power_strength'].mean()


# In[76]:


inverted_wingers_15['mentality_interceptions'].mean(),trad_wingers_15['mentality_interceptions'].mean()


# In[77]:


inverted_wingers_21['mentality_interceptions'].mean(),trad_wingers_21['mentality_interceptions'].mean()


# In[78]:


inverted_wingers_15['mentality_positioning'].mean(),trad_wingers_15['mentality_positioning'].mean()


# In[79]:


inverted_wingers_21['mentality_positioning'].mean(),trad_wingers_21['mentality_positioning'].mean()


# In[80]:


inverted_wingers_15['mentality_vision'].mean(),trad_wingers_15['mentality_vision'].mean()


# In[81]:


inverted_wingers_21['mentality_vision'].mean(),trad_wingers_21['mentality_vision'].mean()


# In[ ]:





# In[ ]:


inverted_wingers_15.dribbling.hist()


# In[82]:


trad_wingers_15.dribbling.hist()


# In[52]:


# Hypothesis testing for dribbling (considering fifa 15-16 season)
import numpy as np
from scipy import stats
from statsmodels.stats.power import TTestIndPower
import seaborn as sns


# In[57]:


from matplotlib import pyplot as plt


# In[105]:


inverted_wingers_15.columns


# In[107]:


inv_dribble_array=np.array(inverted_wingers_15['dribbling'])
trad_dribble_array=np.array(trad_wingers_15['dribbling'])

inv_crossing_array=np.array(inverted_wingers_15['attacking_crossing'])
trad_crossing_array=np.array(trad_wingers_15['attacking_crossing'])

inv_attck_array=np.array(inverted_wingers_15['attacking_finishing'])
trad_attck_array=np.array(trad_wingers_15['attacking_finishing'])


# In[108]:


x_bar_inv_dribble=np.mean(inverted_wingers_15['dribbling'])
x_bar_trad_dribble=np.mean(trad_wingers_15['dribbling'])

x_bar_inv_crossing=np.mean(inverted_wingers_15['attacking_crossing'])
x_bar_trad_crossing=np.mean(trad_wingers_15['attacking_crossing'])

x_bar_inv_attck=np.mean(inverted_wingers_15['attacking_finishing'])
x_bar_trad_attck=np.mean(trad_wingers_15['attacking_finishing'])


# In[109]:


x_bar_inv_dribble,x_bar_trad_dribble,x_bar_inv_crossing,x_bar_trad_crossing,x_bar_inv_attck,x_bar_trad_attck


# In[34]:


diff= x_bar_inv_dribble - x_bar_trad_dribble
diff


# In[74]:


diff1= x_bar_inv_crossing - x_bar_trad_crossing
diff1


# In[30]:


#Cohen's d Effective Size for dribbling
n_inv = len(inv_dribble_array)

n_trad = len(trad_dribble_array)

inv_total = sum(inv_dribble_array)
trad_total = sum(trad_dribble_array)

inv_rate = inv_total/n_inv
trad_rate = trad_total/n_trad

diff = inv_rate-trad_rate
print(f"inv dribble Rate: {inv_rate}")
print(f"trad dribble Rate: {trad_rate}")
print(f"Difference: {diff}")


# In[86]:


#Cohen's d Effective Size for crossing
n_inv1 = len(inv_crossing_array)

n_trad1 = len(trad_crossing_array)

inv_total1 = sum(inv_crossing_array)
trad_total1 = sum(trad_crossing_array)

inv_rate1 = inv_total1/n_inv1
trad_rate1 = trad_total1/n_trad1

diff1 = trad_rate1-inv_rate1
print(f"inv dribble Rate: {inv_rate1}")
print(f"trad dribble Rate: {trad_rate1}")
print(f"Difference: {diff1}")


# In[110]:


#Cohen's d Effective Size for attacking finishing
n_inv2 = len(inv_attck_array)

n_trad2 = len(trad_attck_array)

inv_total2 = sum(inv_attck_array)
trad_total2 = sum(trad_attck_array)

inv_rate2 = inv_total2/n_inv2
trad_rate2 = trad_total2/n_trad2

diff2 = inv_rate2-trad_rate2
print(f"inv dribble Rate: {inv_rate2}")
print(f"trad dribble Rate: {trad_rate2}")
print(f"Difference: {diff2}")


# In[87]:


var_inv_cross=inv_crossing_array.var()
var_trad_cross=trad_crossing_array.var()
var_inv_cross,var_trad_cross


# In[88]:


var_inv_dribble=inv_dribble_array.var()
var_trad_dribble=trad_dribble_array.var()
var_inv_dribble,var_trad_dribble


# In[111]:


var_inv_attck=inv_attck_array.var()
var_trad_attck=trad_attck_array.var()
var_inv_attck,var_trad_attck


# In[83]:


pooled_var = (n_inv * var_inv_dribble + n_trad * var_trad_dribble) / (n_inv + n_trad)
cohens_d = diff / np.sqrt(pooled_var)


# In[89]:


pooled_var1 = (n_inv1 * var_inv_cross + n_trad1 * var_trad_cross) / (n_inv1 + n_trad1)
cohens_d1 = diff1 / np.sqrt(pooled_var1)


# In[112]:


pooled_var2 = (n_inv2 * var_inv_attck + n_trad2 * var_trad_attck) / (n_inv2 + n_trad2)
cohens_d2 = diff2 / np.sqrt(pooled_var2)


# In[113]:


cohens_d1,cohens_d,cohens_d2


# In[91]:


# parameters Initialization for dribbling
effect = cohens_d
alpha = 0.05
sign_lvl = 0.95
# sample 2 / sample 1   
ratio = len(inv_dribble_array) / len(trad_dribble_array)
# Perform power analysis
analysis = TTestIndPower()
result = analysis.solve_power(effect, power=sign_lvl, nobs1=None,ratio=ratio, alpha=alpha)
print(f"The sample size is: {result}")


# In[94]:


# parameters Initialization for crossing
effect1 = cohens_d1
alpha1 = 0.05
sign_lvl1 = 0.95
# sample 2 / sample 1   
ratio1 = len(inv_crossing_array) / len(trad_crossing_array)
# Perform power analysis
analysis1 = TTestIndPower()
result1 = analysis1.solve_power(effect1, power=sign_lvl1, nobs1=None,ratio=ratio1, alpha=alpha1)
print(f"The sample size is: {result1}")


# In[114]:


# parameters Initialization for crossing
effect2 = cohens_d2
alpha = 0.05
sign_lvl = 0.95
# sample 2 / sample 1   
ratio2 = len(inv_attck_array) / len(trad_attck_array)
# Perform power analysis
analysis2 = TTestIndPower()
result2 = analysis1.solve_power(effect2, power=sign_lvl, nobs1=None,ratio=ratio2, alpha=alpha)
print(f"The sample size is: {result2}")


# In[46]:


# Bootstrapping samples for dribbling
sample_means_inv = []
for _ in range(50):
    sample_mean = np.random.choice(inv_dribble_array,size=382).mean()
    sample_means_inv.append(sample_mean)
len(sample_means_inv)

sample_means_trad = []
for _ in range(50):
    sample_mean = np.random.choice(trad_dribble_array,size=382).mean()
    sample_means_trad.append(sample_mean)
len(sample_means_trad)


# In[95]:


# Bootstrapping samples for crossing
sample_means_inv_crossing = []
for _ in range(50):
   sample_mean1 = np.random.choice(inv_crossing_array,size=382).mean()
   sample_means_inv_crossing.append(sample_mean1)
len(sample_means_inv_crossing)

sample_means_trad_crossing = []
for _ in range(50):
   sample_mean1 = np.random.choice(trad_crossing_array,size=382).mean()
   sample_means_trad_crossing.append(sample_mean1)
len(sample_means_trad_crossing)


# In[115]:


# Bootstrapping samples for crossing
sample_means_inv_attacking= []
for _ in range(50):
   sample_mean2 = np.random.choice(inv_attck_array,size=286).mean()
   sample_means_inv_attacking.append(sample_mean2)
len(sample_means_inv_attacking)

sample_means_trad_attacking = []
for _ in range(50):
   sample_mean2 = np.random.choice(trad_attck_array,size=286).mean()
   sample_means_trad_attacking.append(sample_mean2)
len(sample_means_trad_attacking)


# In[65]:


def cal_var(sample):
    '''Computes the variance a list of values'''
    sample_mean = np.mean(sample)
    return sum([(i - sample_mean)**2 for i in sample])

def cal_sample_var(sample1, sample2):
    '''Computes the pooled variance 2 lists of values, using the calc_variance function'''
    n_1, n_2 = len(sample1), len(sample2)
    var1, var2 = cal_var(sample1), cal_var(sample2)
    return (var1 + var2) / ((n_1 + n_2) - 2)

def twosample_tstatistic(expr, ctrl):
    '''Computes the 2-sample T-stat of 2 lists of values, using the calc_sample_variance function'''
    expr_mean, ctrl_mean = np.mean(expr), np.mean(ctrl)
    n_e, n_c = len(expr), len(ctrl)
    samp_var = cal_sample_var(expr,ctrl)
    t = (expr_mean - ctrl_mean) / np.sqrt(samp_var * ((1/n_e)+(1/n_c)))
    return t


# In[99]:


t_stat = twosample_tstatistic(sample_means_inv, sample_means_trad)

t_stat


# In[67]:


stats.ttest_ind(sample_means_inv, sample_means_trad)
# p < 0.05 (rejecting H0)


# In[98]:


stats.ttest_ind(sample_means_inv_crossing, sample_means_trad_crossing)
# p > 0.05 (keeping H0) for crossing


# In[116]:


stats.ttest_ind(sample_means_inv_attacking, sample_means_trad_attacking)
# p < 0.05 (rejecting H0) for attacking finishing


# In[143]:

f, axes = plt.subplots(nrows=3,ncols= 1, figsize=(12, 12))
f.tight_layout(pad=4) 
sns.set(color_codes=True)
sns.distplot(sample_means_inv,label='Inverted Wingers',ax=axes[0])
sns.distplot(sample_means_trad,label='Traditional Wingers',ax=axes[0])
axes[0].set_title('Inverted wingers Vs Trad. wingers Dribbling Distribution')
axes[0].set_xlabel('Dribbling')
axes[0].set_ylabel('Density')
axes[0].legend()

sns.distplot(sample_means_inv_crossing,label='Inverted Wingers',ax=axes[1]) 
sns.distplot(sample_means_trad_crossing,label='Traditional Wingers',ax=axes[1])
axes[1].set_title('Inverted wingers Vs Trad. wingers Crossing Distribution')
axes[1].set_xlabel('Crossing')
axes[1].set_ylabel('Density')
axes[1].legend()

sns.distplot(sample_means_inv_attacking,label='Inverted Wingers',ax=axes[2]) 
sns.distplot(sample_means_trad_attacking,label='Traditional Wingers',ax=axes[2])
axes[2].set_title('Inverted wingers Vs Trad. wingers Attack-Finishing Distribution')
axes[2].set_xlabel('Attack-finishing')
axes[2].set_ylabel('Density')
axes[2].legend()


plt.savefig(r'G:\Fall 2020\Ireland\UCD\Modules\Summer\Sports Analytics\Research Project\final_consolidated.png')






# In[126]:


sns.set(color_codes=True)
sns.set(rc={'figure.figsize':(12,12)})
sns.distplot(sample_means_inv_crossing,label='Inverted Wingers') 
sns.distplot(sample_means_trad_crossing,label='Traditional Wingers')
plt.title('Inverted wingers Vs Trad. wingers Crossing skills Distribution')
plt.xlabel('Crossing')
plt.ylabel('Density')
plt.legend()
plt.savefig(r'G:\Fall 2020\Ireland\UCD\Modules\Summer\Sports Analytics\Research Project\pic2.png')


# In[127]:


sns.set(color_codes=True)
sns.set(rc={'figure.figsize':(12,12)})
sns.distplot(sample_means_inv_attacking,label='Inverted Wingers') 
sns.distplot(sample_means_trad_attacking,label='Traditional Wingers')
plt.title('Inverted wingers Vs Trad. wingers Attack Finishing Distribution')
plt.xlabel('Attack finishing')
plt.ylabel('Density')
plt.legend()
plt.savefig(r'G:\Fall 2020\Ireland\UCD\Modules\Summer\Sports Analytics\Research Project\pic3.png')


# In[119]:


np.mean(inverted_wingers_15['attacking_finishing']),np.mean(trad_wingers_15['attacking_finishing'])


# In[ ]:


sns.savefig("output.png")






