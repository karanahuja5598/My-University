# Dumb Students Final Project

University of Illinois School Notifier

## Description

TODO: An English language description of what your application does, intended for a developer
audience. Pretend this is the real `README.md` for your app that will show up on GitHub: what do you
want people to know about it? What does it do? Why should they use it/check it out/hack on it? This
should be approximately two paragraphs. Take a look at the description of your favorite software
repository for inspiration.

Students often have to reach out to many different sources to get information about their assignments,
lecture notes, and instructor assignments. It can be hard keeping track of all of this information from
multiple different sources. The goal of this app is to attempt to provide a single point of access
for all of your UIC notification needs. This app will gather information from Blackboard and Piazza initially,
and if feasible will try to expand to also include Gradescope. <br />

It will also have a calendar, allowing you to see notifications in the order that they appear.
If available, it will access grading info so that you can see how you are faring in each of your classes.
We will also make it so that you can add your own notifications and notes.
This application will hopefully allow you to gather all the information you need for your day-to-day
school activities.



## Authors

TODO: List group members, each group member must EITHER be marked "web programming novice" OR list a
specialization - you don't need to implement it all yourself, but you do need to be in charge of
getting it described and added. Your expertise self-evaluation is completely on the honor system.

For instance:

| Member | Web dev level | Specialization |
| --- | --- | --- |
| Ned the Novice | web programming novice | |
| Isaac the Intermediate | Took IT 202, built something in php once | I want to learn about website performance so I will be adding performance tests and keeping a performance log. |
| Edith the Expert | Interned as a web dev for the last 2 semesters | I will containerize the app and configure it to run within Kubernetes, integrate it with a CI/CD platform so that the deployed version is updated once all tests pass, and I will run a load test with several synthetic long-session users to demonstrate rolling updates to the code. |

| Member | Web dev level | Specialization |
| --- | --- | --- |
| Aashish Agrawal | web programming novice | |
| Karan Ahuja | web programming novice | |

## Deliverables for checkpoint 2

Outline in English what the deliverables will be for checkpoint 2. Provide a concise list that is
amenable to being translated into specific tests. Pro-tip: if you write that concise list here, you
should be able to easily translate it into a collection of test suites.

For each specialization, you must list specific checkpoints that are relevant to that particular specialization.

- Demonstrate ability to access Blackboard API
- Store any pulled data from APIs into MongoDB database
- Pull data from database and represent it as a dynamically updated web view
- Have a test suite for making sure database can perform CRUD operations

## Deliverables for checkpoint 4

Outline in English what the deliverables will be for checkpoint 4. Reminder that this is not *due*
until checkpoint 2, but failing to plan is planning to fail.

For each specialization, you must list specific checkpoints that are relevant to that particular specialization.

- User should be able to filter out data as desired
- User should be able to add "notifications" to a calendar, allowing for easy planning
- There should be warnings if app can tell if a due date is coming up soon
- Demonstrate ability to access Piazza API
- Attempt at scraping Gradescope data
- Show grading info for each course

## Deliverables for final project

Outline in English what the deliverables will be for the final checkpoint. This will should be
similar to the **Description** above, but written out as an explicit checklist rather than a human
readable description. Reminder that this is not *due* until checkpoint 4, but failing to plan is
planning to fail.

For each specialization, you must list specific checkpoints that are relevant to that particular specialization.

- User should be able to add their own notifications/notes
- User should be able to set up reminders and alarms for calendar events
- User should be able to see previews of any files attached to notifications

## Specialization deliverables

For each student/team adding a specialization, name that specialization and describe what
functionality you will be adding.

We are not specialized students.

# Installation

By the time you get to the end of the final project, this section should have a full set of
instructions for how to spin up your app.
