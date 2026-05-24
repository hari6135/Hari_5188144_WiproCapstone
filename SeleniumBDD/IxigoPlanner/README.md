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

# Ixigo Trip Planner BDD Automation Framework

## Selenium WebDriver + Behave BDD + Page Object Model + Allure Reports

---

# Project Overview

The Ixigo Trip Planner Automation Framework is developed using Selenium WebDriver with Python Behave BDD framework to automate the major functionalities of the ixigo Trip Planner web application.

The framework validates:

- End-to-End Workflow
- Positive Test Scenarios
- Negative Test Scenarios
- Data-Driven Testing
- Behavior Driven Development (BDD)

The framework follows the Page Object Model (POM) design pattern for better maintainability, scalability and reusability.

---

# Features

- Selenium WebDriver Automation
- Behave BDD Framework
- Feature Files and Step Definitions
- Page Object Model (POM)
- Data-Driven Testing using Excel
- Professional Logging
- Screenshot Capture
- Allure Reporting
- Positive & Negative Testing
- End-to-End Workflow Validation

---

# Tech Stack

| Technology | Usage |
|---|---|
| Python | Programming Language |
| Selenium WebDriver | Browser Automation |
| Behave | BDD Framework |
| Allure Reports | Reporting |
| OpenPyXL | Excel Data Handling |
| Logging Module | Execution Logs |
| Chrome Browser | Test Execution |

---

# Framework Architecture

```text
IxigoPlannerBDD
│
├── config
├── features
│   ├── end_to_end.feature
│   ├── test_cases.feature
│   └── steps
│       ├── end_to_end_steps.py
│       └── test_cases_steps.py
│
├── logs
├── pages
├── reports
│   ├── allure-results
│   └── allure-report
│
├── screenshots
├── testdata
├── utils
├── environment.py
├── behave.ini
├── runtest.bat
└── requirements.txt
````

---

# BDD Implementation

The framework follows Behavior Driven Development using:

* Feature Files
* Step Definition Files
* Gherkin Syntax
* Given-When-Then Structure

Example:

```gherkin
Scenario: Verify complete ixigo trip planner workflow

Given user launches ixigo application

When user performs login flow for end to end

And user completes planner flow for end to end

Then flight details page should open successfully
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

# Positive Test Scenarios

### Positive Test Scenario 1 – Plan Page Navigation

* Validates successful navigation to planner page
* Verifies Plan module loading
* Checks planner URL navigation

---

### Positive Test Scenario 2 – Travel Month Selection

* Validates travel month selection
* Reads travel month dynamically from Excel
* Verifies selected month update successfully

---

### Positive Test Scenario 3 – Filter Selection Validation

* Validates category filter functionality
* Selects International category
* Applies Pollution Free filter
* Verifies successful filter application

---

### Positive Test Scenario 4 – Tourist Location Selection

* Validates tourist location card selection
* Selects destination country
* Opens tourist location details page
* Verifies successful navigation

---

# Negative Test Scenarios

### Negative Test Scenario 1 – Invalid Location Search

* Enters invalid location value
* Validates application error handling
* Verifies invalid destination error message
* Ensures unsupported location validation

---

### Negative Test Scenario 2 – Book Now Button Validation

* Selects unsupported route location
* Navigates to How To Reach section
* Verifies Book Now button absence
* Ensures unavailable routes cannot be booked

---

# Test Environment

| Component        | Description                 |
| ---------------- | --------------------------- |
| Operating System | Windows 10                  |
| IDE              | PyCharm Unified Product     |
| Browser          | Google Chrome               |
| Framework        | Selenium WebDriver + Behave |
| Reporting Tool   | Allure Reports              |
| Design Pattern   | Page Object Model           |
| Test Approach    | Behavior Driven Development |

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
* Pass/Fail scenario status
* Screenshot attachments
* Execution history
* Failure debugging
* Execution summary

---

# Logging

The framework uses Python logging module for detailed execution tracking.

Execution logs include:

* Browser launch details
* Scenario execution flow
* Assertions and validations
* Error handling
* Screenshot tracking

Logs are stored in:

```text
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

## Run End-to-End Feature

```bash
behave features/end_to_end.feature
```

---

## Run Test Cases Feature

```bash
behave features/test_cases.feature
```

---

# Generate Allure Report

```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
```

---

# Open Allure Report

```bash
allure serve reports/allure-results
```

---

# Test Summary

<div class="summary-box">

✔ Total Scenarios Executed: 7

✔ Scenarios Passed: 7

✔ Scenarios Failed: 0

✔ Automation Accuracy: 100%

</div>

---

# Conclusion

The Selenium Behave BDD automation framework successfully validates the ixigo Trip Planner application using End-to-End, Positive and Negative testing approaches.

The framework is developed using:

* Selenium WebDriver
* Behave BDD Framework
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

Overall, the project demonstrates a practical and professional BDD automation framework for real-world web application testing.


