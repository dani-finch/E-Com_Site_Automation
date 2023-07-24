'''
Write a Selenium script for your website that registers a new user, 
in order to verify that registration works
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string

# Keeps webdriver from closes Chrome immediately
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)

# Go to website account page
driver.get('http://frenchy-petes.local/my-account/')

# Find the register email address field
reg_email = driver.find_element(By.ID, 'reg_email')

# Generate random email
ran_string = ''.join(random.choice(string.ascii_lowercase) for i in range(9))
ran_email = f'{ran_string}@email.com'

# Input email address into the field
reg_email.send_keys(ran_email)

# Find the register password field
reg_pass = driver.find_element(By.ID, 'reg_password')

# Generate random password
ran_pass = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))

# Input password into the field
reg_pass.send_keys(ran_pass)

# Click the Register button
button_css = '#customer_login > div.u-column2.col-2 > form > p:nth-child(4) > button'
reg_button = driver.find_element(By.CSS_SELECTOR, button_css)
reg_button.click()

# Find the 'Dashboard' link on the My Account page
dash_xpath = '//*[@id="post-9"]/div/div/nav/ul/li[1]'
dash = driver.find_element(By.XPATH, dash_xpath)

# Verify that the new user was registered
if dash.is_displayed():
    print('New user was registered successfully!')
else:
    print('Failed to register new user.')
