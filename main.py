from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.pocketyoga.com/pose/")