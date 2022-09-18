"""
Uses package BeautifulSoup4 to webscrape Purdue math class pages
for lecture information.

Created: Saturday, September 17, 2022

@author: Mary V (mvoorhe), Caitlin Wilson (Caitlin-Wilson-8642), Lexi Ogrinz (AOgrinz-pixel)

"""

import requests
from bs4 import BeautifulSoup
from array import *
import pandas as pd
filteredClasses = []  # Holds values of filtered classes
tempArr = []  # Holds values of course name, professor, time, etc.
course = 0  # Keeps track of index course is being put in filteredClasses array
identifierNum = 0  # Keeps track of which object is being pu in array
# 0 is Course Title
# 1 is Professor


main_page = requests.get("https://www.math.purdue.edu/academic/courses/")
keyword = input("What math class are you looking for (5 digit number)?\n")

src = main_page.content
soup = BeautifulSoup(src, 'lxml')

links = soup.find_all("a")
courseName = "MA " + keyword
for link in links:
    if courseName in link.text:
        class_url = link.attrs['href']
        # print(class_url)

class_page = requests.get("https://www.math.purdue.edu/academic/courses/" + class_url)
# print(class_page)

src = class_page.content
class_soup = BeautifulSoup(src, 'lxml')

teacher_preference = input("Do you have a preference on who teaches the class?\n").lower()
if teacher_preference == "yes":
    prof_name = input("What is the teacher's last name?\n").capitalize()
    print(prof_name)

prof_tags = class_soup.find_all("a")
identifierNum = 1
course = 0
for prof_classes in prof_tags:
    if prof_name in prof_classes.text:
        classObj = prof_classes.parent.parent  # Sets class as an object to put in array
        print(classObj)
        # print("The type of this is..." + str(type(classObj)))
        profNameForArray = str(classObj.find('a').contents[0])  # professors name to put in array as a string
        # print(type(profNameForArray))

        filteredClasses.insert([course][0], courseName)
        print(type(courseName))
        print(type(profNameForArray))

    course += 1


day_preference = input("Do you care about what days the class is held on?\n").lower()
days = "none"
if day_preference == "yes":
    days = input("What day(s) do you want (conditions for input)?\n").upper()

day_tags = class_soup.find_all("td")
for available_days in day_tags:
    if days in available_days.text:
        print(available_days.parent)

print(filteredClasses)
# Goals: get elements from class and out into 3d array
# Send array to javascript
# https://stackoverflow.com/questions/59951283/convert-python-list-to-java-array-using-py4j

