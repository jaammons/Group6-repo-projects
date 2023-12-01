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
* API tests - Postman/Request Library
* Test Driven Development (TDD)


<p align="right">(<a href="#top">back to top</a>)</p>


### Made With
* Python
* Django
* Selenium
* Pytest


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

## Utilities

### Pytest
Pytest is an excellent tool to aid in testing. One of the most useful features in Pytest is the ability to create reusable fixtures that provide test methods with easy access to commonly used objects. Pytest also uses automatic test collection to search for and run any tests that it can find.

* This example uses Pytest to create a log to hold results during testing, then proceeds to save and display the results while taking additional command line arguments to customize the report. The fixture is placed in conftest.py and is accessible to all of the tests Pytest automatically discovers.
```sh
# Create a pytest fixture that stays in scope for all tests
@pytest.fixture(scope="session", autouse=True, name="log")
def test_log(request) -> dict:
   # Initialize log
   log = initialize_log(request)
```
```sh
   # Yield log and run tests
   yield log
```
```sh
   # Save test data to a json file
   save_json(log, "test_log")
```
```sh
   # Get command line arguments
   args = []
   args.append(request.config.getoption("--show"))
   args.append(request.config.getoption("--more"))
```
```sh
   # Display results
   display_log(log, args)
```

## Labs

### Selenium
Selenium is a powerful, open-source framework that is popular for automating testing with web applications. The framework provides
the user with tools to navigate webpages and interact with them. It is capable to finding page elements through a variety of methods to which provides the ability to automatically test environments that may change frequently.
<br>
To begin testing a page with selenium, you need to initialize a webdriver and navigate to the page you want to test.
```sh
# Import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
```
```sh
# Using webdriver to emulate a chrome browser
driver = webdriver.Chrome()
```
```sh
# Navigate to web address, this address is the default for django's runserver command.
driver.get("http://127.0.0.1:8000/")
```

Now that the webdriver is initialized, here are some examples of other selenium tools and tests that use them:

find_element - Searches the page for an html element that matches the given arguments and returns that element. Useful for verifying that all form fields are present on a webpage or finding an element to interact with such as typing into an input.

### Validate Registration Form Fields: Verify all necessary form fields exist on the page.
```sh
# Navigate to registration form page.
driver.get("http://127.0.0.1:8000/users/register")
```
```sh
# Search for element by html name field and verify form fields exist
try:
   driver.find_element(By.NAME, "username")
   driver.find_element(By.NAME, "email")
   driver.find_element(By.NAME, "password")
   driver.find_element(By.NAME, "confirmation")
```
```sh
# Selenium will throw NoSuchElemenException if find_element returns nothing.
except NoSuchElementException as e:
   log_result("fail", log, f"{type(e).__name__} : {e.msg}")
```
Expected Result: All elements found.

<br>

Next, we can add interaction with the elements we find.

### Test Login - Verify that user with valid credentials can log in.
```sh
# Navigate to Auctions site login page.
 driver.get("http://127.0.0.1:8000/users/login")
```
```sh
# Enter username and password.
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
# Click login button
driver.find_element(By.NAME, "login").click()
```
```sh
# Check for user greeting in nav bar, "Welcome, User."
greeting = user_driver.find_element(By.ID, "greeting").text
assert greeting == "Welcome, User."
```
Expected Result: Logged in as User with appropriate greeting.

<br>
<br>

You can also interact with dropdown menus.

### Test Category Dropdown - Verify that category dropdown selection redirects user to the proper page.
```sh
# Check if category dropdown exists
category_dropdown = user_driver.find_element(By.NAME, "category")
```
```sh
# Select a category 
Select(category_dropdown).select_by_visible_text("Watches")
```
```sh
# Submit choice
user_driver.find_element(By.ID, "category_select").click()
```
```sh
# Find auction listings on page
auctions = user_driver.find_elements(By.CLASS_NAME, "item-name")
# Confirm expected number of auctions
assert len(auctions) == 4
# Confirm items match category.
items = ["Fossil Watch", "Golden Hour Watch", "Casio Watch", "Timex Watch"]
for auction in auctions:
      assert auction.text in items
```
Expected Result: Page results return only the selected category.

<br>

Selenium can also capture screenshots of a webpage to compare it with a baseline image.

### Test Listings - Verifies that auction listings show on index page and provides a screenshot to compare with expected results if it fails.
```sh
# Declare utility function for taking screenshots
def capture_screenshot(driver: webdriver.Chrome, file_path: str, file_name: str):
    driver.save_screenshot(file_path)
```
```sh
# Assert that selenium found a page element
try:
   assert len(driver.find_elements(By.CLASS_NAME, "item-container")) > 0
```
```sh
except NoSuchElementException as e:
   # Log errors
   log_result("fail", log, f"{type(e).__name__} : {e.msg}")
   # Capture screenshot
   capture_screenshot(driver, "test_listings_actual")
```
Expected result: 

