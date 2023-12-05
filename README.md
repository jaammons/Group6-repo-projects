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

- Website Testing - Selenium
- Behavior Driven Development - Behave
- API tests - Postman/Request Library
- Test Driven Development (TDD)

<p align="right">(<a href="#top">back to top</a>)</p>

### Made With

- Python
- Django
- Selenium
- Pytest

<p align="right">(<a href="#top">back to top</a>)</p>

### Contributors

- James Ammons - Document Writer
- Allan Alvarez-Gomez - Document Writer
- Sean Norini - Developer
- Isaiah Dillard - Developer
- Quinton Gilchrist - Developer
- Noah Liby - Tester
- Stephen Strong - Tester
- Prince Varghese - Tester

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

- Python - https://www.python.org/downloads/release/python-3120/

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
   # Populate database with test values
   python manage.py loaddata fixtures/default.json
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Utilities

### Pytest

Pytest is an excellent tool to aid in testing. One of the most useful features in Pytest is the ability to create reusable fixtures that provide test methods with easy access to commonly used objects. Pytest also uses automatic test collection to search for and run any tests that it can find. Pytest-Django also provides a fixture called live_server which runs a django server in the background to provide a test environment. To access a return or yield value from a fixture, just add the fixture to an argument call and pytest will automatically use the matching fixture in that test. Below are the necessary imports and some of the pytest fixtures used by the following labs.

- Imports

```python
import pytest
from django.core.management import call_command
from selenium import webdriver
```

- This fixture sets up the database for the testing session.

```python
# scope variable determines how often to run the fixture. function is run once per each test function.
@pytest.fixture(scope='function', autouse=True)
def django_db_setup(django_db_setup, django_db_blocker):

   # Open database
   with django_db_blocker.unblock():

      # Wipe data
      call_command("flush", interactive=False)

      # Load default values
      call_command('loaddata', 'default.json')
```

- Fixture to initialize and yield a chromedriver for web navigation.

```python
@pytest.fixture(scope="session", autouse=True)
def driver(live_server) -> webdriver.Chrome:
   # Create chromedriver instance
   driver = webdriver.Chrome()

   yield driver

   # End chromedriver instance
   driver.quit()
```

- Pytest comes with a lot of customizable options for logging already, but, while using selenium, we can create a fixture that takes a screenshot if the test fails or a command line argument was given.

```python
# Automatically use on test start, but doesn't do anything until the test finishes.
@pytest.fixture(scope="function", autouse=True)
def screenshot(request, driver):
   # Test start

   yield

   # Test end

   # Get the name of the test function
   function_name = request.function.__name__

   # Take screenshot if --capture in command line arguments
   if request.config.getoption("--screenshot"):
      capture_screenshot(driver, function_name)

   # Take screenshot if test failed
   elif request.node.rep_call.failed:
      capture_screenshot(driver, function_name + "_actual")
```

## Labs

### Selenium

Selenium is a powerful, open-source framework that is popular for automating testing with web applications. The framework provides
the user with tools to navigate webpages and interact with them. It is capable to finding page elements through a variety of methods to which provides the ability to automatically test environments that may change frequently. Here is a list of some of the useful functions that selenium provides:
<br>
| Function | Description |
| ----------- | ----------- |
| driver.get | Navigates to specified url |
| driver.find_element(type, value) | Finds a webpage element using a selector type and selector value. |
| driver.find_elements(type, value) | Same as find element, except it will return multiple elements if there is more than one match. |
| element.text | Retrieves the visible text from a web element. |
| element.click() | Clicks on a given element. |
| element.send_keys(value) | Types a given value into an input element. |
| element.get_attribute(attribute_name) | Gets the value of a specific attribute of a web element. |
| element.clear() | Clears the selected input field. |
| driver.title | Returns the webpages title. |
| driver.current_url | Returns the url of the current webpage. |
| driver.close() | Closes current browser window. |
| driver.quit() | Quits the browser and closes all windows. |

