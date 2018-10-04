import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
import os

# name is to be same as in contacts
#name = input("Enter name: ")
#message = input("Enter message: ")
#c = int(input("Number of times message is to be sent: "))
name="Nikhil"
message="Hello!"
c=3;
# import chromium driver so to open Whatsapp Web
driver = webdriver.Chrome("/home/kashishsehgal73/Downloads/chromedriver")
driver.get("http://web.whatsapp.com/")
# wait for 7 seconds
time.sleep(7)

# locate contacts search bar
searchBox = driver.find_element_by_xpath('//input[@class="input-search"]')

#input-search
# clear anything which is already present in search bar and enter the name
searchBox.clear()
searchBox.send_keys(name)
searchBox.send_keys(Keys.RETURN)

# find message box by xpath
messageBox = driver.find_element_by_xpath('//div[@class="input"]')

# send message c times
for i in range(c):
    messageBox.send_keys(message)
    messageBox.send_keys(Keys.RETURN)
