# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""
Uses package BeautifulSoup4 to webscrape Purdue math class pages
for lecture information.
Created: Saturday, September 17, 2022
@author: Mary V(mvoorhe), Caitlin Wilson (Caitlin-Wilson-8642), Lexi Ogrinz (AOgrinz-pixel)
"""
import pandas
import requests
from bs4 import BeautifulSoup
import pandas as pd

main_page = requests.get("https://www.math.purdue.edu/academic/courses/")

keyword = input("What math class are you looking for (5 digit number)?\n")

src = main_page.content
soup = BeautifulSoup(src, 'lxml')  # parses the html page, so it's in a readable format

links = soup.find_all("a")  # 'a' is referring to the tag for html. Within the 'a' tag links can be found
for link in links:
    if "MA " + keyword in link.text:  # Looks for full course name within the 'a' tag
        class_url = link.attrs['href']
        # print(class_url) - Tests that the url is found
linkToCourse = "https://www.math.purdue.edu/academic/courses/" + class_url
class_page = requests.get(linkToCourse)
print(class_page)  # prints the class page to verify the url is valid

teacher_preference = input("Do you have a preference on who teaches the class?\n")
teacher_preference.lower()
if teacher_preference == "yes":
    prof_name = input("What is the teacher's last name?\n")
    prof_name.lower()


day_preference = input("Do you care about what days the class is held on?\n")
day_preference.lower()
if day_preference == "yes":
    day = input("What day(s) do you want (separate with commas)?\n")
    day.lower()

tables = pd.read_html(linkToCourse)  # Returns table
math_chart = tables[0]  # Select table of interest
print(math_chart)

df = pandas.DataFrame(math_chart)
df = df.reset_index()
for row in df.iterrows():
    if prof_name != 'undefined' and prof_name in row['Instructor']:




#  src = class_page.content
#  class_soup = BeautifulSoup(src, 'lxml')
#  print(class_soup)