To begin actual testing on a page with selenium, some additional imports are needed.

```python
# Import libraries
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
```

Now that we have fixtures in place and all the imports necessary to run selenium, we can create some utility functions to assist with webpage testing.
<br>

1. **navigate_to(driver, live_server, url)** - Retrieve given url.

```python
# Driver is from the fixture created earlier. Live_server is a fixture that's part of pytest-django and doesn't need to be created.
driver.get(live_server.url + url)
```

<br>

2. **find_element(driver, selector_type, selector_value)** - Find and return a web element.

```python
# Provides a little more flexibility for find_element and allows for variable selector types.
element = None
match selector_type:
   case "id":
      element = driver.find_element(By.ID, selector_value)
   case "name":
      element = driver.find_element(By.NAME, selector_value)
   case "class":
      element = driver.find_element(By.CLASS_NAME, selector_value)
return element
```

<br>

3. **find_elements(driver, selector_type, selector_value)** - Same as above but can return multiple elements.

<br>

4. **elements_exist(driver, elements)** - Takes a dictionary argument and checks the page for all elements matching the key:value pairs.

```python
# Loop over elements
for selector_type, selector_value in elements.items():

   # Use custom find_elements function to search for an element
   elements = find_elements(driver, selector_type, selector_value)

   # If no elements were found, return False
   if len(find_elements(driver, selector_type, selector_value)) == 0:
      return False

# Otherwise return True.
return True
```

<br>

5. **select(driver, selector_type, selector_value)** - Select an option from a dropdown menu.

```python
# Find the dropdown menu
dropdown = find_element(driver, selector_type, selector_value)

# Select an option from the menu
Select(dropdown).select_by_visible_text(selector_value)
```

<br>

6. **capture_screenshot(driver, file_name)** - Capture a screenshot of the current page.

```python
# Save a screen with a given file name in the auctions/static/tests directory.
driver.save_screenshot("auctions/static/tests/" + file_name + ".png")
```

<br>

7. **fill_form(driver, form_fields)** - Takes a dictionary argument and uses the key:value pairs to find input elements on a form and insert values. With a slight modification to the dictionary values and function, this method could also utilize the custom find_element and allow for variable css selectors.

```python
# Loop over dictionary items
for field_name, field_value in form_fields.items():

   # Search for element by name and insert value.
   driver.find_element(By.NAME, field_name).send_keys(field_value)
```

<br>

8. **click(driver, selector_type, selector_value)** - Clicks on a webpage element.

```python
# Use custom find_element to get element
element = find_element(driver, selector_type, selector_value)

# Click element
element.click()
```

<br>

9. **login(driver, live_server, form_fields)** - Combines above functions to log in a user.

```python
# Navigate to page
navigate_to(driver, live_server, "/users/login")

# Enter login info
fill_form(driver, form_fields)

# Click login
click(driver, "name", "login")
```

Now that selenium is ready and the utility functions are made, here are some examples using selenium tools in webpage testing:

<br>

**Validate Registration Form Fields**: Verify all necessary form fields exist on the page.

```python
# Form fields to check for
form_fields = {"name":"username","name":"email","name":"password","name":"confirmation","name":"register"}
```

```python
# Navigate to registration form page.
navigate_to(driver, live_server, "/users/register")
```

```python
# Search for element by html name field and verify form fields exist
assert elements_exist(driver, form_fields)
```

Expected Result: All elements found.

<br>

**Test Login** - Verify that user with valid credentials can log in.

```python
# Login as User
login(driver, live_server, LOGIN_USER_FORM_FIELDS)

# Verify expected greeting on index
expected = "Welcome, User."  # Output is Welcome, <username>, but the test user is User.

# Use .text to retrieve the visible text from page greeting
greeting = find_element(driver, "id", "greeting").text
assert greeting == expected
```

Expected Result: Logged in as User with appropriate greeting.

<br>

**Test Category Dropdown** - Verify that category dropdown selection redirects user to the proper page.

