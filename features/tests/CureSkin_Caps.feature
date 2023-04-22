# Created by babao at 4/21/2023
Feature: CureSkin Caps set

Scenario: User can search for a product
Given Open CureSkin page
 When Click on the search field
 Then Search for CureSkin gel
 Then Verify search results are shownCureSkicure
#
#Scenario: Top logo takes to the main page
#Given Open search results page
# When Click on CureSkin logo in the header
# Then Verify user is taken to the main page
#
#Scenario: User can shop by product Face Washes
#Given Open the main page
# When Click on "Shop by product" - select Face Washes
# Then Verify "Face Wash" is shown
#
#Scenario: User can shop by product Sunscreens
#Given Open main page
# When Click to "Shop by product" - select Sunscreens
# Then Verify the fist product in Sunsreen
#
#Scenario: User can shop by category Face
#Given Open main page
# When Click to "Shop by category" - select Face
# Then Verify "Face" header is shown
#
#Scenario: User can shop by category Body
#Given Open main page
#When Click to "Shop by category" - select Body
#Then Verify "Body" header is shown
#Scenario: Search results UI is correct
#Given Open search results page
# When Verify first results have name, image, and price
#
#Scenario: Search results show the right result
#Given Open main page
# When From page footer, click "Search"
# Then Search for the SPF
#
#Scenario: Search results can be sorted by prices (high - low)
#Given Open search results page
# When Select sort by proce, high to low
# Then Verify filter applied (fist product price should be > last product price)
#
#Scenario: Product Details page can be accesed from Search Results
#Given Open search results page
# When Store the name of the 1st product
# Then Click on the 1st product
