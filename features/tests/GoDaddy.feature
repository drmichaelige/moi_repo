# Created by babao at 5/3/2023
Feature: Automate GoDaddy.com
 ##Launch browser of your choice say., Firefox, chrome etc.
Scenario: Open Godaddy.com and maximize browser window.
Given Open godaddy page
 When Maximize browser window
 Then Close browser


Scenario: Open Godaddy.com and Print it's Page title.
Given Open godaddy page
 When Maximize browser window
 Then Get Title of page and print it
 Then Get URL of current page and print it
 Then Close browser

Scenario: Open Godaddy.com and Validate Page Title
Given Open godaddy page
 When Maximize browser window
 Then Get Title of page and validate it with expected value
 Then Get URL of current page and validate it with expected value
 Then Get Page source of web page
 Then Validate that page title is present in page source
 Then Close browser
