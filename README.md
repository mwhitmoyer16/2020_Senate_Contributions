# 2020 Senate Election FEC Contributions Analysis

### Overview

This analysis is a 9-script (plus 1 optional) assessment of FEC campaign contributions in the 2020 Senate Elections. 
The project looks at differences between the two major parties in amount of contributions and money as well as 
large and small contributions and in v. out-of-state contributions. Overall, it seeks to discover contributions trends
and give a more system-level view of campaign contributions. This is mainly realized via heatmaps and chord diagrams 
to analyze the flows of money in all 2020 Senate races as well as mapping and chord diagrams of contributions for four
highly publicized Senate races in Arizona, Georgia, South Carolina, and Kentucky.

An important part of this analysis is that it offers opportunities to build off of it and perform various analyses
of your choosing. So feel free to use the files produced by this scripts or to modify the scripts 
to do your own analyses on different aspects of the 2020 Senate contributions. 

### Getting the Data

To get the input data for the first two scripts you will need to download 3 main files from the FEC website via their bulk data download 
at https://www.fec.gov/data/browse-data/?tab=bulk-data

You can click on the 2019-2020 option for 'Contributions by individuals', 'Candidate Master', and 'Committee Master.'
For each file you will also need to download the header file that is also with it on the page.

Download may take a bit and reading them into and then processing them in the first few scripts will take some time.
If they are taking too long (over 10 minutes or so) you should cancel the process and see if something is wrong. For
the most part, you should expect slow reading and processing times for the files in most of this project due to the 
large size of the FEC files.

You will also want to download a TIGER shape file for the US map for script9. That can be found and downloaded
by choosing "2020" and "States (and equivalent" from the Census Bureau at https://www.census.gov/cgi-bin/geo/shapefiles/index.php

### The Process and Outputs

In general, the scripts could be run in order by their number (i.e. Script1, Script2,...). Script4 though can be run
at any point before it is needed for Script6 and onwards. As well, if you want to map the contributions before you create 
the chord/flow diagrams feel free to. There should be 8 python scripts for Spyder or a similar text editor, 1 ipynb file 
to be run in JupyterLab for the chord diagrams, and an optional python script if you want to use or pay for Chord to 
create some chord diagrams in html.

There will be various intermediate pickles and CSV files produced throughout the process that will be used to 
construct the visualizations. So, if you do change up the order of the scripts or even reorganize the depository,
you may have to edit the paths for the input files for some or all scripts.

For script8 you will have to switch to JupyterLab in order to open the ipynb file properly and to generate the chord
diagrams.

By the end of script8, you should have 9 chord diagrams for the overall Senate contributions as well as by each major 
party for all the Senate races as well as absolute and per capita ones for the four key states chosen for this analysis.
You should also get 6 heatmaps that help articulate the contributions patterns of states and parties in all the Senate 
races as well as the four key states.

Then, you can take the outputs of script9 to create various maps displaying similar info for all four key states,
highlighting the absolute amounts, the intensity of contributions (the per capita amounts), and the party breakdown 
of contributions coming from other states to each key state. This can be achieved by joining the 4 CSVs with the shp 
file for the US. Make sure to cut out Alaska, Hawaii, and the other US island territories in order to make the maps 
tighter and clearer. Also, add pie charts for each state and use 'DEM' and 'REP' as the attributes in order to roughly
see both the contribution flows and their party breakdowns for each state. You should end up with 12 maps (3 kinds for
each key state) in a qgz file called 'key_states'.

Further, there will also be various outputs in the console of summary data in the scripts (especially 6 and 7), that 
will help shed some light on in vs. out-of-state contributions and small vs. large contributions. They will also 
support and hopefully help clarify some of the data going into the visualizations that are the main output 
of this analysis.




