"""
Uses package BeautifulSoup4 to webscrape Purdue math class pages
for lecture information.
Created: Saturday, September 17, 2022
@author: Mary V (mvoorhe), Caitlin Wilson (Caitlin-Wilson-8642), Lexi Ogrinz (AOgrinz-pixel)
"""
import numpy
import requests
from bs4 import BeautifulSoup
from array import *
import pandas as pd

filteredClasses = []  # Holds values of filtered classes
tempArr = []  # Holds values of course name, professor, time, etc.
course = 0  # Keeps track of index course is being put in filteredClasses array
identifierNum = 0  # Keeps track of which object is being pu in array

# Finds appropriate math course according to user input and returns
# new webpage to search through class information
main_page = requests.get("https://www.math.purdue.edu/academic/courses/")
keyword = input("What math class are you looking for (5 digit number)?\n")

src = main_page.content
soup = BeautifulSoup(src, 'lxml')

links = soup.find_all("a")
courseName = "MA " + keyword
for link in links:
    if courseName in link.text:
        class_url = link.attrs['href']

class_page = requests.get("https://www.math.purdue.edu/academic/courses/" + class_url)
src = class_page.content
class_soup = BeautifulSoup(src, 'lxml')

# Finds class information for classes taught by
# user-inputted teacher
prof_name = "none"

teacher_preference = input("Do you have a preference on who teaches the class?\n").lower()
if teacher_preference == "yes":
    prof_name = input("What is the teacher's last name?\n").capitalize()

# Finds class information for classes that occur
# on specific days of the week
days = "none"

day_preference = input("Do you care about what days the class is held on?\n").lower()
if day_preference == "yes":
    days = input("What day(s) do you want (single letter representation)?\n").upper()

# Objects that will help return class times

# Returning table data sets according
# to user input

if prof_name != "none":
    prof_tags = class_soup.find_all("a")  # checks if there was a professor input
    for prof_classes in prof_tags:
        courseObj = prof_classes.parent.parent
        profNameForArray = str(courseObj.find('a').contents[0])  # professors name to put in array as a string
        if prof_name in prof_classes.text:
            tempArr = []
            times = []
            if days != "none":  # checks if there was a weekday input
                for available_days in courseObj:
                    if days in available_days.text:
                        # For loop to check days
                        for times in available_days.parent:
                            if ":" in times.text:
                                # print(times.text)
                                roomNum = times.previous_sibling.previous_sibling.text
                                # print(roomNum)
                                # print(available_days.text)
                                tempArr = [courseName, profNameForArray, available_days.text, times.text, roomNum]
                                filteredClasses.append(tempArr)

            else:  # Preference for professor but not days
                # Print(prof_classes.parent.parent)
                for times in courseObj:
                    if ":" in times.text:
                        # print(times.text)
                        roomNum = times.previous_sibling.previous_sibling.text
                        # print(roomNum)
                        availableDays = times.next_sibling.next_sibling.text
                        tempArr = [courseName, profNameForArray, availableDays, times.text, roomNum]
                        filteredClasses.append(tempArr)

elif prof_name == "none" and days != "none":  # No preferred professor, but a preferred date
    day_tags = class_soup.find_all("td")
    for available_days in day_tags:
        if days in available_days.text:
            # Print(available_days.parent)
            for times in available_days.parent:
                if ":" in times.text:
                    print(times.text)
                    roomNum = times.previous_sibling.previous_sibling.text
                    print(roomNum)
                    profNameForArray = str(times.next_sibling.next_sibling.next_sibling.next_sibling.text)
                    if days in available_days.text:
                        tempArr = [courseName, profNameForArray, available_days.text, times.text, roomNum]
                        filteredClasses.append(tempArr)

else:  # No preferred Professor or Date
    table = class_soup.find("table", {"class": "table table-condensed"})
    table_rows = table.find("tbody")
    table_data = table_rows.find_all("td")
    # print(table_data)
    for times in table_data:
        if ":" in times.text:
            # print(times.text)
            roomNum = times.previous_sibling.previous_sibling.text
            # print(roomNum)
            availableDays = times.next_sibling.next_sibling.text
            profNameForArray = str(times.next_sibling.next_sibling.next_sibling.next_sibling.text)
            tempArr = [courseName, profNameForArray, availableDays, times.text, roomNum]
            filteredClasses.append(tempArr)

tempArr = []
for i in filteredClasses:
    if i not in tempArr:
        tempArr.append(i)

filteredClasses = tempArr

print(filteredClasses)
