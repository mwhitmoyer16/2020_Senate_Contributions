#Creating a population csv for all the states to create a pop column for the 
#coming dataframes
#MWhitmoyer

import pandas as pd
import requests

#setting up the api request
api = 'https://api.census.gov/data/2018/acs/acs5'

for_clause = 'state:*'

key_value = 'a6c1d09a53f26ed2b244bdd968cd4fcf3312ede5'

payload = {'get':"NAME,B01001_001E",'for':for_clause,'key':key_value}

response = requests.get(api,payload)
if response.status_code == 200:
    print('\nRequest Successful')
else:
    print(response.status_code,'\n',response.text)
    assert False

#taking advantage of JSON to make a dataframe
row_list = response.json()
colnames = row_list[0]
datarows = row_list[1:]

pop = pd.DataFrame(columns=colnames,data=datarows)

#editing and merging pop with pocodes
new_names = {"B01001_001E":"pop"}
pop = pop.rename(new_names,axis='columns')

po = pd.read_csv('pocodes.csv')
po = po.rename({'Name':'NAME','PO':'STATE'},axis='columns')
pop = pop.merge(po,on='NAME',how='inner',validate='m:1')
pop = pop.drop(['NAME','state'],axis='columns')

pop.to_csv('pop.csv',index=False)
