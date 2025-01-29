Admission Assistant for Nigerian Students
Table of Contents
Overview
Requirements
Setup
Usage
Example Use Cases
Contributing
License
Overview
This project aims to provide an admission assistant system for Nigerian students, helping them get admission into their preferred university or one assigned based on their JAMB score, state of origin, and residential address.

Requirements
Python 3.8+
Pandas
NumPy
Matplotlib (optional)
Setup
Clone the repository: git clone https://github.com/IDLEMONK/admission-assistant.git
Install required libraries: pip install -r requirements.txt
Update the config.json file with your API keys and database credentials
Usage
Run the application: python main.py
Provide the student's JAMB score, state of origin, and residential address
The system will suggest universities based on the student's eligibility
Example Use Cases
A student with a JAMB score of 250, from Lagos state, and residing in Abuja can be assigned to a university in the Federal Capital Territory (FCT)
A student with a JAMB score of 300, from Ogun state, and residing in Lagos can be assigned to a university in the South-West region
Contributing
Contributions are welcome! Please submit a pull request with your changes and a brief description of the changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Code Structure
config.json: Configuration file for API keys and database credentials
main.py: Entry point for the application
models.py: Data models for universities and students
utils.py: Utility functions for data processing and visualization
Commit Message Guidelines
Use the present tense (e.g., "Add feature" instead of "Added feature")
Keep the first line short and concise (less than 50 characters)
Use bullet points for multiple changes
API Documentation
University API
Student API
University API
GET /universities: Retrieve a list of universities
POST /universities: Create a new university
Student API
GET /students: Retrieve a list of students
POST /students: Create a new student
Database Schema
universities table:
id (primary key)
name
location
students table:
id (primary key)
name
jamb_score
state_of_origin
residential_address
