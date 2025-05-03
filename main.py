import requests

url = "https://www.pocketyoga.com/poses.json"
resp = requests.get(url)
data = resp.json()
print(data[0].keys())

out_path = "poses.txt"
with open(out_path, "w", encoding="utf-8") as f:

    f.write("Name\tSanskrit\tDescription\n")

    for pose in data:
        name = pose.get("latin", "").strip()
        sanskrit = pose.get("devanagari", "").strip()
        translation = pose.get("simplified", "").strip()
        description= pose.get("description", "").replace("\n", " ").strip()

        f.write(f"{name}\t{sanskrit}\t{description}\n")

print(f"Wrote {len(data)} poses to {out_path}")



'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#open up chrome, head to pocketyoga -> poses, wait until each pose is loaded
driver = webdriver.Chrome()
driver.get("https://www.pocketyoga.com/pose/")
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((
    By.CSS_SELECTOR, "section.posesDisplay ul li a")))

#grab <a> tags under poseDisplay
pose_links = driver.find_elements(By.CSS_SELECTOR, "section.posesDisplay ul li a")

#loop through to grab each link until the pattern doesnt match "/pose/..."
for link in pose_links:
    url = link.get_attribute("href")
    if not url.startswith("https://www.pocketyoga.com/pose/"):
        break

    #grab the names
    # go through each pose link
    # in HTML:
    #   -->  class="poseHeading"
    # then for English Translation -->  <h3> English Name </h3>
    # then for Sanskrit English -->  <a href="#" data-index="0" class="big">
    driver.get(url)
    heading = driver.find_element(By.CLASS_NAME, "poseHeading")
    english_translation = heading.find_element(By.TAG_NAME, "h3").text
    big_links = heading.find_elements(By.CLASS_NAME, "big")

    if big_links:
        sanskrit_in_english = big_links[0].text
    else:
        all_links = heading.find_elements(By.TAG_NAME, "a")
        sanskrit_in_english = all_links[0].text if all_links else ""
    print(f"{english_translation} - {sanskrit_in_english}")

    #pauses to make sure script doesnt try to click the next link while page isnt ready
    time.sleep(0.5)
    driver.back()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "section.posesDisplay ul li a")))

driver.quit()

########## NEED TO SCRAPE DESCRIPTIONS
########## WILL ADD A PART WHERE IT WILL WRITE ALL THE INFO INTO A CSV OR TXT
'''