# Created by babao at 4/21/2023
Feature: Product Search

Scenario: User can search for a product that doesn't exist
Given Open CureSkin page
 When Click on the search icon
 Then Input non-existent product name: Bicycle to search
 Then Click to search
 Then Verify no results found


