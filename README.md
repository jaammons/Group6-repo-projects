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


### BDD
* WIP


<p align="right">(<a href="#top">back to top</a>)</p>


### API Tests
# Overview

Postman is a comprehensive API development tool that streamlines the creation, testing, documentation, and sharing of APIs. It offers a user-friendly interface that empowers developers to efficiently design, test, and debug APIs.

Postman Lab Instructions

# Installation
- **Download Postman:**
  - Go to the [Postman website](https://www.postman.com/downloads/) or search "Postman download" in your preferred search engine.
  - Choose the appropriate version for your operating system (Windows, macOS, Linux).
  - Click on the download button to start downloading the installer.

- **Install Postman:**
  - **For Windows:**
    - Once the download is complete, locate the downloaded installer file (usually in your 'Downloads' folder) and double-click to open it.
    - Follow the on-screen instructions provided by the installer. Typically, this involves accepting terms, choosing installation location, and confirming the installation.
    - After the installation completes, Postman should be ready to use. You can launch it from the Start menu or desktop shortcut.

  - **For macOS:**
    - Locate the downloaded Postman file, usually in your 'Downloads' folder, and double-click to open it.
    - Drag and drop the Postman app into the 'Applications' folder or follow any prompts to install.
    - Once installed, you can open Postman from the Applications folder or using Spotlight Search (Cmd + Space and type "Postman").

  - **For Linux:**
    - Depending on your Linux distribution, the installation process may vary slightly. Refer to Postman's documentation for detailed instructions.
    - Typically, it involves downloading the compressed file, extracting it to a desired location, and running Postman from the extracted folder using terminal commands.

- **Sign in or Create Account (Optional):**
  - Upon launching Postman, you might have the option to sign in or create a new account.
  - Signing in allows access to syncing collections, environments, and collaborating with team members.
  - You can choose to sign in or skip this step and use Postman without an account.

- **Start Using Postman:**
  - Postman should now be installed and ready for use. Open the application to start designing, testing, and documenting APIs.


# Lab

# Request

# Postman VS Request Library


<p align="right">(<a href="#top">back to top</a>)</p>


### TDD
* WIP


<p align="right">(<a href="#top">back to top</a>)</p>


