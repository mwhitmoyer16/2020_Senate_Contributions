#Analyzing the contributions for Senate races in four key states
#MWhitmoyer

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

key_states = pd.read_pickle('key_states_pkl.zip')
pop = pd.read_csv('pop.csv')
pop = pop.rename({'STATE':'SOURCE_STATE'},axis='columns')

###ANALYZING BY CONTRIBUTION SOURCE AND SIZE

#sorting by the key election state, Democrat or Republican, and source type of the contribution (in vs. out of state)
grouped_by_source_type = key_states.groupby(['RECIPIENT_STATE','PARTY','OUT_OF_STATE'])

#Breakdown of the number, total amount, and mean of in-state and out-of-state contributions by state and party
source_type_dem_rep_summary = grouped_by_source_type['AMOUNT'].agg(['count','sum','mean'])
print(f'Breakdown of the number, total amount, and mean of in-state and out-of-state contributions by state and party:\n{source_type_dem_rep_summary}')

#sorting by the key election state, Democrat or Republican, and contribution size (large or small)
grouped_by_size = key_states.groupby(['RECIPIENT_STATE','PARTY','SMALL_CONTRIBUTION'])

#Breakdown of the number, total amount, and mean of small and large contributions by state and party
size_dem_rep_summary = grouped_by_size['AMOUNT'].agg(['count','sum','mean'])
print(f'Breakdown of the number, total amount, and mean of small and large contributions by state and party:\n{size_dem_rep_summary}')

#%%
#finding the states that were the top contributors
grouped_by_source = key_states.groupby(['SOURCE_STATE','PARTY'])
source_state_sums = grouped_by_source['AMOUNT'].sum()
source_state_sums = source_state_sums.unstack('PARTY')
source_state_sums.fillna(0,inplace=True)
source_state_sums['TOTAL_AMOUNT'] = source_state_sums['DEM'] + source_state_sums['REP']

totals = source_state_sums['TOTAL_AMOUNT'].sort_values()
dem = source_state_sums['DEM'].sort_values()
rep = source_state_sums['REP'].sort_values()
print(f'\nTop Ten Source States of Overall Contributions in Key 2020 Senate Races:\n{totals[-10:]}')
print(f'\nTop Ten Source States of Democrat Contributions in Key 2020 Senate Races:\n{dem[-10:]}')
print(f'\nTop Ten Source States of Republican Contributions in Key 2020 Senate Races:\n{rep[-10:]}')

#%%
#finding the states that were the top recipients
grouped_by_source = key_states.groupby(['RECIPIENT_STATE','PARTY'])
recip_state_sums = grouped_by_source['AMOUNT'].sum()
recip_state_sums = recip_state_sums.unstack('PARTY')
recip_state_sums.fillna(0,inplace=True)
recip_state_sums['TOTAL_AMOUNT'] = recip_state_sums['DEM'] + recip_state_sums['REP']

totals = recip_state_sums['TOTAL_AMOUNT'].sort_values()
dem = recip_state_sums['DEM'].sort_values()
rep = recip_state_sums['REP'].sort_values()
print(f'\nSorted Overall Contributions in Key 2020 Senate Races:\n{totals}')
print(f'\nSorted Democrat Contributions in Key 2020 Senate Races:\n{dem}')
print(f'\nSorted Republican Contributions in Key 2020 Senate Races:\n{rep}')

#%%
###LOOKING AT THE FLOWS BETWEEN STATES
#looking at the flows between sources and recipients
grouped = key_states.groupby(['SOURCE_STATE','RECIPIENT_STATE','PARTY'])
flow_sums = grouped['AMOUNT'].sum()
flow_sums = flow_sums.unstack('PARTY')
flow_sums.fillna(0,inplace=True)
flow_sums['TOTAL_AMOUNT'] = flow_sums['DEM'] + flow_sums['REP']

