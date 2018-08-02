# AnswerDigital-Test

Summary:
This is a code test for Answer Digital.

This project allows the user to easily perform UI web-app testing using Python and Selenium.
It supports testing in 'Internet Explorer', 'EDGE', 'FireFox', & 'Chrome'.

Requirements:

* Python 3-32bit
* Selenium (pip install selenium)
* Nose Tests (pip install nose)
* At least one WebDriver

Setup Instructions:

1. Set the base URL in the strings.py file located in the Values folder
2. Set the driver_path in the strings.py file to the folder where the webdriver .exes are located
3. Set the 'webdriver' environment variable to 'CHROME', 'IE' 'FIREFOX' or 'EDGE' (If not set, it will default to chrome)

To run:

Open a command prompt window and type *nosetests "{project_directory}/AnswerDigital-Test/TestCases"* and press enter 

