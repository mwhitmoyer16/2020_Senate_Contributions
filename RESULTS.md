# Results and Discussion

The breadth and variety of this analysis can be a bit confusing at first but I 
believe I found a few insightful takeaways from this project.

### Key Findings and Lessons

1. Empirical Confirmation of Political Campaign Mythos
    
    When looking at both the heatmap and the chord diagrams the differences in flows by party is 
    striking at the national level and for the four key states. Republicans were spending a lot more
    and being more selective than Democrats. Republicans spent  spend differently than Republicans
       
        **Under Construction**
    
    
    
1. Suggestion of not too large a difference in type of contribution source or size by party

    When you look at the console output on contribution size and source types on both script6 and 
    script 7, no clear pattern for success based on solely these contributions emerges. Republicans
    had larger average contribution sizes for small and big contributions in all 4 key states. 
    
        **Under Construction**
    
1. Scale of outside spending in 2020 Senate elections

    The hypothesis when I started this analysis was that there would be more out-of-state
    contributions (in number and amount) than in-state ones, but the size of that
    difference surprised me. I saw a supermajority of contributions and overall money
    coming from out of state, especially in big elections like South Carolina's and Georgia's.
    However, I think it is important to point out that once I broke it down by state and not
    just outside states vs. election state, I found that the election state sometimes had
    the most contributions out of any single state. For instance, Georgia was the source of
    the most money going into its elections. 

1. Utility of chord diagrams and heatmaps
    
    Seeing the themes in Democrat vs. Republican spending would not have been possible without
    visualization tools like the heatmap. What was vague or hard to discern in pure numbers,
    was almost automatically self-evident in a heatmap in which I could see the scale, intensity,
    and precision of contributions by each party. The same goes the chord diagrams, with which any 
    person gets to easily see the complicated web of money flowing from state to state, and
    can see which states play the biggest roles in each party's politics. For instance, the intensity
    of contributions in DC was much clearer with a chord diagram than with dataframes or even maps or 
    heatmaps. Chords turn even the most daunting, computer-killing data files into approachable, 
    insightful visuals. I hope to explore them further because I think they will have a huge impact 
    on communicating policy and the realities of governance to the average person.

1. Opaqueness of PACs and Campaign Financing

    I kept the analysis to just contributions to candidate committees as it is hard
    to analyze PAC and other entities's contributions. In FEC data there is no
    code easily linking them to a specific candidate. There is definitely a significant
    amount of money going into to them though and by not having them, the power
    of this project is limited. It seems to me to be another example of how 
    campaign funding remains very distance from and non-transparent to the average
    person. Thankfully there are sites and institutions that analyze this info, 
    but there still remain many barriers and the FEC is sometimes a part of that. 
    I definitetly garnered a new appreciation for election data analysts and what
    transparent campaign finance should mean.

### Future/Optional Applications

A lot of different components went into this project and a lot of different avenues were explored as well
as left partially explored. It is my hope to continue to explore them and for others to as well. That is why
I made sure to leave partially explored components like in vs. out-of-state, contribution sizes, and flows per
capita in this project. Feel free to explore them more or do you own analysis based on candidate names or third 
parties maybe. There are a lot of great projects that could be done with this data, but unfortunately my time
and skills have constrained this analysis to just a few aspects of campaign finance.

Some suggestions:

    1. Including House races and comparing between Senate and House contribution patterns
    1. Using the Census API to add in demographic variables into your analysis
    1. Using Chord or Chord Pro to more easily create interactive and interesting chord diagrams
    1. Comparing these 2020 Senate contribution patterns to past years
    
The applications are limitless. So, I hope this depository is not too hard to understand and that it
helps shed some light on campaign finance and aid people in crafting their own analyses.