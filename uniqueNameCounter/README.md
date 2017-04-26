# Unique Name Counter challenge:

Count number of unique names in a transaction:

Write a function countUniqueNames(billFirstName,billLastName,shipFirstName,shipLastName,billNameOnCard) that counts the number of unique names in a transaction.

billFirstName - the first name in the billing address form (could include middle names)
billLastName - the last name in the billing address form
shipFirstName - the first name in the shipping address form (could include middle names)
shipLastName - the last name in the shipping address form
billNameOnCard - the full name as it appears on the credit card.

You should be able to handle middle names, nicknames and editing typos:

countUniqueNames(“Deborah”,”Egli”,”Deborah”,”Egli”,”Deborah Egli”) returns 1

countUniqueNames(“Deborah”,”Egli”,”Debbie”,”Egli”,”Debbie Egli”) returns 1

countUniqueNames(“Deborah”,”Egni”,”Deborah”,”Egli”,”Deborah Egli”) returns 1

countUniqueNames(“Deborah S”,”Egli”,”Deborah”,”Egli”,”Egli Deborah”) returns 1

countUniqueNames(“Michele”,”Egli”,”Deborah”,”Egli”,”Michele Egli”) returns 2

# My Solution:

I chose to write the solution in python.
The solution contains two files:
uniqueNameCounter.py - represents the solution to the challenge
unitTest.py - represents the unit tester for my solution

You can run the testing by typing the following command:
```python
PATH_TO_PROJECT>python unitTest.py
```
My solution starts by checking if the middle names on the bill and ship names represents the same person,
if one of them doesn't contains a middle name we should pass the check, but if both of them contains middle
names we should compare them, and if they are not equal we need to preform a typo check.
In case of one char middle name we need to compare the middle names because different one char middle names doesn't
represents the same person.

After that, if the middle names represents different persons we need to move to the card name and compare it to both
ship name and bill name, we need to make sure that they are both match the card name, otherwise we need to increment our
unique person counter.
If the middle names aren't unique we need to make sure that the ship name matches the bill name, and make sure that they are
matching also the name on the card.

In order to do the compare I wrote a function that compares the names and returns True if they are unique and false otherwise,
this function first checks, if the names are equal, and then (if they aren't equal) it checks if there is a typo mistake,
and if it's not a typo mistake the function checks if one of the names is a nickname of the other name.
