# Created by babao at 5/1/2023
Feature: Integrate your tests with a Cloud Testing Platform

Scenario: User can search for a product that doesn't exist
Given Open CureSkin page
 When Click on the search icon
 Then Input non-existent product name: Bicycle to search
 Then Click to search
 Then Verify no results found

 Scenario: User delete an item from the cart
Given Open CureSkin page
 When Click on a product
 Then Add items to the cart
 Then View cart
 Then Delete product from cart
 Then Verify cart is empty




#The Task
#Open web application CureSkin - Skin care products approved by dermatologists
#Create a free BrowserStack account
#Run all your tests in BrowserStack and make sure they work
#It’d be better to pick a different platform. If you’re on Mac, try running
#tests on Windows in BrowserStack; if you’re on Windows, try running tests on Mac.