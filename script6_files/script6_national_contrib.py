##Analyzing the contributions for all Senate races
#MWhitmoyer

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

merged = pd.read_pickle('all_states_pkl.zip')
pop = pd.read_csv('pop.csv')
pop = pop.rename({'STATE':'SOURCE_STATE'},axis='columns')

#%%
###ANALYZING BY CONTRIBUTION SOURCE AND SIZE

#sorting by the key election state, Democrat or Republican, and source type of the contribution (in vs. out of state)
grouped_by_source_type = merged.groupby(['RECIPIENT_STATE','PARTY','OUT_OF_STATE'])

#Breakdown of the number, total amount, and mean of in-state and out-of-state contributions by state and party
source_type_dem_rep_summary = grouped_by_source_type['AMOUNT'].agg(['count','sum','mean'])
print(f'Breakdown of the number, total amount, and mean of in-state and out-of-state contributions by state and party:\n{source_type_dem_rep_summary}')

#sorting by the key election state, Democrat or Republican, and contribution size (large or small)
grouped_by_size = merged.groupby(['RECIPIENT_STATE','PARTY','SMALL_CONTRIBUTION'])

#Breakdown of the number, total amount, and mean of small and large contributions by state and party
size_dem_rep_summary = grouped_by_size['AMOUNT'].agg(['count','sum','mean'])
print(f'Breakdown of the number, total amount, and mean of small and large contributions by state and party:\n{size_dem_rep_summary}')

#creating a scatter plot to visualize the amount of small and large contributions in each state and their relationship with party
#***Under Construction*** 

#%%
###FINDING THE TOP CONTRIBUTOR AND RECIPIENT STATES OVERALL AND BY PARTY
#finding the states that were the top contributors
grouped_by_source = merged.groupby(['SOURCE_STATE','PARTY'])
source_state_sums = grouped_by_source['AMOUNT'].sum()
source_state_sums = source_state_sums.unstack('PARTY')
source_state_sums.fillna(0,inplace=True)
source_state_sums['TOTAL_AMOUNT'] = source_state_sums['DEM'] + source_state_sums['REP']

totals = source_state_sums['TOTAL_AMOUNT'].sort_values()
dem = source_state_sums['DEM'].sort_values()
rep = source_state_sums['REP'].sort_values()
print(f'\nTop Ten Source States of Overall Contributions in 2020 Senate Races:\n{totals[-10:]}')
print(f'\nTop Ten Source States of Democrat Contributions in 2020 Senate Races:\n{dem[-10:]}')
print(f'\nTop Ten Source States of Republican Contributions in 2020 Senate Races:\n{rep[-10:]}')

#%%
#finding the states that were the top recipients
grouped_by_source = merged.groupby(['RECIPIENT_STATE','PARTY'])
recip_state_sums = grouped_by_source['AMOUNT'].sum()
recip_state_sums = recip_state_sums.unstack('PARTY')
recip_state_sums.fillna(0,inplace=True)
recip_state_sums['TOTAL_AMOUNT'] = recip_state_sums['DEM'] + recip_state_sums['REP']

totals = recip_state_sums['TOTAL_AMOUNT'].sort_values()
dem = recip_state_sums['DEM'].sort_values()
rep = recip_state_sums['REP'].sort_values()
print(f'\nTop Ten Recipient States of Overall Contributions in 2020 Senate Races:\n{totals[-10:]}')
print(f'\nTop Ten Recipient States of Democrat Contributions in 2020 Senate Races:\n{dem[-10:]}')
print(f'\nTop Ten Recipient States of Republican Contributions in 2020 Senate Races:\n{rep[-10:]}')

#%%
###LOOKING AT THE FLOWS BETWEEN STATES
#looking at the flows between sources and recipients
grouped = merged.groupby(['SOURCE_STATE','RECIPIENT_STATE','PARTY'])
flow_sums = grouped['AMOUNT'].sum()
flow_sums = flow_sums.unstack('PARTY')
flow_sums.fillna(0,inplace=True)
flow_sums['TOTAL_AMOUNT'] = flow_sums['DEM'] + flow_sums['REP']

totals = flow_sums['TOTAL_AMOUNT'].sort_values()
dem = flow_sums['DEM'].sort_values()
rep = flow_sums['REP'].sort_values()
print(f'\nTop Ten Flows of Overall Contributions in 2020 Senate Races:\n{totals[-10:]}')
print(f'\nTop Ten Flows of Democrat Contributions in 2020 Senate Races:\n{dem[-10:]}')
print(f'\nTop Ten Flows of Republican Contributions in 2020 Senate Races:\n{rep[-10:]}')
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
print(f'\nTop Ten FLows Per Capita of Overall Contributions in 2020 Senate Races:\n{totals_pc[-10:]}')
print(f'\nTop Ten Flows Per Capita of Democrat Contributions in 2020 Senate Races:\n{dem_pc[-10:]}')
print(f'\nTop Ten Flows Per Capita of Republican Contributions in 2020 Senate Races:\n{rep_pc[-10:]}')
print(len(flow_pc))

