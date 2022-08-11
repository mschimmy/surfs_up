# Surfs Up Analysis

## Overview of Analysis
The client, W. Avy, is an investor that will be using this analysis to determine if they will invest in the Surf n’ Shake business proposition, a shop selling surf boards and ice cream in Oahu, Hawaii.

### Purpose
Using a weather dataset for the island of Oahu,SQL, SQLAlchemy, and Python Pandas this analysis will produce temperature descriptive statistics for the months of June and December.

## Results

![June temperatures](https://github.com/mschimmy/surfs_up/blob/main/Resources/june_temps.png)

![December temperatures](https://github.com/mschimmy/surfs_up/blob/main/Resources/dec_temps.png)

The two tables above give the descriptive statistics for temperatures on the island of Oahu for the months of June and December.
- The average temperature difference between June and December is 3.903 degrees Fahrenheit, with June being slightly warmer than December.
- The standard deviation, which describes how spread out the data is, is larger for December than in June by 0.489 degrees Fahrenheit. This means that on average, December has a slightly larger variance in the temperature from day to day, though not by much.
- The most notable difference between the two months is their minimum temperature, with December having colder minimums by 8 degrees Fahrenheit

## Summary

Overall, the descriptive statistics for temperature in June and December are not drastically different. The most notable difference is in their minimum temperature values, with June being 8 degrees Fahrenheit warmer than December. In Oahu, December is a slightly colder month, has more variance in its day-to-day temperatures, and reaches temperatures that are lower than those in June.

Two additional queries that could be useful to the client include:
1. Plotting the temperature data for the two months to visually compare the two. This could be used to show trends that static descriptive statistics do not illustrate.
2. A second query that would be helpful is to determine the active stations that are collecting data, and seeing if these descriptive statistics change based on the station. This could be useful in determining where to open the Surf n’ Shake location on the island. 
