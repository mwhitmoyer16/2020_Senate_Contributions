#Creating the flow diagrams with Chord (OPTIONAL)
#MWhitmoyer

import pandas as pd
from chord import Chord

overall_grid = pd.read_csv('overall_grid.csv')
dem_grid = pd.read_csv('dem_grid.csv')
rep_grid = pd.read_csv('rep_grid.csv')

#%%
#creating a header list to both add extra 18 columns to dfs and create the names for our flow diagrams
header_list = ['AK','AL','AR','AZ','CA','CO','CT','DC',
               'DE','FL','GA','HI','IA','ID','IL','IN',
               'KS','KY','LA','MA','MD','ME','MI','MN',
               'MO','MS','MT','NC','ND','NE','NH','NJ',
               'NM','NV','NY','OH','OK','OR','PA','PR',
               'RI','SC','SD','TN','TX','UT','VA','VT',
               'WA','WI','WV','WY']

#reindexing the dfs with the header_list in order to add in new all zero columns to make a symmetrical matrix
overall = overall_grid.reindex(columns = header_list) 
dem = dem_grid.reindex(columns = header_list)
rep = rep_grid.reindex(columns = header_list)
overall.fillna(0,inplace=True)
dem.fillna(0,inplace=True)
rep.fillna(0,inplace=True)

#%%
#writing the dfs to lists so chord can read them
o_matrix = overall.values.tolist()
d_matrix = dem.values.tolist()
r_matrix = rep.values.tolist()

#%%
#makign the diagram
Chord(o_matrix,header_list,wrap_labels=False,padding=0.05,font_size_large="14px").to_html('overall_chord.html')
Chord(d_matrix,header_list,wrap_labels=False,padding=0.05,font_size_large="14px").to_html('dem_chord.html')
Chord(r_matrix,header_list,wrap_labels=False,padding=0.05,font_size_large="14px").to_html('rep_chord.html')

#%%
#example of edit you may want to make to the resulting html files on line 408 to make the flow diagram clearer
#w/o the edit it will refe to the flows 'instances' of occurrence btw two given states instead
#of dollars flowing from one to the other
 
tippy_content = "from <span style='font-weight:900'>" +
            Names[d.source.index] +
            "</span> to <span style='font-weight:900'>" +
            Names[d.target.index] +
            "</span><br> flowed <span style='font-weight:900'>" +
            d.source.value +
            "</span> dollars";