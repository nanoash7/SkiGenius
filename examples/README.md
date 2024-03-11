# This file contains instructions on how to use this application

### Create and Activate a virtual environment using pip:
Windows Instructions:\
From the root directory, run "python -m venv venv" to create the virtual environment.\
From the root directory, run "venv/Script/Activate" to activate the virtual environment.

MacOS/Linux Instructions:\
<>

### Install the required packages for the application using pip:
Windows Instructions:\
From the root directory, run "pip install -r requirements.txt". This step might take some time...

MacOS/Linux Instructions:\
<>

### Running the streamlit application:
From the root directory, run "streamlit run src/frontend.py" to run the application.

### Running the test suite:
From the root directory, step into the src/ folder.\
From the src/ folder, run "coverage run -m unittest discover" to run the test suite.\
From the src/ folder, run "coverage report -m" to view the test suite's code coverage.

### Running the pylint linter:
From the root directory, run "pylint src" to run the linter on all of the source code.
