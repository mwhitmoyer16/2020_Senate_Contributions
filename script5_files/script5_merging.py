#Merging and filtering the committee/candidate and contributions files
#MWhitmoyer

import pandas as pd

#reading in the files for candidates/committees and contributions to Senate General Elections in 2020
com_cand = pd.read_csv('C:/Users/mswhi/Documents/Advanced Project/Script1_Files/com_cand.csv')
contrib = pd.read_pickle('C:/Users/mswhi/Documents/Advanced Project/Script3_Files/contrib_pkl.zip') 

#%%
###MERGING AND FILTERING THE FINAL BIG DATAFRAME
#merging the read in dataframes on committee IDs
merged = contrib.merge(com_cand,on='CMTE_ID',how='inner',validate='m:1')
merged['AMOUNT'] = merged['TRANSACTION_AMT'].astype(float)
merged_len = len(merged)
merged = merged.rename({'CAND_PTY_AFFILIATION':'PARTY','STATE':'SOURCE_STATE','CAND_STATE':'RECIPIENT_STATE'},axis="columns")
print(f'\nNumber of Contributions Overall:\n{merged_len}')
cand_values = merged['CAND_NAME'].value_counts()
print(f'\nNumber of Contributions by Candidate:\n{cand_values}')
party_values = merged['PARTY'].value_counts()
print(f'\nNumber of Contributions by Party:\n{party_values}')

#filtering out third parties and checking how the dataframe changed because their contributions
#are neither large nor the focus of this analysis
merged = merged.query("PARTY == 'DEM' or PARTY == 'REP'")
merged_len = len(merged)
print(f'\nNumber of Contributions Overall to Two Major Parties:\n{merged_len}')
cand_values = merged['CAND_NAME'].value_counts()
print(f'\nNumber of Contributions by Major Party Candidate:\n{cand_values}')
    #the small number of contributions to other candidates in the two parties are from 
    #leftover contributions from the primaries
party_values = merged['PARTY'].value_counts()
print(f'\nNumber of Contributions by Major Party:\n{party_values}')

#%%
###ADDING IN SOURCE AND SIZE OF CONTRIBUTIONS COLUMNS
#just so you can look at them for reference without having to wait for the variable to open in the variable explorer
print(merged.columns) 

#setting up a boolean to mark if contributions are from in or out of state
outside = merged['RECIPIENT_STATE'] != merged['SOURCE_STATE']

#will add a column to merged where out of state contributions are True and in state are False
merged['OUT_OF_STATE'] = outside 

#setting up a boolean to mark if contributions are from in or out of state
small = merged['AMOUNT'] <= 200

#will add a column to merged where out of state contributions are True and in state are False
merged['SMALL_CONTRIBUTION'] = small 

#%%
#editing and sending the merged file to a pickle for use in the next scripts
merged.to_pickle('all_states_pkl.zip')

key_states = merged.query("RECIPIENT_STATE == 'KY' or RECIPIENT_STATE == 'GA' or RECIPIENT_STATE == 'SC' or RECIPIENT_STATE == 'AZ'")
key_states.to_pickle('key_states_pkl.zip')

#%%
 ###look at g23 to see that thing to get rid of negative contributions
                #grouping contributions by zipcode and party
                    grouped = pa.groupby(['zip','party'])
                    amount = grouped['amt'].sum()
                    amount = amount.where(amount>0,0)
                    wide = amount.unstack(level='party')
                    wide.fillna(0,inplace=True)
                    wide['total'] = wide.sum(axis='columns')
            
            #column for small or large donor
            ###talk to wilcoxen
            print(merged['TRANSACTION_AMT'].value_counts())
            if merged["TRANSACTION_AMT"] >= 200:
                return merged["DONOR_TYPE"] == 'Large'
                elif:
                    return merged["DONOR_TYPE"] == 'Small'
            merged["DONOR_TYPE"] = 
            