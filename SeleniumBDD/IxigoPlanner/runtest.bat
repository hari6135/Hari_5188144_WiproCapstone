@echo off

echo ----------------------- DELETING OLD ALLURE REPORTS -------------------------

rmdir /s /q reports\allure-results
rmdir /s /q reports\allure-report

echo ------------------------- RUNNING BEHAVE TEST --------------------------------

behave %1

echo --------------------- GENERATING ALLURE REPORT --------------------------------

call allure generate reports/allure-results -o reports/allure-report

echo --------------------- OPENING ALLURE REPORT -----------------------------------

call allure open reports/allure-report