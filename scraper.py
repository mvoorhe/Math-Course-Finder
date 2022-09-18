"""
Uses package BeautifulSoup4 to webscrape Purdue math class pages
for lecture information.
Created: Saturday, September 17, 2022
@author: Mary V (mvoorhe), Caitlin Wilson (Caitlin-Wilson-8642), Lexi Ogrinz (AOgrinz-pixel)
"""
import requests
from bs4 import BeautifulSoup
from array import *
filteredClasses = []  # Holds values of filtered classes
tempArr = []  # Holds values of course name, professor, time, etc.
course = 0  # Keeps track of index course is being put in filteredClasses array
identifierNum = 0  # Keeps track of which object is being pu in array


# Finds appropriate math course according to user input and returns
# new webpage to search through class information
class Math():
    def findclass(self, maclass, mprof, mday):
        filteredClasses = []
        tempArr = []
        course = 0
        identifierNum = 0
        main_page = requests.get("https://www.math.purdue.edu/academic/courses/")

        src = main_page.content
        soup = BeautifulSoup(src, 'lxml')

        links = soup.find_all("a")
        courseName = "MA " + maclass
        for link in links:
            if courseName in link.text:
                class_url = link.attrs['href']

        class_page = requests.get("https://www.math.purdue.edu/academic/courses/" + class_url)
        src = class_page.content
        class_soup = BeautifulSoup(src, 'lxml')

        if mprof != "none":
            prof_tags = class_soup.find_all("a")  # checks if there was a professor input
            for prof_classes in prof_tags:
                courseObj = prof_classes.parent.parent
                profNameForArray = str(courseObj.find('a').contents[0])  # professors name to put in array as a string
                if mprof in prof_classes.text:
                    tempArr = []
                    times = []
                    if mday != "none":  # checks if there was a weekday input
                        for available_days in courseObj:
                            if mday in available_days.text:
                                # For loop to check days
                                for times in available_days.parent:
                                    if ":" in times.text:
                                        roomNum = times.previous_sibling.previous_sibling.text
                                        tempArr = [courseName, profNameForArray, available_days.text, times.text,
                                                   roomNum]
                                        filteredClasses.append(tempArr)

                    else:  # Preference for professor but not days
                        # Print(prof_classes.parent.parent)
                        for times in courseObj:
                            if ":" in times.text:
                                availableDays = times.next_sibling.next_sibling.text
                                roomNum = times.previous_sibling.previous_sibling.text
                                tempArr = [courseName, profNameForArray, availableDays, times.text, roomNum]
                                filteredClasses.append(tempArr)

        elif mprof == "none" and mday != "none":  # No preferred professor, but a preferred date
            day_tags = class_soup.find_all("td")
            for available_days in day_tags:
                if mday in available_days.text:
                    # Print(available_days.parent)
                    for times in available_days.parent:
                        if ":" in times.text:
                            availableDays = times.next_sibling.next_sibling.text
                            roomNum = times.previous_sibling.previous_sibling.text
                            profNameForArray = str(times.next_sibling.next_sibling.next_sibling.next_sibling.text)
                            tempArr = [courseName, profNameForArray, availableDays, times.text, roomNum]
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

        return filteredClasses

test = Math()
print(test.findclass("16200", "Chen", "none"))
