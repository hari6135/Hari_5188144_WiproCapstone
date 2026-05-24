<div align="center">

# Hari_5188144_WiproCapstone

### Selenium Automation Frameworks using PyTest & Behave BDD

<img src="https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/Selenium-Automation-green?style=for-the-badge&logo=selenium"/>
<img src="https://img.shields.io/badge/PyTest-Framework-orange?style=for-the-badge&logo=pytest"/>
<img src="https://img.shields.io/badge/Behave-BDD-yellow?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Allure-Reports-purple?style=for-the-badge"/>

</div>

---

# Project Overview

This repository contains two complete Selenium Automation Frameworks developed for the Wipro Capstone Project.

The project automates the **Ixigo Trip Planner Web Application** using:

- Selenium WebDriver
- Python
- PyTest Framework
- Behave BDD Framework
- Page Object Model (POM)
- Allure Reports

The repository demonstrates:

- End-to-End Automation
- Positive Testing
- Negative Testing
- Data-Driven Testing
- BDD Automation
- Professional Reporting
- Logging & Screenshot Capture

---

# Repository Structure

```text
Hari_5188144_WiproCapstone
│
├── SeleniumBDD
│   └── IxigoPlanner
│
├── SeleniumPytest
│   └── IxigoTripPlanner
│
└── README.md
```

---

# Selenium PyTest Framework

## Features

- Selenium WebDriver Automation
- PyTest Framework
- Page Object Model (POM)
- Excel Data-Driven Testing
- Allure Reports
- Screenshot Capture
- Logging Framework
- Positive & Negative Testing
- End-to-End Workflow Validation

---

## PyTest Framework Architecture

```text
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

## PyTest Test Coverage

| S.No | Test Type | Scenario | Status |
|---|---|---|---|
| 1 | End-to-End | Complete Trip Planner Workflow | Passed |
| 2 | Positive | Plan Page Navigation | Passed |
| 3 | Positive | Travel Month Selection | Passed |
| 4 | Positive | Filter Selection Validation | Passed |
| 5 | Positive | Tourist Location Selection | Passed |
| 6 | Negative | Invalid Location Search | Passed |
| 7 | Negative | Book Now Button Validation | Passed |

---

## Execute PyTest Framework

### Run All Tests

```bash
pytest
```

---

### Generate Allure Report

```bash
pytest --alluredir=reports/allure-results
```

---

### Open Allure Report

```bash
allure serve reports/allure-results
```

---

# Selenium Behave BDD Framework

## Features

- Selenium WebDriver Automation
- Behave BDD Framework
- Gherkin Feature Files
- Step Definition Files
- Page Object Model (POM)
- Allure Reports
- Screenshot Capture
- Logging Framework
- Data-Driven Testing
- Positive & Negative Testing

---

## BDD Framework Architecture

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
```

---

## BDD Test Coverage

| S.No | Test Type | Scenario | Status |
|---|---|---|---|
| 1 | End-to-End | Complete Trip Planner Workflow | Passed |
| 2 | Positive | Plan Page Navigation | Passed |
| 3 | Positive | Travel Month Selection | Passed |
| 4 | Positive | Filter Selection Validation | Passed |
| 5 | Positive | Tourist Location Selection | Passed |
| 6 | Negative | Invalid Location Search | Passed |
| 7 | Negative | Book Now Button Validation | Passed |

---

## Execute BDD Framework

### Run End-to-End Feature

```bash
behave features/end_to_end.feature
```

---

### Run Test Cases Feature

```bash
behave features/test_cases.feature
```

---

### Generate Allure Report

```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
```

---

### Open Allure Report

```bash
allure serve reports/allure-results
```

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Selenium WebDriver | Browser Automation |
| PyTest | Automation Framework |
| Behave | BDD Framework |
| Allure Reports | Reporting |
| OpenPyXL | Excel Data Handling |
| Logging Module | Execution Logs |
| Chrome Browser | Test Execution |

---

# Test Automation Highlights

- Complete End-to-End Automation
- Positive & Negative Test Coverage
- Reusable Page Object Model
- Professional Allure Reports
- Screenshot Evidence
- Detailed Logging
- Excel Data-Driven Testing
- Modular Framework Design
- Maintainable Automation Architecture

---

# Allure Reporting Features

- Step-by-step execution tracking
- Pass / Fail scenario status
- Screenshot attachments
- Execution history
- Detailed execution summary
- Failure debugging support

---

# Logging & Screenshot Support

The frameworks automatically generate:

- Execution Logs
- Screenshot Evidence
- Validation Checkpoints
- Failure Tracking

---

# Test Summary

| Framework | Executed | Passed | Failed | Accuracy |
|---|---|---|---|---|
| Selenium PyTest | 7 | 7 | 0 | 100% |
| Selenium Behave BDD | 7 | 7 | 0 | 100% |

---

# Developed By

## Hariharan M

- Wipro Capstone Project
- Selenium Automation Engineer
- Python Automation Testing
- BDD Automation Framework Development

---

# Conclusion

This repository demonstrates professional Selenium Automation Framework development using both:

- PyTest Framework
- Behave BDD Framework

The frameworks successfully implement:

- End-to-End Testing
- Positive Testing
- Negative Testing
- Data-Driven Testing
- Page Object Model
- Allure Reporting
- Logging & Screenshot Automation

The project showcases scalable, reusable and industry-standard automation testing practices for real-world web applications.

---

<div align="center">

### Wipro Capstone Project B2

⭐ Selenium Automation Framework Repository ⭐

</div>