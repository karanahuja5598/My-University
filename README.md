## Dumb Students Final Project

University of Illinois School Notifier

Note: The test descriptions can be found under app/test_app.py

## Description

Students often have to reach out to many different sources to get information about their assignments,
lecture notes, and instructor assignments. It can be hard keeping track of all of this information from
multiple different sources. The goal of this app is to attempt to provide a single point of access
for all of your notification needs. This app will gather information from Gradescope and Piazza initially,
and if feasible will try to expand to also include Blackboard. <br />

## Authors

| Member | Web dev level | Specialization |
| --- | --- | --- |
| Aashish Agrawal | web programming novice | |
| Karan Ahuja | web programming novice | |

## Deliverables for checkpoint 2

- Demonstrate ability to access unofficial Piazza API
- Store any pulled data from APIs into MongoDB database
- Pull data from database and represent it as a dynamically updated web view
- Have a test suite for making sure database can perform CRUD operations

## Deliverables for checkpoint 3
- Inside app/test_app.py
- Test Cases that passed for our App:
  - test_index_unauth
  - test_login_unauth
  - test_register_unauth
  - test_register_auth
  - test_register_login_auth

## Deliverables for checkpoint 4

- Make sure data is validated
- User should be able to filter out data as desired
- Demonstrate ability to access Gradescope
- Attempt at scraping Blackboard data
- Show grading info for each course from Gradescope
- Inside app/test_app.py
- Test Cases that passed for our App:
   - test_register_piazza_auth
   - test_contents_piazza_auth
   - test_register_gradescope_auth
   - test_contents_gradescope_auth
   - test_className_gradescope_auth

## Deliverables for Checkpoint 5
- Specific Deliverables for Checkpoint 5
  - Will establish a fully implemented scraper for Blackboard
  - Have a fully completed test suite for the app
  - Make the app more appealing by adding templates that make it more colorful
- Final Test List located in app/test_app.py
  - The tests will be more focused towards Blackboard as that is the last thing that is left to be implemented
  - The first test will be testing if the credentials for logging in to Blackboard work properly, this test case is called     test_register_blackboard_auth
  - The second test will be testing to see if the list of recent activity from Blackboard can be accessed properly, this test case is called test_contents_blackboard_auth

## Specialization deliverables

We are not specialized students.

# Installation

To spin up our app, first run (docker-compose up --build -d) on the terminal and then go to (localhost:5000) to see the app.
Then to turn off the container, run the command docker-compose down.

To run the test cases, first run (docker-compose up --build -d) on the terminal and then run the commmand (docker exec my_uni python -m unittest discover) to see the test cases run. After that to turn off the container, run the command 
(docker-compose down).
