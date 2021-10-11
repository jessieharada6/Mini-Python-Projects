from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/jewang/Desktop/16/Mini-Python-Projects/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# <input class="vector-search-box-input" type="search" name="search" placeholder="Search Wikipedia" autocapitalize="sentences" title="Search Wikipedia [ctrl-option-f]" accesskey="f" id="searchInput" autocomplete="off">
search = driver.find_element_by_name("search")
# use keyboard to enter texts
search.send_keys("Python")
# use enter key
search.send_keys(Keys.ENTER)