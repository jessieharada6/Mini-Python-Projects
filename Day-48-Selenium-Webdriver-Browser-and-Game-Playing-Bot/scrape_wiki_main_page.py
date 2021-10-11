from selenium import webdriver

# <a href="/wiki/Special:Statistics" title="Special:Statistics">6,391,238</a>
chrome_driver_path = "/Users/jewang/Desktop/16/Mini-Python-Projects/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

number_of_articles_element = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
number_of_articles = number_of_articles_element.text
print(number_of_articles)

# it is id, so use #, if it's class, use .
# element = driver.find_element_by_css_selector("#articlecount a").text


driver.quit()