"""
Uses package BeautifulSoup4 to webscrape Purdue math class pages
for lecture information.

Created: Saturday, September 17, 2022

@author: Mary V (mvoorhe), Caitlin Wilson (Caitlin-Wilson-8642), Lexi Ogrinz (AOgrinz-pixel)

"""

import requests
from bs4 import BeautifulSoup

main_page = requests.get("https://www.math.purdue.edu/academic/courses/")
keyword = input("What math class are you looking for (5 digit number)?\n")

src = main_page.content
soup = BeautifulSoup(src, 'lxml')

links = soup.find_all("a")
for link in links:
    if "MA " + keyword in link.text:
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
for prof_classes in prof_tags:
    if prof_name in prof_classes.text:
        print(prof_classes.parent.parent)

day_preference = input("Do you care about what days the class is held on?\n").lower()
if day_preference == "yes":
    days = input("What day(s) do you want (condtions for input)?\n").upper()

day_tags = class_soup.find_all("td")
for available_days in day_tags:
    if days in available_days.text:
        print(available_days.parent)
