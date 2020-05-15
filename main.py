from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# Step 1) Open Firefox
browser = webdriver.Firefox()
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('path/to/installed firefox binary')
browser = webdriver.Firefox(firefox_binary=binary)

# Step 2) Navigate to Facebook
browser.get("https://www.facebook.com")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit   = browser.find_element_by_id("loginbutton")
username.send_keys("mohankrushnabehera@gmail.com")
password.send_keys("password")
# Step 4) Click Login
submit.click()
wait = WebDriverWait( browser, 5 )
page_title = browser.title
assert page_title == "Facebook"