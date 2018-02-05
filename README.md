This repository contains a small library for printing supermarket receipts.
Its written in python 2.x because that's what I'm working with at the moment.

As of now, the user input is API based, requiring the user of the library to provide Item and Discount objects.
These are found at the top of the supermarket.py file.

Discounts are specified by writing a rule function that applies to all items.
This makes it very general, allowing pretty much any discount to be specified.
It does, however have the disadvantage that the user has to write a discount function in python,
which may be beyond the supermarket management.

If we are to roll this out, some kind of UI will need to be designed to enable people to enter specific types of discount.