totals = flow_sums['TOTAL_AMOUNT'].sort_values()
dem = flow_sums['DEM'].sort_values()
rep = flow_sums['REP'].sort_values()
print(f'\nTop Ten FLows of Overall Contributions in Key 2020 Senate Races:\n{totals[-10:]}')
print(f'\nTop Ten Flows of Democrat Contributions in Key 2020 Senate Races:\n{dem[-10:]}')
print(f'\nTop Ten Flows of Republican Contributions in Key 2020 Senate Races:\n{rep[-10:]}')

#%%
#making the flows per capita
flows = flow_sums.reset_index()
flow_pc = flows.merge(pop,on='SOURCE_STATE',how='right',validate='m:1')
flow_pc.set_index(['SOURCE_STATE','RECIPIENT_STATE'], inplace=True)
flow_pc['DEM_PC'] = flow_pc['DEM']/flow_pc['pop']
flow_pc['REP_PC'] = flow_pc['REP']/flow_pc['pop']
flow_pc['TOTAL_PC'] = flow_pc['TOTAL_AMOUNT']/flow_pc['pop']

totals_pc = flow_pc['TOTAL_PC'].sort_values()
dem_pc = flow_pc['DEM_PC'].sort_values()
rep_pc = flow_pc['REP_PC'].sort_values()
print(f'\nTop Ten FLows Per Capita of Overall Contributions in Key 2020 Senate Races:\n{totals_pc[-10:]}')
print(f'\nTop Ten Flows Per Capita of Democrat Contributions in Key 2020 Senate Races:\n{dem_pc[-10:]}')
print(f'\nTop Ten Flows Per Capita of Republican Contributions in Key 2020 Senate Races:\n{rep_pc[-10:]}')

#%%
###CREATING A HEATMAP
#first we are gonna drop the source states that don't include the 50 states plus DC and PR
trim = flow_sums.drop(['AA','AE','AP','AS','GU','MP','ZZ','VI'],axis='index')

#creating a heatmap variable of the flows
heatmap_overall = trim.drop(['DEM','REP'],axis='columns')
heatmap_dem = trim.drop(['TOTAL_AMOUNT','REP'],axis='columns')
heatmap_rep = trim.drop(['DEM','TOTAL_AMOUNT'],axis='columns')

#unstacking by recipient state to create a matrix
overall_grid = heatmap_overall.unstack('RECIPIENT_STATE')
dem_grid = heatmap_dem.unstack('RECIPIENT_STATE')  
rep_grid = heatmap_rep.unstack('RECIPIENT_STATE')
overall_grid = overall_grid['TOTAL_AMOUNT']
dem_grid = dem_grid['DEM']
rep_grid = rep_grid['REP']
overall_grid.fillna(0,inplace=True)
dem_grid.fillna(0,inplace=True)
rep_grid.fillna(0,inplace=True)

#%%
#making the heatmap for each 
fig,ax1 = plt.subplots(dpi=300)
fig.suptitle('Overall Contribution Flows From All States to Key States')
sns.heatmap(overall_grid,ax=ax1)
ax1.set_xlabel("Recipient State")
ax1.set_ylabel('Source State')
fig.tight_layout()
fig.savefig('key_contrib_overall_heatmap.png')

fig,ax1 = plt.subplots(dpi=300)
fig.suptitle('Democrat Contribution Flows From All States to Key States')
sns.heatmap(dem_grid,ax=ax1)
ax1.set_xlabel("Recipient State")
ax1.set_ylabel('Source State')
fig.tight_layout()
fig.savefig('key_contrib_dem_heatmap.png')

fig,ax1 = plt.subplots(dpi=300)
fig.suptitle('Republican Contribution Flows From All States to Key States')
sns.heatmap(rep_grid,ax=ax1)
ax1.set_xlabel("Recipient State")
ax1.set_ylabel('Source State')
fig.tight_layout()
fig.savefig('key_contrib_rep_heatmap.png')