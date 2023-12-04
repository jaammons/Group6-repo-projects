Feature: User Login
    Scenario: Accountholder logins
        Given user is on the login page
        When valid username and password entered
        Then clicks login button
        Then user is taken to a new login page