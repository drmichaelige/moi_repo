# Created by babao at 4/24/2023
Feature: CareSkin Testing Practice

Scenario: User delete an item from the cart
Given Open CureSkin page
 When Click on Shop All section
 Then Adjust Price Filter to change products number
 Then Verify that number of products changes
 Then Verify that products displayed are within the Price filter