```python
# Check if category dropdown exists
assert elements_exist(driver, {"name":"category"})

# Select a category
select(driver, "name", "category")

# submit choice
click(driver, "id", "category-select")

# Verify page loads with right category
auctions = find_elements(driver, "class", "item-name")
assert len(auctions) == 4

# Verify items match category
items = ["Fossil Watch", "Golden Hour Watch", "Casio Watch", "Timex Watch"]
for auction in auctions:
   assert auction.text in items
```

Expected Result: Page results return only the selected category.

<br>

**Test bid display** - Verify that auctions accept valid bids and display a message if the user is currently winning the bid.

```python
# Navigate to auction to bid on
navigate_to(driver, live_server, "/listing/1")

# Verify notification of winning bid is not currently displayed.
assert find_element(driver, "id", "bid_notification").text == "New Bid"

# Get minimum bid amount needed
bid = find_element(driver, "id", "bid")

# Use get_attribute to get the placeholder value, which is the minimum valid bid amount.
min_bid = bid.get_attribute("placeholder")

# Enter bid
bid.send_keys(min_bid)

# Submit bid
click(driver, "id", "submit_bid")

# Verify notification of user winning bid is displayed.
assert find_element(driver, "id", "bid_notification").text == "Currently winning bid."
```

<br>

**Test login redirect** - Verify that logged in users who visit the log in page are redirected to the index.

```python
# Log in user
login(driver, live_server, LOGIN_USER_FORM_FIELDS)

# Navigate to log in page
navigate_to(driver, live_server, "/users/login")

# Check url after redirect
assert live_server.url + "/index" == driver.current_url
```

<br>

**Test Listings** - Verifies that auction listings show on index page and provides a screenshot to compare with expected results if it fails.

```python
# Navigate to index
    navigate_to(driver, live_server, "/index")
```

```python
 # Check for auction listing containers
    assert elements_exist(driver, {"class":"item-container"})
```

Expected result: Item containers for auction listings exist.

**Test URL Titles** - Load each page and verify URL titles match expected value.

```python
# List of pages to check
   url_titles = [{"/users/register":"Registration"}, {"/users/login":"Log In"}, {"/index":"Auctions"}, {"/watchlist":"Watchlist"}
                  , {"/add_listing":"Add Listing"}, {"/category/shoes":"Shoes"}]
```

```python
for index, item in enumerate(url_titles):
   # Compare expected and actual titles
   url, title = item.popitem()
   navigate_to(driver, live_server, url)
   assert title in driver.title
```

```python
# log in after viewing registration and log in pages
if index == 1:
   login(driver, live_server, LOGIN_USER_FORM_FIELDS)
```

Expected result: All webpage titles match the expected value.

<p align="right">(<a href="#top">back to top</a>)</p>

## Behavior Driven Development

Behavior-Driven Development (BDD) is a software development methodology that focuses on improving communication and collaboration between different stakeholders involved in the software development process. It also consist of three phases

1. Discovery phase: Product Owner or Product Manager creates acceptance criteria that will be used for scenarios/stories.
2. Formulation phase: During the formulaion phase, acceptance criteria is turned into acceptance test.
3. Automation phase: Acceptance test is to ran continuously and validates that the new behavior implements into the system with no problems.

Writing BDD scenarios is a fundamental aspect of Behavior-Driven Development

### Gherkin Language

In BDD Scenarios are designed to illustrate a specific aspect of a behavior of the application. The words Given, When and Then are often used to help drive out the scenarios. Gherkin helps developers and QA engineers clarify the requirements by breaking them into specific examples. Gherkin is used by Behave and many other tools.

Scenario Example

```sh
Feature: User Login
Scenario: User logs into site
   Given user is on login page
   When valid username and password are entered
   Then user is brought to new homepage
```
### Behave
Behave is a tool used in Python for Behavior Driven Development. Behave is able to make use of any feature written in the Gherkin language. Using the scenario above in a feature file always programmers to create scenarios using the basic language and behave will transform them into code. 

