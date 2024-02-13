# Background

SkiGenius is a recommendation tool to help skiers determine where to ski (daily outings and bigger trips). SkiGenius allows users to compare snow quality and amount of snow between ski resorts and provide recommendations based on skill level, budget, and location and other preferences.

# User profile

## User 1: This is Kyle Johnson

### User Stories

**Wants**: Kyle wants to use our tool to decide which of the local ski areas to visit for a daytrip\
**Interaction methods**: Kyle will interact with the tool through the user interface on the web\
**Needs**: Access to the web interface\
**Skills**: We should assume general computer skills, but nothing particularly beyond that

### Use cases

**User**: Access webpage for tool\
**System**: Display options for Kyle to enter ski area preferences\
**User**: Selects desired options\
**System**: Shows a list and map of the top 5 ski areas sorted by how well they match Kyle’s preferences\
**User**: Select/Hover for more information\
**System**: Displays summary of snow report, forecast, price\
**(Implicit)** Filter based on price, location, facilities?


## User 2: Geoff Calhoun III

### User Stories

**Who**: Wall street stockbroker visiting from New York\
**Wants**: Week-long ski vacation with his old frat brothers\
**Interaction methods**: Uses the UI of the website to get recommendations of ski-resorts that fit the criteria he is looking for\
**Needs**: Access to the web interface\
**Skills**: Stock trading, disposable income, general computer skills, really good with powerpoint\

### Use cases

User: Access webpage for tool\
System: Display options for Geoff to enter ski area preferences\
User: Selects desired options\
System: Shows a list and map of the top 5 ski areas sorted by how well they match Geoff’s preferences (includes resort name, snow summary, estimated trip price)

## User 3: This is Kayil 

### User Stories

**Who**: Kayil is an analyst working at BlahBlahBlah ski resort\
**Wants**: Kayil would like to see data on who is searching for resorts similar to BlahBlahBlah, see search trends for when their resort is popular (and under what conditions), in order to advertise to these people\
**Interaction methods**: Kayil will be getting user data from a database of tool searches\
**Needs**: Kayil needs access to the search database, resort comparisons\
**Skills**: Kayil has a lot of coding and technical experience\

### Use cases

User: Access webpage for tool\
System: Display options for Geoff to enter ski area preferences\
User: Selects desired options\
System: Shows a list and map of the top 5 ski areas sorted by how well they match Geoff’s preferences (includes resort name, snow summary, estimated trip price)


# Data Sources

- https://www.kaggle.com/datasets/ulrikthygepedersen/ski-resorts?select=resorts.csv 
- http://ski-resort-stats.com/find-ski-resort/#1498675249678-9966e624-d30e 
- https://www.kaggle.com/code/beaubellamy/ski-resorts
- https://www.nsaa.org/NSAA/Media/Who_Owns_Which_Mountain_Resorts.aspx 
