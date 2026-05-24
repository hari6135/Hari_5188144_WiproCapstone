<style>

body{
    font-family: "JetBrains Mono", monospace;
    background-color: #2b2b2b;
    color: #a9b7c6;
    line-height: 1.7;
    padding: 20px;
}

h1{
    color: #ffc66d;
    border-bottom: 1px solid #3c3f41;
    padding-bottom: 10px;
    margin-top: 35px;
    font-weight: 600;
}

h2{
    color: #9876aa;
    margin-top: 30px;
    font-weight: 600;
}

h3{
    color: #6897bb;
    margin-top: 25px;
    font-weight: 600;
}

p{
    color: #a9b7c6;
}

table{
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
    margin-bottom: 20px;
    background-color: #313335;
}

table, th, td{
    border: 1px solid #3c3f41;
}

th{
    background-color: #3c3f41;
    color: #a9b7c6;
    padding: 12px;
    text-align: left;
}

td{
    padding: 10px;
    color: #a9b7c6;
}

code{
    background-color: #3c3f41;
    color: #a5c261;
    padding: 3px 6px;
    border-radius: 4px;
    font-family: "JetBrains Mono", monospace;
}

pre{
    background-color: #313335;
    color: #a9b7c6;
    padding: 15px;
    border-radius: 6px;
    overflow-x: auto;
    border: 1px solid #3c3f41;
    font-family: "JetBrains Mono", monospace;
}

hr{
    border: 1px solid #3c3f41;
    margin-top: 35px;
    margin-bottom: 35px;
}

ul li{
    margin-bottom: 8px;
}

blockquote{
    border-left: 4px solid #3c3f41;
    padding-left: 15px;
    color: #808080;
}

.summary-box{
    background-color: #313335;
    border: 1px solid #3c3f41;
    padding: 20px;
    border-radius: 6px;
    margin-top: 20px;
}

</style>

# Ixigo Trip Planner Automation Framework

## Selenium WebDriver + PyTest + Page Object Model + Allure Reports

---

# Project Overview

The Ixigo Trip Planner Automation Framework is developed using Selenium WebDriver with Python PyTest framework to
automate the major functionalities of the ixigo Trip Planner web application.

The framework validates:

* End-to-End Workflow
* Positive Test Scenarios
* Negative Test Scenarios
* Data-Driven Testing

The framework follows the Page Object Model (POM) design pattern for better maintainability, scalability and
reusability.

---

# Features

* Selenium WebDriver Automation
* PyTest Framework
* Page Object Model (POM)
* Data-Driven Testing using Excel
* Professional Logging
* Screenshot Capture
* Allure Reporting
* Positive & Negative Testing
* End-to-End Workflow Validation

---

# Tech Stack

| Technology         | Usage                |
|--------------------|----------------------|
| Python             | Programming Language |
| Selenium WebDriver | Browser Automation   |
| PyTest             | Test Framework       |
| Allure Reports     | Reporting            |
| OpenPyXL           | Excel Data Handling  |
| Logging Module     | Execution Logs       |
| Chrome Browser     | Test Execution       |

---

# Framework Architecture

```text id="rd1"
IxigoTripPlanner
│
├── config
├── logs
├── pages
├── reports
│   ├── allure-results
│   └── allure-report
│
├── screenshots
├── testdata
├── tests
├── utils
├── conftest.py
├── pytest.ini
└── requirements.txt
```

---

# Test Coverage

## End-to-End Test Flow

The framework validates the complete business workflow including:

* User Login
* Planner Navigation
* Travel Month Selection
* Source Location Selection
* Travel Filter Application
* Tourist Location Selection
* Google Map Verification
* Book Now Navigation
* Flight Details Verification

---

# Positive Test Cases

### Positive Test Case 1 – Plan Page Navigation

* Validates successful navigation to planner page
* Verifies Plan module loading
* Checks planner URL navigation

---

### Positive Test Case 2 – Travel Month Selection

* Validates travel month selection
* Reads travel month dynamically from Excel
* Verifies selected month update successfully

---

### Positive Test Case 3 – Filter Selection Validation

* Validates category filter functionality
* Selects International category
* Applies Pollution Free filter
* Verifies successful filter application

---

### Positive Test Case 4 – Tourist Location Selection

* Validates tourist location card selection
* Selects destination country
* Opens tourist location details page
* Verifies successful navigation

---

# Negative Test Cases

### Negative Test Case 1 – Invalid Location Search

* Enters invalid location value
* Validates application error handling
* Verifies invalid destination error message
* Ensures unsupported location validation

---

### Negative Test Case 2 – Book Now Button Validation

* Selects unsupported route location
* Navigates to How To Reach section
* Verifies Book Now button absence
* Ensures unavailable routes cannot be booked

---

# Test Environment

| Component        | Description                 |
|------------------|-----------------------------|
| Operating System | Windows 10                  |
| IDE              | PyCharm Unified Product     |
| Browser          | Google Chrome               |
| Framework        | Selenium WebDriver + PyTest |
| Reporting Tool   | Allure Reports              |
| Design Pattern   | Page Object Model           |

---

# Test Data Strategy

The framework uses Excel files for dynamic test data handling.

The framework reads:

* Login Data
* Planner Data
* Filter Data
* Tourist Location Data

This improves:

* Maintainability
* Reusability
* Scalability

---

# Reporting

## Allure Reports

The framework integrates Allure Reports for professional execution reporting.

Features include:

* Step-by-step execution flow
* Pass/Fail status
* Screenshot attachments
* Execution history
* Failure debugging
* Execution summary

---

# Logging

The framework uses Python logging module for detailed execution tracking.

Execution logs include:

* Browser launch details
* Test execution flow
* Assertions and validations
* Error handling
* Screenshot tracking

Logs are stored in:

```text id="rd2"
logs/automation.log
```

---

# Screenshot Capture

Screenshots are automatically captured during important execution stages including:

* Planner Page
* Filter Page
* Tourist Location Page
* Google Map Verification
* Invalid Location Validation
* Flight Details Page

---

# Test Execution

## Run All Tests

```bash id="rd3"
pytest
```

---

## Run Specific Test File

```bash id="rd4"
pytest tests/test_end_to_end.py
```

---

# Generate Allure Report

```bash id="rd5"
pytest --alluredir=reports/allure-results
```

---

# Open Allure Report

```bash id="rd6"
allure serve reports/allure-results
```

---

# Test Summary

<div class="summary-box">

✔ Total Tests Executed: 7

✔ Tests Passed: 7

✔ Tests Failed: 0

✔ Automation Accuracy: 100%

</div>

---

# Conclusion

The Selenium PyTest automation framework successfully validates the ixigo Trip Planner application using End-to-End,
Positive and Negative testing approaches.

The framework is developed using:

* Selenium WebDriver
* PyTest Framework
* Page Object Model
* Allure Reporting
* Data-Driven Testing
* Logging Framework

The framework improves:

* Test maintainability
* Reusability
* Scalability
* Reporting quality
* Automation reliability

Overall, the project demonstrates a practical and professional Selenium automation framework for real-world web
application testing.
