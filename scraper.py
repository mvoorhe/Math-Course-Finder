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
class Math():
    def findclass(self, mclass, mprof, mday):
        main_page = requests.get("https://www.math.purdue.edu/academic/courses/")

        src = main_page.content
        soup = BeautifulSoup(src, 'lxml')

        links = soup.find_all("a")
        courseName = "MA " + mclass
        for link in links:
            if courseName in link.text:
                class_url = link.attrs['href']

        class_page = requests.get("https://www.math.purdue.edu/academic/courses/" + class_url)
        src = class_page.content
        class_soup = BeautifulSoup(src, 'lxml')


        # Finds class information for classes taught by
        # user-inputted teacher



        # Finds class information for classes that occur
        # on specific days of the week




        # Objects that will help return class times

        # Returning table data sets according
        # to user input

        if mprof != "none":
            prof_tags = class_soup.find_all("a")  # checks if there was a professor input
            for prof_classes in prof_tags:
                courseObj = prof_classes.parent.parent
                profNameForArray = str(courseObj.find('a').contents[0])  # professors name to put in array as a string
                if mprof in prof_classes.text:
                    tempArr = []
                    times = []
                    if mday != "none":                                      # checks if there was a weekday input
                        for available_days in courseObj:
                            # For loop to check days
                            mday.upper()
                            arrDays = []
                            for element in range(0, len(mday)):
                                if mday[element] in available_days.text:
                                    for times in available_days.parent:
                                        if ":" in times.text:
                                            print(times.text)
                                            roomNum = times.previous_sibling.previous_sibling.text
                                            print(roomNum)
                                            tempArr = [courseName, profNameForArray, available_days.text, times.text, roomNum]
                                            arrDays.append(tempArr)
                          #  for a in arrDays:
                             # for b in range(len(arrDays) - 1):
                                 # if not (numpy.array_equal(arrDays[a], arrDays[b], equal_nan=False)):


                            if mday in available_days.text:  # Days is user input
                                # Print(available_days.parent)
                                for times in available_days.parent:
                                    if ":" in times.text:
                                        print(times.text)
                                        roomNum = times.previous_sibling.previous_sibling.text
                                        print(roomNum)
                                        tempArr = [courseName, profNameForArray, available_days.text, times.text, roomNum]
                                        filteredClasses.append(tempArr)  # Preference for professor and days

                    else:  # Preference for professor but not days
                        # Print(prof_classes.parent.parent)
                        for times in courseObj:
                            if ":" in times.text:
                                print(times.text)
                                roomNum = times.previous_sibling.previous_sibling.text
                                print(roomNum)
                                tempArr = [courseName, profNameForArray, times.text, roomNum]
                                filteredClasses.append(tempArr)

        elif mprof == "none" and mday != "none":  # No preferred professor, but a preferred date
            day_tags = class_soup.find_all("td")
            for available_days in day_tags:
                if mday in available_days.text:
                    # Print(available_days.parent)
                    for times in available_days.parent:
                        if ":" in times.text:
                            print(times.text)
                            roomNum = times.previous_sibling.previous_sibling.text
                            print(roomNum)
                            tempArr = [courseName, available_days.text, times.text, roomNum]
                            filteredClasses.append(tempArr)

        else:  # No preferred Professor or Date
            table = class_soup.find("table", {"class": "table table-condensed"})
            table_rows = table.find("tbody")
            table_data = table_rows.find_all("td")
            # print(table_data)
            for times in table_data:
                if ":" in times.text:
                    print(times.text)
                    roomNum = times.previous_sibling.previous_sibling.text
                    print(roomNum)
                    tempArr = [courseName, times.text, roomNum]
                    filteredClasses.append(tempArr)

        return filteredClasses
