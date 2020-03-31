<# Dumb Students Final Project

University of Illinois School Notifier

Note: The test descriptions can be found under test/integration.js

## Description

Students often have to reach out to many different sources to get information about their assignments,
lecture notes, and instructor assignments. It can be hard keeping track of all of this information from
multiple different sources. The goal of this app is to attempt to provide a single point of access
for all of your notification needs. This app will gather information from Blackboard and Piazza initially,
and if feasible will try to expand to also include Gradescope. <br />

It will also have a calendar, allowing you to see notifications in the order that they appear.
If available, it will access grading info so that you can see how you are faring in each of your classes.
We will also make it so that you can add your own notifications and notes.
This application will hopefully allow you to gather all the information you need for your day-to-day
school activities.

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
- User should be able to view notifications on a calendar, seeing when they were recieved
- Demonstrate ability to access Gradescope
- Attempt at scraping Blackboard data
- Show grading info for each course
- Test Cases for Checkpoint 4 in app/test_app.py:
  - To test Gradescope, the first test case would be to update credentials in the database. The test case is called
    test_register_gradescope_auth
  - Another test case would be to pull data from a specific class like the name of the class. The test case is called 
    test_className_gradescope_auth
  - Finally, the final test case would be to see all of the assignments from one class. The test case is called     
    test_contents_gradescope_auth
  - 
  - To test Piaaza, we would test to see if we are able to register within the app to login to Piaaza. The test case is called
    test_register_piazza_auth
  - Another test for Piaaza would be is to actually get the contents from the posts within Piaaza. The test case is called 
    test_contents_piazza_auth
  -
  - To further test the app, we would test to see if a username is already registered, that username should not be able to
    register again. The test case is called test_double_register_auth

## Deliverables for final project

- User should be able to add their own notifications/notes, making changes as needed
- User should be able to set up reminders and alarms for calendar events
- User should be able to see previews of some types of files attached to notifications

## Specialization deliverables

We are not specialized students.

# Installation

By the time you get to the end of the final project, this section should have a full set of
instructions for how to spin up your app.

To spin up our app, first run (docker-compose up --build) on the terminal and then go to (localhost:5000) to see the app.

To run the test cases, first run (docker-compose up --build) on one terminal window and then on another terminal window run 
(docker exec my_uni python -m unittest discover) to see the test cases run.
