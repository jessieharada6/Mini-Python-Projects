from selenium import webdriver

chrome_driver_path = "/Users/jewang/Desktop/16/Mini-Python-Projects/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count_element = driver.find_element_by_css_selector("#articlecount a")
# article_count_element.click()

all_portals = driver.find_element_by_link_text("All portals")
all_portals.click()