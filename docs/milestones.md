# Milestones for SkiGenius

- [ ] **Milestone 1**:
  
  High level design with component specifications.

- [ ] **Milestone 2** (Low level design part 1):
  
  Decide on User inputs and other user related information we will be collecting (like current location)

- [ ] **Milestone 3**: 
  
   Decide on the features to be used for recommendation vectors and which ones for filtering.

   The features in the recommendation vectors will be compared with the user preferences and the top x similar vectors will be returned.

   Also TODO in this stage :

    - [ ] Decide on how many recommendations we should return (i.e the value of "x")
    - [ ] Should the filtering be applied on top of the recommended records or should we go with filter and then recommend?

- [ ] **Milestone 4**: 
 
  Data preprocessing and data vectorization.
  
  Primary owner: 
  
  TODO:
   - [ ] Cleaning and preprocessing
   - [ ] Finalize vectorization startegy
   - [ ] Generate vectors
   - [ ] Decide on DB schema i.e the structure of the mongoDB object, what fields should each object contain? 
  
- [ ] **Milestone 6**: 
  
    Setup the Database
    
    Primary owner: 
    
    TODO:
    - [ ] Setup instance on Atlas
    - [ ] Configure Data on the instance (there is an option to upload as CSV)
    - [ ] Setup Search Index (required for KNN beta and will speed up other search strategies as well)
    - [ ] Test connection to DB and write test cases for DB operations
  
- [ ]  **Milestone 7** (can be done in tandem with milestone 6): 
    
    Front end prototype/wireframes.
    
    Primary owner:

    TODO:
    - [ ] Decide basic structure of UI i.e pages, buttons, input methods
    - [ ] Implement filter functionality (front end)
    - [ ] Write test cases for each UI operation i.e are all the buttons and input methods working as expected, etc.
  
- [ ] **Milestone 8**: 
    
    Work on the processing module.
    
    Primary owner:

    TODO:
    - [ ] Implement functionality to query the DB and return the recommendations
    - [ ] Implement filter functionality on the backend
    - [ ] Test cases to check communication with front end
    - [ ] Test cases to check communication with DB
    - [ ] Test cases for filtering logic (tentative)

- [ ] **Milestone 9**:
    
    Preparing for demos.
    
    Primary owner:

    TODO:
    - [ ] Beta test the hosted version, if hosted. (Just check if all the features work as expected)
    - [ ] Prepare presentation slides
    - [ ] Finish up tool usage (and setup, if applicable) documentation

