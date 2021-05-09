#Formatting the contributions csv
#MWhitmoyer

###Most of the actions in this file will take some time
###to complete because of the size of the file but will
###be easier to do in subsequent files after we pickle

import pandas as pd

#creating Pandas dataframe and trying to cut out some ofthe unnecessary columns
raw = pd.read_csv("C:/Users/mswhi/Documents/Advanced Project/Script2_Files/contrib2020.csv",dtype=str)   
contrib_raw = pd.DataFrame(raw, columns= ['CMTE_ID','TRANSACTION_PGI','ENTITY_TP','STATE','ZIP_CODE','TRANSACTION_DT','TRANSACTION_AMT'])
n_now = len(contrib_raw) 
print('\nNumber of records read:',n_now)

##editing and filtering the dataframe for individual contributions
#editing contrib_raw dataframe columns
contrib_raw = contrib_raw.rename({"TRANSACTION_PGI":"PGI"},axis='columns')

#editing the date info
ymd = pd.to_datetime(contrib_raw["TRANSACTION_DT"],format="%m%d%Y")
contrib_raw['DATE'] = ymd.dt.to_period('M')

#filtering out for contributions before 2019 and not for the General
n_last = n_now
year_ok = ymd.dt.year >= 2019
contrib = contrib_raw[year_ok == True]
n_now = len(contrib)
print('\nNumber of records dropped by filtering for 2019:',n_last-n_now)

n_last = n_now
contrib = contrib.query("PGI == 'R2020' or PGI == 'G2020' or PGI == 'S2020'" )
n_now = len(contrib)
print('\nNumber of records dropped by filtering for election type:',n_last-n_now)
print('\nNumber of records in contrib after filtering:',n_now)

##editing the zipcodes down to 5 digits
#counting lengths of zipcodes
zip_all = contrib['ZIP_CODE']
ziplen = zip_all.str.len()
print(ziplen.value_counts(dropna=False))

#sorting out 9 and 5 length zips
zip_9 = ziplen==9
zip_5 = ziplen==5
zip_ok = zip_5 | zip_9
zip_bad = -zip_ok

#making a column for all 5 length zips
zip5 = zip_all.copy()
zip5[zip_9] = zip5[zip_9].str[:5]
zip5[zip_bad] = None
zip5len = zip5.str.len()
print('\n')
print(zip5len.value_counts(dropna=False))
contrib['5_DIGIT_ZIP'] = zip5
print('\nCheck of columns in contrib:\n',list(contrib.columns))

#%%
#pickling the contrib dataframe
contrib.to_pickle('contrib_pkl.zip')