#%%
###CREATING A HEATMAP AND CREATING CSV FILES FOR MAPPING AND CHORD DIAGRAMS
#first we are going to drop the source states that don't include the 50 states plus DC and PR
###They would be less visually pleasing to map later as well
trim = flow_sums.drop(['AA','AE','AP','AS','GU','MP','PW','ZZ','VI'],axis='index')

#creating a heatmap variable of the flows
heatmap_overall = trim.drop(['DEM','REP'],axis='columns')
heatmap_dem = trim.drop(['TOTAL_AMOUNT','REP'],axis='columns')
heatmap_rep = trim.drop(['DEM','TOTAL_AMOUNT'],axis='columns')

#%%
#then we will create dfs of combined heatmap dfs and flow dfs to create comprehensive dfs for the chord diagrams
#it may seem unnecessary but helps the flow data be sorted a bit better
overall_pc = heatmap_overall 
overall_pc['SOURCE_POP'] = flow_pc['pop']
overall_pc['TOTAL_PC'] = flow_pc['TOTAL_PC']
d_pc = heatmap_dem 
d_pc['SOURCE_POP'] = flow_pc['pop']
d_pc['DEM_PC'] = flow_pc['DEM_PC']
r_pc = heatmap_rep 
r_pc['SOURCE_POP'] = flow_pc['pop']
r_pc['REP_PC'] = flow_pc['REP_PC']

#%%
#saving each combined setup to a CSV for use in the holoviews-bokeh extension flow diagram script so we can look at
#total amounts and per capita contribution amounts
overall_pc.to_csv('overall_flows.csv')
d_pc.to_csv('dem_flows.csv')
r_pc.to_csv('rep_flows.csv')

#we will save flow_pc to a csv to use in the mapping script
flow_pc.to_csv('all_states_trim.csv')

#%%
#unstacking by recipient state to create a grid
overall_grid = heatmap_overall.unstack('RECIPIENT_STATE')
dem_grid = heatmap_dem.unstack('RECIPIENT_STATE')  
rep_grid = heatmap_rep.unstack('RECIPIENT_STATE')
overall_grid = overall_grid['TOTAL_AMOUNT']
dem_grid = dem_grid['DEM']
rep_grid = rep_grid['REP']
overall_grid.fillna(0,inplace=True)
dem_grid.fillna(0,inplace=True)
rep_grid.fillna(0,inplace=True)

#*OPTIONAL*:reading the three dfs to files to use if you want to create a flow diagram via Chord or its paid version
overall_grid.to_csv('overall_grid.csv')
dem_grid.to_csv('dem_grid.csv')
rep_grid.to_csv('rep_grid.csv')

#%%
#filtering to just those flows with amounts over $500,000 so its a bit easier to see in the heatmap
t = (overall_grid > 500000).sum(axis='columns')
filtered_overall = overall_grid[t>0]
t = (dem_grid > 500000).sum(axis='columns')
filtered_dem = dem_grid[t>0]
t = (rep_grid > 500000).sum(axis='columns')
filtered_rep = rep_grid[t>0]

#%%
#making the heatmap for each 
fig,ax1 = plt.subplots(dpi=300)
fig.suptitle('Overall Contribution Flows From State to State')
sns.heatmap(filtered_overall,ax=ax1)
ax1.set_xlabel("Recipient State")
ax1.set_ylabel('Source State')
fig.tight_layout()
fig.savefig('all_contrib_overall_heatmap.png')

fig,ax1 = plt.subplots(dpi=300)
fig.suptitle('Democrat Contribution Flows From State to State')
sns.heatmap(filtered_dem,ax=ax1)
ax1.set_xlabel("Recipient State")
ax1.set_ylabel('Source State')
fig.tight_layout()
fig.savefig('all_contrib_dem_heatmap.png')

fig,ax1 = plt.subplots(dpi=300)
fig.suptitle('Republican Contribution Flows From State to State')
sns.heatmap(filtered_rep,ax=ax1)
ax1.set_xlabel("Recipient State")
ax1.set_ylabel('Source State')
fig.tight_layout()
fig.savefig('all_contrib_rep_heatmap.png')