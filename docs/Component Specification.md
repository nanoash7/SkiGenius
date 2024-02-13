# Software Components

## User interface (View)
This component is responsible for handling user interactions with the tool. The User interface prompts the user to enter their preferences and filtering critieria. It will display the recommendations that fit the specified preferences. 

## Processing Module (Contoller)
This component is responsible for handling the business logic of the application. It forms a vector out of the user inputs received from the User interface component, forms a query and queries the database for similar vectors to the input vector. It receives the query result from the database and perfoms any neccessary processing before passing it back to the User Interface component. Aditionally it contains the logic for filtering and applies it to the results pre or post querying in order to return only the results relavant to the user's filters.

## Database (Model)
This component is the database containing the vectorized features of the ski resort information from our dataset. It is a database hosted on a free tier instance on MongoDB Atlas.

# Interactions


![Component Diagram](ComponentDiagram1.png)