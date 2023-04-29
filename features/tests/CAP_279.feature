# Created by babao at 4/28/2023
Feature: Make your tests cross-browser and run them headlessly

Scenario: User can search for a product that doesn't exist
Given Open CureSkin page
 When Click on the search icon
 Then Input non-existent product name: Bicycle to search
 Then Click to search
 Then Verify no results found


#Description
#Open web application CureSkin - Skin care products approved by dermatologists
#Make your tests cross-browser and run them headlessly:
#Run your tests(from task 2) in the headless mode of Google Chrome.
#Fix the tests to run in headless mode if they fail.
#Install the Firefox browser and make sure all your automated tests run
#in the Firefox browser. Fix the tests if they fail in Firefox.
# Copy and past the link to your GitHun under task 3 once you are done.