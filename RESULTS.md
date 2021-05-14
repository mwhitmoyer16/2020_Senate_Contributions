# Results and Discussion

The breadth and variety of this analysis can be a bit confusing at first but I believe I found a few 
insightful takeaways from this project.

### Key Findings and Lessons

1. Empirical Confirmation of Political Campaign Mythos and Trends
    
    When looking at both the heatmap and the chord diagrams the differences in flows by party is 
    striking at the national level and for the four key states. Republicans were spending a lot more
    and being more selective than Democrats. Georgia is key in showing this as Republican contributions
    flowing into the state were almost double that of Democrats. On the heatmaps, we can see Republicans
    donating more overall as well as sending a plurality of their money to GA while the Democrats seem to
    spread it out a bit more, focusing on SC and GA more equally. I do not have PAC and other spending data
    though, nor do I have first few days of 2021 spending in GA so it is hard to see how the totality of 
    contributions came out in that state. From this data though, it looks like Republicans were putting up a
    lot more than Democrats and were a lot more concerted in their effort. This mirrors the campaign lore of 
    Democrats suffering at winning campaigns, due to a number of reasons including idealism, a reluctance to
    engage in some forms of machiavellian rhetoric and tactics, relatively poor fundraising infrastructure,
    and challenges their base faces in making contributions and staying engaged. The same lore paints Republicans
    as skilled at fundraising, turning out their base, and fortunate in having many large private and corporate donors.
    Many of the causal reasons are many times more hearsay and rhetoric, but at least in the data for this election
    we do see a more focused Republican effort and more overstretched Democrat effort, which may best be accounted for 
    by the Republicans' defensive position in this elections (trying to keep the Senate) and the Democrats' all-out 
    approach as they felt energized to take back the White House and the Senate. 
    
    Yet money does not equal votes necessarily, so we see Republicans outdonating Democrats in absolute terms in GA 
    and to a lesser extent AZ and losing both races, while being outdonated by Democrats in SC and KY and still winning.
    It is just another example of the tried and true principle of political campaigns that money is not everything.
    Determining what really earns victories at the ballot box has been a question of research since before this
    country came to be and probably after it ceases to exist, so this analysis was never trying to get there. Still,
    it is fascinating to have these visualization tools to see just how much money and, by virtue of that, effort and
    economic power go into these races.
    
    This analysis does help us shed some light though on what the New South battlegrounds will look like as SC and GA
    were the top recipients of contribution dollars of all 34 recipient states. We will continue to see Democrats
    reaching to add them and Republicans sending massive amounts of money to keep them. 
    
    Finally, one note on the power of DC in politics. It was not until I made the final per capita chord diagrams
    that I noticed something interesting. CA's size shrank dramatically and DC's exploded, for both parties. It may
    not contribute the top amounts of money in absolute terms, but it punches well above its weight class. The amount
    of politically-involved/interested individuals in DC is monumental, and it is thought provoking to see a district
    that remains without statehood and representation of its own in the Senate play such an outsized role in the 
    financing of our Senate elections.
    
    
1. Suggestions from the Type of Contribution Source and its Size by Party

    This is an area I unfortunately did not get to explore as much as I wanted to and hope to in the
    future. However, I did see some interesting things to note in the data. When you look at the console
    output on contribution size and source types on both script6 and script 7, no clear pattern for success
    based on solely these contributions emerges. 
    
    Yet they may work to gauge how party contributors felt about the races. Republicans had larger average contribution
    sizes for large contributions in all 4 key states. The gap between the average large contribution (a contribution 
    over $200 that is), however, was much greater in AZ and GA, paralleling what generally seemed to be the two states
    Republicans cared about the most. Further displaying this is the fact that in Georgia the average large contribution
    was almost double that of Democrats and Republicans had a greater number and total amount of contributions going into
    the state than Democrats during this time period. Meanwhile in AZ, Democrats did out do Republicans in the number of
    large contributions sent to the state. The small contribution do not reveal any clear trends though. It seems the 
    data more helps to quantify what the donor and political class (sometimes the same) of the Republican Party felt 
    intensely about more so than the small donors. The small gaps in the other two states, just like the heatmaps, serve
    to show again how Republicans focused a lot more narrowly in their donations and Democrats spread it across the board.
    
    
1. Scale of Outside Spending in 2020 Senate Elections

    The hypothesis when I started this analysis was that there would be more out-of-state
    contributions (in number and amount) than in-state ones, but the size of that
    difference surprised me. I saw a supermajority of contributions and overall money
    coming from out of state, especially in big elections like South Carolina's and Georgia's.
    However, I think it is important to point out that once I broke it down by state and not
    just outside states vs. election state, I found that the election states sometimes had
    the most contributions out of any single state. For instance, Georgia was the source of
    the most money going into its elections. As well, the contributions per capita helped me 
    see how intensely the elections mattered in their own states as each of the four key states
    had the highest per capita contributions in their respective races.
    

1. Utility of Chord Diagrams and Heatmaps
    
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

    I kept the analysis to just contributions to candidate committees as it is hard to analyze PAC and other
    entities's contributions. In FEC data there is no code easily linking them to a specific candidate. There 
    is definitely a significant amount of money going into to them though and by not having them, the power
    of this project to reflect all the money going into these races is limited. It seems to me to be another
    example of how campaign funding remains very distance from and non-transparent to the average person. 
    Thankfully there are sites and institutions that analyze this info, but there still remain many barriers 
    and the FEC is sometimes a part of that. I definitetly garnered a new appreciation for election data analysts 
    and what transparent campaign finance should mean.


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
    1. Creating a scatter plot and other figures to see the relationship between in and out-of-state contributions 
       and party
    
The applications are limitless. So, I hope this depository is not too hard to understand and that it
helps shed some light on campaign finance and aid people in crafting their own analyses.