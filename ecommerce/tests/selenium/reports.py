from datetime import date
import csv

def log_result(test_name, test_result, log):
    log.append(f"{test_name}: {test_result}")

def read_log(file_name):
    with open(file_name, "r") as log:
        pass