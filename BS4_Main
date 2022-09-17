"""
Uses package BeautifulSoup4 to webscrape airline websites
for flight prices.

Created: Saturday September 17, 2022

@author: Mary V(mvoorhe), Caitlin Wilson (Caitlin-Wilson-8642), Lexi Ogrinz (AOgrinz-pixel)

"""

import requests
from bs4 import BeautifulSoup

# object that is appended to the BoilerLink website to narrow the search
keyword = input("What club or hobby are you interested in?\n")

# object for website after keyword filters all clubs
filtered_page = requests.get("https://boilerlink.purdue.edu/organizations?query=" + keyword)

# full html content of filtered_page
src = filtered_page.content
# object that stores new BS object
soup = BeautifulSoup(src, 'lxml')




