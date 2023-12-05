
Feature: User Management
    Scenario: User logs in
        Given the user has valid log in credentials
        When the user goes to users/login
        And the user fills out login form
        And the user clicks on element with name login
        Then the user is taken to index
        And the user greeting is Welcome, User.

    Scenario: User logs out
        Given the user is logged in
        When the user clicks on element with id logout
        Then the user is taken to index
        And the user greeting is Not signed in.
    
    Scenario: New user registers
        Given the user has valid registration information
        When the user goes to users/register
        And the user fills out registration form
        And the user clicks on element with name register
        Then the user is taken to index
        And the user greeting is Welcome, RegistrationTest.
        
    Scenario: User goes to log in page after being authenticated
        Given the user is logged in
        When the user goes to users/login
        Then the user is taken to index

    Scenario: User checks the information needed to register
        Given the user is on index
        When the user goes to users/register
        Then the user can see element with name username
        And the user can see element with name email
        And the user can see element with name password
        And the user can see element with name confirmation