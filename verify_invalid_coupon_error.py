'''
Write a selenium script that verifies invalid coupon code will show error in cart page
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Keeps webdriver from closes Chrome immediately
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
# driver = webdriver.Firefox()

# Go to website home page
driver.get('http://frenchy-petes.local/')


# Find a product and go to product page
product_css = 'a.woocommerce-LoopProduct-link.woocommerce-loop-product__link'
product = driver.find_element(By.CSS_SELECTOR, product_css)
product.click()


# Find add to cart button and click it
add_to_cart = 'button[value="319"]'
add_to_cart_btn = driver.find_element(By.CSS_SELECTOR, add_to_cart)
add_to_cart_btn.click()

# Find view cart button and click it
view_cart = 'a.button.wc-forward'
view_cart_btn = driver.find_element(By.CSS_SELECTOR, view_cart)
view_cart_btn.click()


# Find coupon code field, add coupon and click to apply it
find_coupon = 'input[id="coupon_code"]'
apply_coupon = driver.find_element(By.CSS_SELECTOR, find_coupon).send_keys('WHAM!ZAP')
apply_coupon_btn = 'button[value="Apply coupon"]'
driver.find_element(By.CSS_SELECTOR, apply_coupon_btn).click()


# Find error after clicking coupon 
coupon_error = '//*[@id="post-7"]//*[contains(@class, "woocommerce-error")]'
coupon_error_msg =  WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, coupon_error)))
# driver.find_element(By.XPATH, coupon_error)


# Verify that the coupon was invalid
assert coupon_error_msg.is_displayed(), "The coupon error message is not displayed."
