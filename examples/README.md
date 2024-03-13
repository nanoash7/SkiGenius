# Instructions on how to use this application

### Application Demo
To view a brief demonstration of the application, view the SkiGeniusDemo.mp4 file located in this folder

### Create and Activate a virtual environment using pip:
Windows Instructions:\
From the root directory, run "python -m venv venv" to create the virtual environment.\
From the root directory, run "venv/Script/Activate" to activate the virtual environment.

MacOS/Linux Instructions:\
<>

### Install the required packages for the application using pip:
Windows Instructions:\
From the root directory with the virtual environment activated, run "pip install -r requirements.txt". This step might take some time...

MacOS/Linux Instructions:\
<>

### Setting up DB access:
To run the application locally you will either need to set up your own instance of the MongoDB database and put the URI to the
database in a .env file in the root or you will need access to the existing database.

#### Option 1 - Setting up your own DB and populating it:
To do this, head to https://cloud.mongodb.com (create an account if you don't have one already).
- Follow the steps given in this tutorial: https://www.mongodb.com/basics/mongodb-atlas-tutorial to set up a new cluster and a project. - Manage access to the project as required (there is an option to allow all IP addresses to access).
- In the "Generating Database Connection String" step from the tutorial, select driver to be Python and the appropriate version.
- The dialog box will provide you with the URI. Make sure to replace the "Username" and "Password" fields with the appropriate data.
- Copy this URI. Create a .env file in the root directory of this project. Set MONGO_URI to the URI from the previous step
- Now you are ready to populate this database! By default the code is set up to call the database "ski_info" with a collection named "resorts"
- To populate the database:
``` cd src ```
``` python -m scripts.init_db ```
- The previous step should generate execution logs. Check the logs to see if the connection and insertion to the db is successful
- Once you've confirmed the connection and insertion is successful, you are ready to start querying the database!

#### Option 2 - Accessing the existing database:
- If you happened to require access to the database that is already set up, you will need a secret key. You will have to contact the repo owners/maintainers (@nanoash7, @Chakita, @ksorstokke2, @kylebreth) if you need access to this.
- If you have received a secret key from us, head over to https://www.devglan.com/online-tools/text-encryption-decryption
- Enter the following text in the "Text Decryption" entry box:
```
CXxYrqoVJybWWozmds8TLiUOBgJkAVsfDW+F6izwbC2h4WpZl+nD9vhSVJRds+utuBj5h15dMouE4UbYdAS16SZnLejzHhHNeAsRbwo3Ux1Vy5CtHOrtCdCjuvHnnxswBfR5yvxjH5Hmr0JAGn5R/w==
```
- Check the "Decryption requires a custom secret key" option
- Enter the secret key provided to you. This should show you the decrypted URI
- Copy the decrypted URI. Create a .env file in the root directory of the project and paste the decrypted text into it.
- You are good to go with querying the database now!


### Running the streamlit application:
From the root directory with the virtual environment activated, run "streamlit run src/frontend.py" to run the application.

### Running the test suite:
From the root directory with the virtual environment activated, step into the src/ folder.\
From the src/ folder, run "coverage run -m unittest discover" to run the test suite.\
From the src/ folder, run "coverage report -m" to view the test suite's code coverage.

#### Exclusions from testing:
The scripts folder do not have any test cases associated with them. This is because they contain one-time usage code that is only
needed to get the DB up and running.

### Running the pylint linter:
From the root directory with the virtual environment activated, run "pylint src" to run the linter on all of the source code.
#### Some exclusions from the linter:
- We disabled the linting for relative imports of modules from our codebase due to a known pylint bug - https://github.com/pylint-dev/pylint/issues/3984
- Ignoring the duplicate code warning in test_query_generator.py since we are only creating a pipeline to test if it is as expected.
