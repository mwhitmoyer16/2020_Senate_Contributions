#Converting the contribution file from the FEC to CSV
#MWhitmoyer

import csv
#contribution file: pickling could help
###filter out some of the columns, filtered out by year, filter by senate
###figure out number for race indicator, write if line[#] == 'S, limited loop first
fh = open("contrib2020.csv",'w',newline='')
writer = csv.writer(fh)

contrib_head_reader = csv.reader(open('contrib_header_file.csv'),quoting=csv.QUOTE_NONE)
for line in contrib_head_reader:
    writer.writerow(line)
    print(line)
#%%
contrib_raw = open('contributions2020.txt','r')
reader = csv.reader(contrib_raw,delimiter='|',quoting=csv.QUOTE_NONE)
#filtering out contributions that are only for the 2020 Primary and General Elections
for line in reader:
    if line[3] == 'G2020':
        writer.writerow(line)
    elif line[3] == 'R2020':
        writer.writerow(line)
    elif line[3] == 'S2020':
        writer.writerow(line)
    elif line[3] == 'P2020':
        writer.writerow(line)
fh.close()


