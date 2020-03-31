# Dumb Students Final Project

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

## Deliverables for checkpoint 4

- Make sure data is validated
- User should be able to filter out data as desired
- User should be able to view notifications on a calendar, seeing when they were recieved
- Demonstrate ability to access Blackboard API
- Attempt at scraping Gradescope data
- Show grading info for each course

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
