"""
Uses package BeautifulSoup4 to webscrape Purdue math class pages
for lecture information.

Created: Saturday, September 17, 2022

@author: Mary V (mvoorhe), Caitlin Wilson (Caitlin-Wilson-8642), Lexi Ogrinz (AOgrinz-pixel)

"""

import requests
from bs4 import BeautifulSoup

# Finds appropriate math course according to user input and returns
# new webpage to search through class information
main_page = requests.get("https://www.math.purdue.edu/academic/courses/")
keyword = input("What math class are you looking for (5 digit number)?\n")

src = main_page.content
soup = BeautifulSoup(src, 'lxml')

links = soup.find_all("a")
for link in links:
    if "MA " + keyword in link.text:
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

# Returning table data sets according
# to user input

if prof_name != "none":
    prof_tags = class_soup.find_all("a")                            # checks if there was a professor input
    for prof_classes in prof_tags:
        if prof_name in prof_classes.text:
            if days != "none":                                      # checks if there was a weekday input
                for available_days in prof_classes.parent.parent:
                    if days in available_days.text:
                        print(available_days.parent)
            else:
                print(prof_classes.parent.parent)
elif prof_name == "none" and days != "none":                        # checks if there was NOT a professor
    day_tags = class_soup.find_all("td")
    for available_days in day_tags:
        if days in available_days.text:
            print(available_days.parent)
else:
    table_rows = class_soup.find("table", {"class": "table table-condensed"})
    print(table_rows)
