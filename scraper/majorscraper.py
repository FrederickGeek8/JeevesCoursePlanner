from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import selenium
import getpass
import time
import json
import subprocess
import os
"""
Scrapes major names.
"""

DIRNAME = os.path.dirname(os.path.abspath(__file__)) + "/"
DELAY = 15 # how many seconds do we wait for the page to load?

def dumpJsonAndChmod(obj, fname):
    with open(fname, "w") as f:
        json.dump(obj, f)
    # subprocess.call(["chown", "skyrunner", DIRNAME + fname])


driver = webdriver.Chrome()
driver.get("http://albert.nyu.edu/course-finder")
driver.select = driver.find_element_by_css_selector  # too wordy

timeout = 60

coursesearchlink = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Course Search")))
coursesearchlink.click()

# driver.switch_to_frame("TargetContent")

# We are now in the albert course search.
checkbox = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#NYU_CLS_WRK_NYU_SPRING")))  # selects the semester
checkbox.click()
time.sleep(DELAY)
"""
    {
        "ART-SHU": {
            "2": {
                "name": "Introduction to Studio Art - Chinese Traditional Methods in Contemporary Art",
                "coursenum": "210",
                ...
            },
            "5": { ... }
        }
        "BIOL-SHU": {
            ...
        }
    }

"""

links = []
# On second thought, don't need to select the school.
# unless i only want nyu shanghai's
select = Select(driver.find_element_by_id('NYU_CLS_WRK2_DESCR254$33$'))
#select by visible text
select.select_by_visible_text('NYU Shanghai')
time.sleep(DELAY)

for tag in driver.find_elements_by_tag_name("a"):
    tagid = tag.get_attribute("id")
    if "LINK" in tagid:
        links.append(tag.text)

with open("possiblemajors.txt", "w") as f:
    for link in links:
        link = link.rstrip().replace('\n', ' ')  # remove trailing newline
        f.write(link + "\n")
# subprocess.call(["chown", "skyrunner", DIRNAME + "possiblemajors.txt"])
print("Done.")
driver.close()