# SkiGenius

### Access the Application
Ski Genius is hosted through the streamlit community cloud resource at https://skigenius.streamlit.app/

### How To Use This Application Locally
See the examples folder in the root directory of this repository for how to use this app on your local system.

### Workflow Report
![Coverage Status](https://coveralls.io/repos/github/nanoash7/SkiGenius/badge.svg?branch=main)\
![badge_test](https://github.com/nanoash7/SkiGenius/actions/workflows/build_test.yml/badge.svg)

### Project Type:
Recommendation and Planning Tool

### Questions of Interest:
How does snow quality, location, seasons, ownership company, etc. affect prices?
What resorts are catered towards beginner, intermediate, and advanced visitors
Can our data be used to predict crowd sizes and help people avoid long lines?

### Project Goals:
Help skiers determine where to ski (daily outings and bigger trips).
Compare snow quality and amount of snow between ski resorts.
Provide recommendations based on skill level, budget, and location preferences.


### Data Sources:
https://www.kaggle.com/datasets/ulrikthygepedersen/ski-resorts?select=resorts.csv
http://ski-resort-stats.com/find-ski-resort/#1498675249678-9966e624-d30e
https://www.kaggle.com/code/beaubellamy/ski-resorts
https://www.nsaa.org/NSAA/Media/Who_Owns_Which_Mountain_Resorts.aspx

### Exclusions from testing:
The scripts folder do not have any test cases associated with them. This is because they contain one-time usage code that is only
needed to get the DB up and running.

### Some exclusions from the linter:
- We disabled the linting for relative imports of modules from our codebase due to a known pylint bug - https://github.com/pylint-dev/pylint/issues/3984
- Ignoring the duplicate code warning in test_query_generator.py since we are only creating a pipeline to test if it is as expected.


