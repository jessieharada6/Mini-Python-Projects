from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/jewang/Desktop/16/Mini-Python-Projects/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element_by_name("fName")
f_name.send_keys("f_name")
f_name.send_keys(Keys.TAB)
l_name = driver.find_element_by_name("lName")
l_name.send_keys("l_name")
l_name.send_keys(Keys.TAB)
email = driver.find_element_by_name("email")
email.send_keys("email@email.com")
email.send_keys(Keys.TAB)
sign_up = driver.find_element_by_xpath('/html/body/form/button')
sign_up.click()


