import json
import inspect 
from selenium import webdriver
import pickle

def log_result(result: str, log: dict, error=None) -> None:
    """
    Adds test result to the current log
    """
    # Get name of calling function
    test = inspect.stack()[1][0].f_globals[inspect.stack()[1][3]]

    # Add test result to log
    log[test.__name__]["result"] = result

    log[test.__name__]["doc"] = test.__doc__

    # If there was an error, add error message to log
    if error: 
        log[test.__name__]["error"] = error

def display_log(log: dict, args=None) -> None:
    """
    Display the test results
    """
    # Print results and get number of tests failed
    count_failed = _diplay_log_helper(log, args)
    
    # Print overall outcome
    if count_failed == 0:
        print("All tests passed.")
    else:
        print(f"{count_failed} test(s) failed.")

def _diplay_log_helper(log: dict, args: str=None) -> int:
    """
    Parses and prints the log send by display_log
    """
    # Initailize failed test counter
    count = 0
    
    # Iterate over tests
    for test, outcome in log.items():  
        
        # Check command line arguments and print results requested     
        if "s" in args[0] and outcome["result"] == "skip":
            print(test + " : " + outcome["result"])
        if "p" in args[0] and outcome["result"] == "pass":
            print(test + " : " + outcome["result"])
        if "f" in args[0] and outcome["result"] == "fail":
            print(test + " : " + outcome["result"])
            #Increment failed tests
            count += 1

        # Check command line arguments for --more and print doc info for tests.
        if args[1]:
            print([outcome["doc"]])

        # Print error message if the test failed
        if outcome["result"] == "fail":
            print(outcome['error'])
        print()
    return count

def capture_screenshot(driver: webdriver.Chrome, file_name: str):
    """
    Capture a screenshot of the current webpage selenium driver is on and save it
    to file using file_name.
    """
    driver.save_screenshot("auctions/static/tests/" + file_name + ".png")
    
def save_json(data: dict, file_name: str) -> None:
    """
    Save the passed data as file_name.json
    """
    with open(file_name,"w") as json_file:
        json.dump(data, json_file, indent=4)

def read_json(file_name: str) -> dict:
    """
    Reads data from file_name.json and returns a dict
    """
    with open(file_name,"r") as json_file:
        data = json.loads(json_file)
        return data
    
def reload_page(driver: webdriver.Chrome, url: str) -> webdriver.Chrome:
    """
    Closes the current webdriver and saves the cookies, then reloads webdriver and restarts the session using the save cookies.
    """
    # Save cookies
    pickle.dump(driver.get_cookies(), open("cookies.pkl","wb"))

    # Close driver and restart browser
    driver.close()
    driver = webdriver.Chrome()
    driver.get(url)

    # Reload cookies into session
    cookies = pickle.load(open("cookies.pkl","rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

    # Refresh the page and return the driver
    driver.get(url)
    return driver