1. Create a directory dedicated to behave.

2. With your designated feature in mind create a feature file naming it after that feature.

  ```sh
  Login.feature
  ```
    In this feature file you will create Features and Scenarios in Gherkin like the one above.

3. Within that same directory create a new directory named "steps". This folder will hold the steps that behave creates.

4. Go back to the directory for behave and open up the features file.

    In that features file you will create your Features and Scenarios in Gherkin like we did above.

5. After creating all your Features and Scenarios you will open up a new terminal in the behave root directory.

6. For Behave to convert you feature file into usable code you will type the command "behaave"

    If you have more than one feature you will have to name that feature

  ```sh
  behave feature\Login.feature
  ```
7. The terminal will then print out the steps for you to use.

   ```sh
   @given(u'user is on the login page')
   def step_impl(context):
     raise NotImplementedError(u'STEP: Given user is on the login page')
   
   @when(u'valid username and password entered')
   def step_impl(context):
    raise NotImplementedError(
        u'STEP: When valid username and password entered')
   
   @then(u'clicks login button')
   def step_impl(context):
    raise NotImplementedError(u'STEP: Then clicks login button')

   @then(u'user is taken to a new home page')
   def step_impl(context):
    raise NotImplementedError(u'STEP: Then user is taken to a new home page')
   
   ```
8. Within the "steps" directory create a python file that will house the steps that the terminal has created

   ```sh
   loginFeature.py
   ```
9. Once you have pasted the steps into the python file you will begin writting test for each feature.
   

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

### Welcome API Test