<br>

Some additional tests using selenium...

### Test URL Titles - Load each page and verify URL titles match expected value.
```sh
# List of pages to check
url_titles = [{"users/register":"Registration"}, {"users/login":"Log In"}, {"index":"Auctions"}, {"watchlist":"Watchlist"}, {"add_listing":"Add Listing"}, {"category/shoes":"Shoes"}]
```
```sh
# Load each webpage
for index, item in enumerate(url_titles):  
   # Log in after viewing registration and log in pages
   if index == 2:
      driver = login(driver, "User", "testuser1")

   # Compare expected and actual titles
   url, title = item.popitem()
   driver.get("http://127.0.0.1:8000/" + url)
   assert title in driver.title
```
Expected result: All webpage titles match the expected value.

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

Feature: Register new user
  In order to participate in autions
  Users should have to login
  Using valid credentials

Scenario: User successfully registers using valid credentials
  Given user is on the registration page
  When the user enters a valide username, email, and password
  Then user is successfully registered
```

Behavior Driven Development helps to bridge the gap between software development and stakeholders by promoting collaboration


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

## Postman Test Cases

### Admin Login Functionality Test

- **Objective:** Validate the administrator login functionality on the Auctions site.
- **Steps:**
    1. Send a POST request to the login endpoint of the Auctions site with administrator credentials. 
    2. Check the response for a successful login status (e.g., HTTP 200 OK).
    3. Verify the presence of the "Welcome, Admin" greeting in the navigation bar of the response.

### Logout Functionality Test

- **Objective:** Validate the logout functionality on the Auctions site.
- **Preconditions:** Ensure that an administrator is logged in.
- **Steps:**
    1. Send a POST request to the logout endpoint or perform the action associated with logout.
    2. Check the response for a successful logout status or appropriate confirmation (e.g., HTTP 200 OK or relevant message).
    3. Verify that the navigation bar reflects "Not signed in" or a similar message indicating the successful logout.

 ## Accessing the Home Page Test

- **Objective:** Verify the response message when accessing the home page of the Ecommerce site.
- **Steps:**
    1. Open Postman and import the provided collection.
    2. Click on "Import" in the top-left corner.
    3. Select the "Link" tab.
    4. Paste the collection link: Postman Collection.
    5. Click "Continue" and then "Import."
    6. Select the "Access Home Page" request.
    7. Click the "Send" button to make a GET request to the home page.
    8. Verify that the response includes the expected text: "Welcome to my Ecommerce."




# Request

## Requests Library in Python

The `requests` library in Python is a powerful HTTP library designed to simplify the process of making HTTP requests and handling responses. It offers a user-friendly interface for sending various types of HTTP requests, such as GET, POST, PUT, DELETE, and more, to web servers.

### Key Features:

- **Ease of Use:** Provides a clean and intuitive syntax, making it straightforward to work with HTTP requests and responses.
  
- **HTTP Method Support:** Supports multiple HTTP methods, enabling users to perform different types of requests effortlessly.
  
- **URL Handling:** Simplifies URL construction and parameter passing, allowing easy inclusion of query parameters or request data.
  
- **Response Handling:** Facilitates access to response data, including headers, status codes, and content in different formats like JSON, HTML, or plain text.
  
- **Session Handling:** Supports persistent sessions, allowing users to maintain certain parameters across multiple requests, such as cookies or authentication credentials.
  
- **SSL Certificate Verification:** Provides support for secure connections by verifying SSL certificates for HTTPS URLs.
  
- **Authentication:** Offers straightforward handling of various authentication mechanisms like Basic Authentication, OAuth, etc.

Overall, the `requests` library is widely used in Python for its simplicity, flexibility, and comprehensive documentation, making it a preferred choice for working with HTTP and web APIs.

# Python Requests Library Lab for Testing Ecommerce APIs

## Install Required Package

Ensure you have the `requests` library installed. If not, install it using:

```bash
pip install requests
```
## Create a Test Script

Create a new Python script( e.g., 'ecommerce_api_test.py') in the same directory as your Ecommerce application.

```python
import requests

# Set the base URL for your Ecommerce Flask application
base_url = 'http://localhost:8000'  # Replace with your Ecommerce app's URL

def test_home_endpoint():
    response = requests.get(f'{base_url}/')
    assert response.status_code == 200
    assert response.text == 'Welcome to Our Ecommerce Site'  # Update with your Ecommerce site's welcome message

# Add other test functions similar to the provided lab example

if __name__ == '__main__':
    # Run your test functions
    test_home_endpoint()
    # Add other test function calls here for your Ecommerce app's endpoints
