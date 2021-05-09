#formatting and merging the candidate and committee files from the FEC
#MWhitmoyer

import csv
import pandas as pd

#reading in the header files
fh = open("committees.csv",'w',newline='')
writer = csv.writer(fh)

com_head_reader = csv.reader(open('cm_header_file.csv'),quoting=csv.QUOTE_NONE)
for line in com_head_reader:
    writer.writerow(line)
    print(line)
#%%
com_raw = open('Committee_Master_2020.txt','r')
reader = csv.reader(com_raw,delimiter='|',quoting=csv.QUOTE_NONE)

for line in reader:
    print(line)
    writer.writerow(line)
    
fh.close()
#%%
#reading in the header files
fh = open("candidates.csv",'w',newline='')
writer = csv.writer(fh)

cand_head_reader = csv.reader(open('cn_header_file.csv'))
for line in cand_head_reader:
    writer.writerow(line)
    print(line)

cand_raw = open('Cand_Master_2020.txt','r')
reader = csv.reader(cand_raw,delimiter='|',quoting=csv.QUOTE_NONE)

for line in reader:
    print(line)
    writer.writerow(line)
    
fh.close()

#%%
#now that we have nice CSVs for both we are going to read them in as dataframes
#filter some columns and data out and merge them into one csv to merge with contributions

com_csv = pd.read_csv('committees.csv',dtype=str)
keep_vars = ['CMTE_ID','CMTE_NM','CMTE_ST','CMTE_TP','CAND_ID']
com_filtered = com_csv[keep_vars]
print(len(com_filtered))

cand_csv = pd.read_csv('candidates.csv',dtype=str)
is_senate = cand_csv['CAND_OFFICE'] == 'S'
is_2020 = cand_csv['CAND_ELECTION_YR'] == '2020'
keep = is_senate & is_2020
cand_csv_senate = cand_csv[keep]
keep_vars = ['CAND_ID','CAND_NAME','CAND_PTY_AFFILIATION','CAND_ELECTION_YR','CAND_OFFICE_ST','CAND_OFFICE']
cand_filtered = cand_csv_senate[keep_vars]
print(len(cand_filtered))
#%%
#merging com_csv and cand_csv together
com_cand = com_filtered.merge(cand_filtered,how='left',validate='m:1',indicator=True)
print('\nNumber of committees kept and dropped:\n',com_cand['_merge'].value_counts())

#keeping rows that are in both ie are senate races from 2020 with same candidate ID
good_ones = com_cand['_merge'] == 'both' 
com_cand = com_cand[good_ones == True] 
com_cand = com_cand.drop('_merge',axis='columns')
print(len(com_cand))#hoping for 80 here in this context
com_cand = com_cand.rename({"CAND_OFFICE_ST":"CAND_STATE"},axis='columns')


###This section is more just to take a look at the data. We will be aggregating by the 
###two major parties so it is not as important, but you could use these insights for a more 
###candidate-based analysis
#checking to make sure there are not multiple candidates for a committee
numcan = com_cand.groupby('CMTE_ID').size()
numcan1 = numcan > 1
print('\nHopefully zero:\n',numcan1)

#check to see if candidates have mulitple committees
print('\nNumber of Committees per Candidate:',com_cand['CAND_NAME'].value_counts())
#check to see what committe types they have
print('\nTypes of Committees Used:',com_cand['CMTE_TP'].value_counts())

#make a csv of the merge that will have a list of all the candidates and their
#respective committee IDs that we can then use to do a many to one merge for the contributions
com_cand.to_csv('com_cand.csv',index=False)

