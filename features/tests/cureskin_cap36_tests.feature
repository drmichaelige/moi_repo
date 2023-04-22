# Created by babao at 4/19/2023
Feature: CureSkin Website Search

Scenario: User can access search
Given Open CureSkin page
 When Click on the search icon
 Then Input text SPF
 Then Click to search
 Then Verify the results have spf