```
## Run the Test Script

Open your terminal, navigate to the director containing your Ecommerce application and the new Python script ('ecommerce_api_test.py'), and run:

```python
python ecommerce_api_test.py
```
Ensure that your Ecommerce application is running ('python run.py') while exeecuting the tests.



# Postman VS Request Library

### Similarities between Postman and `requests` Library:

1. **HTTP Requests:**
   - Both Postman and the `requests` library facilitate making HTTP requests to interact with web services and APIs.
  
2. **HTTP Methods:**
   - Both support common HTTP methods like GET, POST, PUT, DELETE, etc., allowing users to perform various operations on resources.

3. **Response Handling:**
   - Both tools provide features to handle responses received from the server, allowing users to extract and validate response data.

4. **Headers and Parameters:**
   - Both allow users to set custom headers and parameters within requests for specific configurations or requirements.

5. **Authentication:**
   - Both support various authentication methods (such as Basic Auth, OAuth, API keys) to access protected endpoints.

6. **Testing and Assertions:**
   - Both enable users to write tests and assertions to validate responses received from the server, ensuring the expected behavior of the API.

7. **Collection/Scripting:**
   - Both tools allow users to organize requests into collections and folders, enabling scripting or automation of API workflows.

8. **Community Support:**
    - Both have active communities where users can seek help, find tutorials, and share knowledge about using the tool effectively.

### Differences between Postman and `requests` Library:

1. **User Interface vs. Library:**
   - Postman provides a graphical user interface (GUI) for building and sending requests, while the `requests` library is used programmatically within Python code.

2. **Accessibility and Environment:**
   - Postman is a standalone application that needs to be installed and used separately, whereas the `requests` library is accessible within Python environments.

3. **Interactivity:**
   - Postman offers an interactive and visual way to construct requests and view responses in real-time, while the `requests` library requires coding and doesn’t have a visual interface.

4. **Dependency:**
   - Postman operates as a standalone application across different operating systems, whereas the `requests` library is dependent on Python and can be used only within Python environments.

5. **Complexity vs. Simplicity:**
   - Postman might be more user-friendly for non-programmers due to its GUI, whereas the `requests` library might require programming skills but offers flexibility and control.

6. **Usage:**
   - Postman is commonly used for quick API testing, collaboration, and documentation, while the `requests` library is employed for integrating API calls within Python applications or scripts.

7. **Automation and Integration:**
   - Postman allows for collection runs and testing suites but might not be as easily integrated into automated workflows compared to the `requests` library within a Python codebase.

8. **Learning Curve:**
   - Postman might have a shorter learning curve for beginners, especially for basic API interactions, while the `requests` library might require understanding Python basics.

9. **Community and Extensibility:**
   - Postman offers a collaborative space with a vast community and built-in features, while the `requests` library's capabilities can be extended through Python's ecosystem and libraries.

10. **Customization and Control:**
    - Postman has its limitations in terms of customization and fine-grained control, whereas the `requests` library allows for highly tailored requests and handling of responses within code.

### Conclusion:

**Postman**:
- **Strengths**:
  - Ideal for quick API testing, exploration, and prototyping.
  - Offers a user-friendly GUI suitable for non-programmers.
  - Facilitates easy collaboration, sharing, and documentation of APIs.
  - Provides an interactive environment for visualizing requests and responses.

- **Best Use Cases**:
  - Initial API testing and exploratory phases.
  - Collaboration among team members for API development.
  - Rapid prototyping and generating API documentation.

**`requests` Library**:
- **Strengths**:
  - Enables programmatic control for integrating API calls within Python applications or scripts.
  - Offers fine-grained control, customization, and flexibility in making HTTP requests.
  - Well-suited for automation, scripting, and integrating API calls into complex workflows.

- **Best Use Cases**:
  - Integration of API calls within Python-based applications.
  - Automating API workflows and integrating them into larger systems.
  - Fine-tuning and customizing requests and handling responses within code.

**Conclusion**:
- **Postman** excels in providing a user-friendly environment for quick API testing, collaboration, and initial API exploration. It's great for non-programmers and teams working on API development.
  
- On the other hand, the **`requests` library** in Python offers unparalleled control and flexibility for developers needing programmatic control over their API interactions, especially when integrating API calls within Python applications or scripts and requiring a high level of customization and automation.

Choosing between them often depends on the specific use case, the level of control needed, and the user's familiarity with programming languages like Python.



<p align="right">(<a href="#top">back to top</a>)</p>


### Test-Driven Development (TDD):

**What is TDD?**

Test-Driven Development (TDD) is a software development approach where tests are written before the actual code implementation. It follows a cycle of writing tests, writing code to pass those tests, and then refactoring the code while ensuring all tests still pass.



<p align="right">(<a href="#top">back to top</a>)</p>


