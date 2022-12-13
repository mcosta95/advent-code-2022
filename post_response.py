from selenium import webdriver
import time

driver = webdriver.Chrome("C:/Program Files/Chrome Driver/chromedriver.exe")  # Path to where I installed the web driver

time.sleep(5) # Let the user actually see something!

driver.get('https://adventofcode.com/2021/day/1')

search_box = driver.find_element("name", "answer")

search_box.send_keys('123')

#search_box.submit()