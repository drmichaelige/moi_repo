# Created by babao at 4/23/2023
Feature: CareSkin Testing Practice

Scenario: User delete an item from the cart
Given Open CureSkin page
 When Click on a product
 Then Add items to the cart
 Then View cart
 Then Delete product from cart
 Then Verify cart is empty
