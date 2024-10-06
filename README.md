GitHub Actions Workflow

This project utilizes GitHub Actions to automate the testing of the Flask application. The workflow runs on every push and pull request to the `main` branch, ensuring that all tests are executed in a consistent and automated manner.

Folder structure


├── .github/                   GitHub Actions configurations
│   └── workflows/
│       └── main.yml          GitHub Actions workflow file
├── venv/                      Virtual environment folder (optional)
├── app.py                     Flask application file
├── requirements.txt           File for Python dependencies
├── test_app.py                Test file for the Flask application
|── README.md                  Project documentation


study basics of yml
   - https://dev.to/sre_panchanan/hello-world-in-github-actions-a-beginners-guide-to-your-first-workflow-1mbh#:~:text=How%20to%20Set%20Up%20A%20Github%20Action%20CI,to%20define%20your%20CI%20workflow%20to%20trigger%20events.

   - https://www.geeksforgeeks.org/run-python-script-in-github-actions/

Steps
   - created app.py 
   - created test_app.py for testing
   - created requrirments.txt for installing dependencies for the project containing app.py
   - set up main.yml inside .github/workflows
   - Checkout Code : The workflow uses the 'actions/checkout@v2' action to pull the latest code from the repository.
   - Set Up Python : The 'actions/setup-python@v4' action sets up the specified Python version 
   - Install Dependencies : A virtual environment is created, and the required packages are installed from 'requirements.txt'.
   - Run Tests : The 'pytest' framework is used to run the test suite defined in 'test_app.py'.


Workflow Overview

The GitHub Actions workflow is saved inside 'github/workflows/main.yml' file. The main step of the workflow are as follows:

Trigger Events
   - The workflow is triggered on every 'push'  event for the 'main' branch.




