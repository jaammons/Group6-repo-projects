<!-- PROJECT LOGO -->
<div align="center">
  <h1 align="center" id="top">Group6 Repo Project</h1>
  <a href="https://jaammons.github.io/Group6-repo-projects/ecommerce">https://jaammons.github.io/Group6-repo-projects/ecommerce</a>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#testing-tools-and-software-development-processes">Testing Tools and Software Development Processes</a></li>
        <li><a href="#made-with">Made With</a></li>
        <li><a href="#contributers">Contributors</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#running-django">Running Django</a></li>
      </ul>
    </li>
    <li>
      <a href="#labs">Labs</a>
      <ul>
        <li><a href="#selenium">Selenium</a></li>
        <li><a href="#bdd">BDD</a></li>
        <li><a href="#api-tests">API Tests</a></li>
        <li><a href="#tdd">Test Driven Development</a></li>
      </ul>
    </li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

This project is designed to teach about software quality assurance by utilizing various testing tools and software development processes.

### Testing Tools and Software Development Processes
* Website Testing - Selenium
* Behavior Driven Development - Behave
* API tests - Postman
* Test Driven Development (TDD)


<p align="right">(<a href="#top">back to top</a>)</p>


### Made With
* Python
* Django
* Selenium


<p align="right">(<a href="#top">back to top</a>)</p>


### Contributors
* James Ammons - Document Writer
* Allan Alvarez-Gomez - Document Writer
* Sean Norini - Developer
* Isaiah Dillard - Developer
* Quinton Gilchrist - Developer
* Noah Liby - Tester
* Stephen Strong - Tester
* Prince Varghese - Tester


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
* Python - https://www.python.org/downloads/release/python-3120/
 

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/jaammons/Group6-repo-projects.git
   ```
2. (Recommended) Setup Virtual Environment
   ```sh
   # Create virtual environment folder name env
   python -m venv env
   ```
   ```sh
   # Activate the virtual environment, terminal should show env near prompt. Type deactivate to exit virtual environment
   env/scripts/activate
   ```
3. Install Project Dependencies
   ```sh
   pip install -r requirements.txt
   ```

### Running Django
1. Navigate to project folder in terminal
   ```sh
   # Example powershell command and directory, the folder should contain manage.py
   cd c:/your-github-folder/group6-repo-projects/ecommerce
   ```
2. Start Django server
   ```sh
   python manage.py runserver
   ```
3. Ctrl + left-click the link created in the terminal or open web browser and enter django site address
   ```sh
   # Default address
   http://127.0.0.1:8000/
   ```
4. The following steps are only necessary if the database is deleted
   ```sh
   # Prepare Django models
   python manage.py makemigrations
   ```
   ```sh
   # Commit model changes to database
   python manage.py migrate
   ```
   ```sh
   # Create new admin
   python manage.py createsuperuser
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Labs

### Selenium

Adminstrator Login Functionality Test
```sh
Navigate to Auctions site login page.
```
```sh
Enter administrator username and password.
```
```sh
Check for administrator greeting in nav bar, "Welcome, Admin."
```

Expected Result: Logged in as Admin with appropriate greeting.

<br>

Logout Functionality Test
```sh
Initialize pytest fixture with logged in user.
```
```sh
Click logout button.
```
```sh
Check for greeting in nav bar for "Not signed in."
```

Expected Result: Logged out of account and returned to homepage.


<p align="right">(<a href="#top">back to top</a>)</p>


## Behavior Driven Development

Behavior-Driven Development (BDD) is a software development methodology that focuses on improving communication and collaboration between different stakeholders involved in the software development process. It also consist of three phases

1. Discovery phase: Product Owner or Product Manager creates acceptance criteria that will be used for scenarios/stories.
2. Formulation phase: During the formulaion phase, acceptance criteria is turned into acceptance test.
3. Automation phase: Acceptance test is to ran continuously and validates that the new behavior implements into the system with no problems.

Writing BDD scenarios is a fundamental aspect of Behavior-Driven Development

Scenario Example 
```sh
@registration
Scenario: User successfully registers using valid credentials

Given user is on the registration page
The user enters a valide username, email, and password
Then user is successfully registered
```

Behavior Driven Development helps to bridge the gap between software development and stakeholders by promoting collaboration


<p align="right">(<a href="#top">back to top</a>)</p>


### API Tests
* WIP


<p align="right">(<a href="#top">back to top</a>)</p>


### TDD
* WIP


<p align="right">(<a href="#top">back to top</a>)</p>