- **Objective:** Validate API endpoint and welcome message.
  1. Send a GET request to the welcome endpoint.
  2. Verify response is "Welcome to Our Ecommerce Site!"
     ![Success!](https://raw.githubusercontent.com/jaammons/Group6-repo-projects/main/ecommerce/readme_imgs/get_api_response.JPG)

### Get Auction Functionality Test

- **Objective:** Validate the get auction functionality on the Auctions site.
- **Steps:**
  1. Send a GET request with the primary key value of the auction to search for.
     ![Get request](https://raw.githubusercontent.com/jaammons/Group6-repo-projects/main/ecommerce/readme_imgs/get_api_test.JPG)
  2. Verify correct auction was retrieved and returned in a json response.
     ![Success!](https://raw.githubusercontent.com/jaammons/Group6-repo-projects/main/ecommerce/readme_imgs/get_api_response.JPG)

### Admin Login Functionality Test

- **Objective:** Validate the administrator login functionality on the Auctions site.
- **Steps:**
  1. Send the login page a GET request and verify status code 200, check on cookies tab.
     ![Get log in page](https://raw.githubusercontent.com/jaammons/Group6-repo-projects/main/ecommerce/readme_imgs/get.JPG)
  2. Copy the csrf token value and create a new X-CSRF-Token header to insert the value.
     ![Copy csrf token](https://raw.githubusercontent.com/jaammons/Group6-repo-projects/main/ecommerce/readme_imgs/token.JPG)
  3. Enter username and password into body and send a POST request to the login endpoint .
     ![Set body parameters!](https://raw.githubusercontent.com/jaammons/Group6-repo-projects/main/ecommerce/readme_imgs/params.JPG)
  4. Check the response for a successful login status (e.g., HTTP 200 OK).
  5. Verify the presence of the "Welcome, Admin" greeting in the navigation bar of the response.
     ![Success!](https://raw.githubusercontent.com/jaammons/Group6-repo-projects/main/ecommerce/readme_imgs/success.JPG)

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

Create a new Python script( e.g., 'api_test.py') in the same directory as your Ecommerce application.

1. This test performs the welcome test we did in postman, but using the python requests library.

```python
import requests
# Set the base URL for your Ecommerce Django application
base_url = 'http://localhost:8000'  # Replace with your Ecommerce app's URL

def test_welcome(live_server):
   # Get server response from endpoint
   response = requests.get(live_server.url + "/welcome")

   # Verify server status
   assert response.status_code == 200

   # Verify response
   assert response.text == 'Welcome to Our Ecommerce Site!'
```

2. API registration test - Validates function to create users through the API.

```python
   # Import json to handle json responses
   import json
   def test_registration(live_server):
      # Send a post request with the user info to add
      response = requests.post(live_server.url + "/users/register_user", data=REGISTRATION_FORM_FIELDS)

      # Verify server status code
      assert response.status_code == 200

      # Get the data from the response
      data = json.loads(response.json())

      # Verify success message
      assert data["Success"] == "New user created."
```

3. Cookie test - Verifies that cookies are still delicious. Sends a get request to the server and examines the cookie obtained in response.

```python
def test_cookies(live_server):
   # Send get request
   response = requests.get(live_server.url + "/users/get_cookie")
   # Receive response
   cookie_monster_says = response.cookies["cookie"][1:-1]
   # Verify cookie value
   assert cookie_monster_says == "COOKIE! Om nom nom nom."
```

## Run the Test Script

Open your terminal, navigate to the director containing your Ecommerce application and the new Python script ('api_test.py'), and run:

```python
pytest api_test.py
```

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

Test-Driven Development (TDD) is a software development approach where tests are written before the actual code implementation. While doing TDD you want to write the smallest amount of code possible that causes a failing test, then write code to make the test pass. It follows a cycle of writing tests, writing code to pass those tests, and then refactoring the code while ensuring all tests still pass.

**Why we do Test Driven Development**:
It helps developers find any errors in the logic of the code for any feature that is being tested, this improves the understanding of the code and how it will function.

![alt text](https://browserstack.wpenginepowered.com/wp-content/uploads/2023/06/TDD-640x770.png)

Here are some examples of features being added by using TDD:

**User log in remember me checkbox** - Saves a session for the user to skip log in when they visit the site.

1. Search for checkbox that doesn't exist yet.

```sh
def test_remember_me(driver):
    checkbox = driver.find_element(By.NAME, "remember_me")
```

2. Add checkbox to the page.

```sh
<input type="checkbox" name="remember_me">Remember Me
```

3. Login with checkbox ticked.

```sh
# Tick checkbox
checkbox.click()
# Login User
driver.find_element(By.NAME, "username").send_keys("User")
driver.find_element(By.NAME, "password").send_keys("testuser1")
driver.find_element(By.NAME, "login").click()
```

4. Reload page and check welcome greeting.

```sh
# Close page and reopen browser
driver = reload_page(driver, "http://127.0.0.1:8000")
# Check User greeting
greeting = driver.find_element(By.ID, "greeting")
assert greeting.text == "Welcome, User."
```

5. After confirming the test fails again, add a check in the django view for the remember_me checkbox.

```sh
if not "remember_me" in request.POST:
   request.session.set_expiry(0)
```

6. Function after refactoring the program. Added utility functions to make the code more readable and reusable. Changed the method to find expiration by checking the cookies.

```sh
# Navigate to login
navigate_to(driver, live_server, "/users/login")

# Click checkbox
click(driver, "name", "remember_me")

# Login User
fill_form(driver, LOGIN_USER_FORM_FIELDS)
click(driver, "name", "login")

# Check that cookie won't expire on browser close
assert get_cookie_expiration_time(driver, "sessionid") > 0
```

- The helper function used for this test:

```sh
def get_cookie_expiration_time(driver, cookie_name):
   # Get all cookies
   cookies = driver.get_cookies()

   # Find the specific cookie by name
   target_cookie = next((cookie for cookie in cookies if cookie["name"] == cookie_name), None)

   # Extract and return the expiration time of the cookie
   if target_cookie:
      if "expiry" in target_cookie:
         return target_cookie["expiry"]

   return 0
```

Expected outcome: User sessions expires immediately when closing browser unless remember me is checked.

**Add API entry point** - Adds a new API entry point to http://127.0.0.1:8000/get to get auction information.

1. Import requests library

```sh
import requests
```

2. Send API request

```sh
# Create request
url = "http://127.0.0.1:8000/auctions"
params = {"get":1}
# Send request
response = requests.get(url, params=params)
```

3. Verify server response, which should currently return 404.

```sh
# Check status code to verify response
assert response.status_code == 200
```

4. Add new view to django to handle the API requests.

```sh
# Create view
def get_auction(request):
    return JsonResponse({})
```

```sh
# Add view to urlpatterns
path("auctions", views.get, name="get")
```

5. Now that the API point exists, we need to check that the returned data is valid.

```sh
# Get the data from the response
data = response.json()
# Check data for valid info
assert data["pk"] == 1
```

6. Currently the page returns nothing, so next we add code to the view to search for the selected auction and return the data.

```sh
# Update django view, grabs data from model and converts to a json response.
data = serialize('json', AuctionListing.objects.filter(pk=request.GET.get("pk")))[1:-1]
json_data = json.loads(data)
return JsonResponse(json_data)
```

Expected outcome: Page successfully returns auction item where primary key = 1.

**Winning Bid Display** - Shows the user viewing an auction if their bid is currently the top bid.

1. Navigate to an auction as a logged in user.

```sh
# Navigate to page
user_driver.get("http://127.0.0.1:8000/listing/1")
```

2. Verify notification of winning bid is not already displayed.

```sh
assert user_driver.find_element(By.ID, "bid_notification") == "New Bid"
```

3. Place a new bid

```sh
# Get minimum bid necessary to bid on item
bid = user_driver.find_element(By.ID, "bid")
min_bid = bid.get_attribute("placeholder")
# Enter new bid
bid.send_keys(min_bid)
# Submit bid
user_driver.find_element(By.ID, "submit_bid").click()
```

4. Check for updated bid notification, which fails the current assertion.

```sh
assert user_driver.find_element(By.ID, "bid_notification") == "Currently winning bid."
```

5. Update django template to display if user is winning the bid and run the test again.

```sh
# Update template to show if current user is winning the auction bid
{% if request.user == bid.username %}
   <label for="bid" id="bid_notification">Currently winning bid.</label>
{% else %}
   <label for="bid" id="bid_notification">New Bid</label>
{% endif %}
```

6. Function after refactoring.

```sh
# Log in user
login(driver, live_server, LOGIN_USER_FORM_FIELDS)

# Navigate to auction to bid on
navigate_to(driver, live_server, "/listing/1")

# Verify notification of winning bid is not currently displayed.
assert find_element(driver, "id", "bid_notification").text == "New Bid"

# Get minimum bid amount needed
bid = find_element(driver, "id", "bid")
min_bid = bid.get_attribute("placeholder")

# Enter bid
bid.send_keys(min_bid)
# Submit bid
click(driver, "id", "submit_bid")

# Verify notification of user winning bid is displayed.
assert find_element(driver, "id", "bid_notification").text == "Currently winning bid."
```

Expected outcome: After placing a new bid, the bid label displays notification that the user is winning the bid.

<p align="right">(<a href="#top">back to top</a>)</p>

### Playwright:

An open-source library created by Microsoft that is used to test browswers and to scrape the web. This tool allows for cross-browser web automation, while supporting different types of tests like API, end-to-end, and component testing.

**Tools**:

- TraceViewer gets the information to find test errors, it adds snapshots, action explorer, screencast execution, etc.
- Codegen produces tests by learning the developer's code and saves them into any language.
- Inspector is a tool that allows for execution tests and logs.
**Languages Suported**:
<table>
  <thead>
    <tr>
      <th >JavaScript </th>
      <th >TypeScript </th>
      <th >Java </th>
      <th >Python </th>
      <th >C# </th>
    </tr>
  </thead>
</table>

### Installation Steps for Playwright in Python

1. **Install Playwright:**

   Install the Playwright library using pip:

   ```sh
   pip install playwright
   ```

2. **Install a Browser:**

   Playwright supports multiple browsers (Chromium, Firefox, WebKit). Install the browser(s) of your choice:

   ```sh
   playwright install
   ```

   This command will download the necessary browser binaries required by Playwright.

### Writing Tests with Playwright

1. **Import Playwright:**

   In your Python script, import Playwright:

   ```python
   from playwright.sync_api import sync_playwright
   ```

2. **Launch a Browser:**

   Use Playwright to launch a browser:

   ```python
   with sync_playwright() as p:
       browser = p.chromium.launch()
       context = browser.new_context()
       page = context.new_page()
   ```

    To simplify grabbing a page for each test, we can add some pytest fixtures. Adding these fixtures allows future test easy access to a browser or page by simply including them in the test arguments:
    ```python
    # Marks this as a fixture automatically used once for the current module being tested.
    @pytest.fixture(scope="module", autouse=True)
    def browser():
       # Specifically for django apps, this option allows async for playwright and live_server.
       os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

       # Start playwright using with context to terminate it after tests
       with sync_playwright() as playwright:

          # Launch a browser
          browser = playwright.chromium.launch()

          # Yield browser and start tests
          yield browser

          # Test ends and clean up browser
          browser.close()

    @pytest.fixture
    def page(browser):
       # Create new browser environment
       context = browser.new_context()

       # Create new page to start web navigation
       page = context.new_page()

       yield page
    ```

4. **Navigate to a URL:**

   Direct the browser to a specific URL:

    ```python
    page.goto("http://127.0.0.1:8000/")
    ```
### Test 1: Verify Page Title

Objective: Ensure the page title matches the expected title.

```python
from playwright.sync_api import sync_playwright

def test_page_title(live_server, page):    
        # Navigate to the specified URL
        page.goto(live_server.url)
        
        # Get the page title
        title = page.title()

        # Assert the title matches the expected title
        assert title == 'Auctions'
```

### Test 2: User Login

Objective: Simulate a user login by filling in the login form and verifying successful login.

```python
from playwright.sync_api import sync_playwright

def test_user_login(live_server, page):
    # Navigate to the specified URL
    page.goto(live_server.url + "/users/login")
    
    # Fill the login form fields
    page.fill('input[name="username"]', 'User')
    page.fill('input[name="password"]', 'testuser1')
    
    # Submit the login form
    page.click('button[type="submit"]')
    
    # Wait for a specific element after login (if applicable)
    # page.wait_for_selector('#greeting')
    
    # Get the greeting message after successful login
    greeting_message = page.inner_text('#greeting')
    
    # Assert the greeting message confirms successful login
    assert greeting_message == 'Welcome, User.'
```

### Reading Playwright Documentation for Python

When exploring Playwright for Python, it's essential to refer to the official documentation for comprehensive guidance and understanding of the library's capabilities. The Playwright documentation offers detailed explanations, examples, and API references, serving as a valuable resource for developers and testers.

#### Key Sections to Explore:

1. **Installation:** Understand the installation process, including setting up Playwright and installing browser binaries.

2. **API References:** Explore the available classes, methods, and functions provided by Playwright's Python API.

3. **Code Examples:** Study the provided code examples demonstrating how to perform various actions such as navigation, interactions with page elements, and assertions.

4. **Guides and Tutorials:** Benefit from guides and tutorials that walk through common use cases, best practices, and tips for efficient usage.

5. **Browser Compatibility:** Learn about the supported browsers (Chromium, Firefox, WebKit) and their features.

6. **Updates and Release Notes:** Stay updated with the latest features, enhancements, and bug fixes introduced in new versions.

Access the Playwright documentation for Python at [Playwright for Python Documentation](https://playwright.dev/python/docs/intro).

By referring to the documentation, developers and testers can effectively leverage Playwright's capabilities to automate browser interactions, perform testing, and ensure robust web applications.

<p align="right">(<a href="#top">back to top</a>)</p>

<p align="right">(<a href="#top">back to top</a>)</p>
