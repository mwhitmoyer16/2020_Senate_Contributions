#Prepping key states data for mapping in QGIS
#MWhitmoyer

import pandas as pd
import geopandas as gpd

#we are going to import all state so we can expand the mapping to other states if we want
all_states = pd.read_csv('all_states_trim.csv')
country = gpd.read_file('zip://tl_2020_us_state.zip') #this is just to be able to see it in the variable explorer

#creating dfs for each key state
ga = all_states.query("RECIPIENT_STATE =='GA'")
az = all_states.query("RECIPIENT_STATE =='AZ'")
ky = all_states.query("RECIPIENT_STATE =='KY'")
sc = all_states.query("RECIPIENT_STATE =='SC'")
#%%
#getting the share of democrat contributions, will use this to show how dem or rep a state is
ga['d_share'] = ga['DEM']/ga['TOTAL_AMOUNT']
az['d_share'] = az['DEM']/az['TOTAL_AMOUNT']
sc['d_share'] = sc['DEM']/sc['TOTAL_AMOUNT']
ky['d_share'] = ky['DEM']/ky['TOTAL_AMOUNT']

#%%
#reading them all to csvs
ga.to_csv('ga_party_contrib.csv',index=False)
az.to_csv('az_party_contrib.csv',index=False)
sc.to_csv('sc_party_contrib.csv',index=False)
ky.to_csv('ky_party_contrib.csv',index=False)
