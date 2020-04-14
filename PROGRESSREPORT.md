## What were the different functionalities you aimed to finish for each deadline (checkpoints 2, 3, 4)?
  - Checkpoint 2: We wanted to use the Piazza api to access data from Piazza and set up MongoDB.
  - Checkpoint 3: We wanted to fully set up Gradescope and access data from there.
  - Checkpoint 4: We wanted to fully set up Blackboard and access data from there.
  -
  - A quick English description of “what is currently working in the app”
    - The things that are currently working in the app are that a docker container can be deployed in which a user can register
    with its username and password and login again. Once the user logins to the app, then the user can enter its username and
    password for Piazza, Gradescope, and Blackboard and those information will be linked to the information for logging into
    the app in the database. Once you click on the links for Piazza and Gradescope, the user will be able to see posts for
    Piazza and assignments from Gradescope. For Blackboard, the user will be able to see the recent activity stream.
  - 
  - Who accomplished what
    - Karan: Wrote the scrapers for Gradescope and Blackboard. Also wrote the test cases for these as well as they implemented
    Selenium which automates the usage of an internet browser.
    - Aashish: Worked on the app structure itself which is Flask, created the MongoDB database, wrote the test cases for that,
    and created the html pages for the app.
  -
  - What didn’t get done in time
    - A lot of things didn't get in time because after checkpoint 2, we realized that NodeJS wasn't the best thing to use for
    our app as the Piazza API, Gradescope scraper, and Blackboard scraper ultilized Python. Therefore, after Checkpoint 2 we
    basically had to write our app from scratch which pushed us a checkpoint behind. For checkpoint 3, we finished what we had
    planned for checkpoint 2 and then we caught up for checkpoint 3 with checkpoint 4's deadline.
 
## What is the plan of attack for finishing Checkpoint 5?
  - The plan of attack is to finish the Blackboard scraper, make the app look beautiful, and pass all of our test cases.
  - 
  - What functionality remains to be finished?
    - The functionality that remains to be finished is the Blackboard scraper so you can see the recent activities on the
    webpage. Also, making the app look more colorful as well.
  -
  - Who will be in charge of finishing what
    - Karan: Will finish the Blackboard scraper and the test cases for it
    - Aashish: Will make the app look more colorful and improve the database with the Blackboard information storage.
    
## What changes, if any, do you want to make from your original plan?
  - The changes are that a calendar will not be provided and you own notifications will not be implemented.
  -
  - What is your reason for making those changes (i.e. what you did try, what you learned, what you realized is way harder 
  than it needed to be, and how you realized that)?
    - The reason for making these changes is that as implementing Gradescope, Piazza, and Blackboard took a lot more time 
    than expected, therefore, we have decided that the calendar and the notifications part will not be part of the app.
  notifications part will not be part of the app.
