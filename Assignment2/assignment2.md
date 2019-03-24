# Assignment 2: Classifier

> Due: 11:59 PM, Wednesday, April 3

## Overview

This assignment aims to give you practice with a few of the Python fundamentals we've covered in class. Specifically, you will use your knowledge about functions, data structures and file input/output.

In this assignment you will write code to classify a students and professors list.

- _Expected Time: 90 mins_
- _Max Time: 180 mins_

Note: Get started early! We want to resolve any confusions or submission problems earlier rather than later.

## Review

If you would like to, get a quick refresher by flipping through our slides from the past weeks on the [course website](https://koltpython.github.io/lecture).

## Starter Code

Please get your starter code [here](https://github.com/koltpython/python-assignments/raw/master/Assignment2/assignment2.zip).

## Tasks

You will write a code which reads a three column file named 'list.txt' where the first column is the title determines if the person a 'Student' or a 'Professor', second column is the name of the person and the third column is the age of that person. Both the title and name consist of a single word and three of them are separated by one space. \
\
Here are some lines from the file:

Student Marcia 23\
Professor Jami 42\
Professor Elizabeth 32\
Student Aimee 21\
Professor Ashanti 55\
Student Sonny 19\
Student Blanche 25

### Task 1 : Reading The File

You should create a dictionary as
`{'students': {}, 'professors': {}}`. In this dictionary, 'students' and 'professors' are keys that have dictionaries as values. In those inner dictionaries, you should keep person name as key and his/her age as its value. The code should read the file line by line, split the contents of a line and determines where to add informations into the dictionary.

For example,\
`{'students': {'Marcia': '23', 'Aimee': '21', 'Sonny': '19', 'Blanche': '25'}, 'professors': {'Jami': '42', 'Elizabeth': '32', 'Ashanti': '55'}}` \
is how the dictionary should be after we added seven people in the upper list.

If there are more than one person with same title and name, then they represent the same person. So, you should update the age of that person instead of adding a new person into the dictionary.

For example, if there is another Professor Elizabeth with age 25 in the file, then the dictionary will be updated as in the following:\
`{'students': {'Marcia': '23', 'Aimee': '21', 'Sonny': '19', 'Blanche': '25'}, 'professors': {'Jami': '42', 'Elizabeth': '25', 'Ashanti': '55'}}`

However, notice that Student Elizabeth and Professor Elizabeth are two different people.

### Task 2: Sorting

After you have added every person into the dictionary, you should sort the students and professors separately by their ages. You can implement a function which sorts dictionaries by their values to handle this task.

> **Hint:** dictionary.values() gives you the values in a dictionary and you can sort values by sorted() function which is already implemented in Python. However, your task is to sort dictionaries by using this sorted values.

### Task 3: Writing Into Files

If your dictionary is as desired above, you are ready for this final task. Create two files named 'students.txt' and 'professors.txt' and write each person into the corresponding file as name and age line by line.

For example, 'professors.txt' includes these lines:

Marybeth 28\
Aleen 29\
Rayford 30\
Lucinda 30\
Danyelle 31\
Elizabeth 32\
Agatha 35\
Delores 37\
Amanda 37\
Colby 37

You can check your txt files which should appear into your workspace. If you have these two files with names and ages in sorted order, congrats, you've finished your second homework successfully.

For further questions, please don't hesitate to contact [ikoprululu16@ku.edu.tr](mailto:ikoprululu16@ku.edu.tr).

## Grading

Your grade for this assignment will be assessed on completion. If you successfully submit a Python program that largely follows the specification above, you will receive full credit on this assignment. We will not be very strict on edge cases, although we encourage you to attempt to match the above specification exactly.

We will be leaving feedback on your implementation and style, please check our feedbacks and ask questions about the parts you didn't understand.

## Submission

To submit your solution, login into [OK website](https://okpy.org) by using your Koc email address. The assignment submission page is under the course named **Python Certificate Program (Spring 2019)** which is already shared with you. All you have to do is to choose the assignment you solved and create a new submission. Drag and drop your code into the specified place, and submit it. You should omit the text files and submit a single file named `assignment2.py` for this assignment.
