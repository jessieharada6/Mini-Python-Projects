# Selenium webdriver
# Selenium web browser
# type or click on browser

# bs4 scrapes html pages, won't be able to scrape if with code of js and angular
# html takes time to load
# selenium is faster and work with code of js and angular

from selenium import webdriver

chrome_driver_path = "/Users/jewang/Desktop/16/Mini-Python-Projects/chromedriver"
# create a chrome browser to drive
# Chrome is an object
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# open a website
# the browser will show "Chrome is being controlled by automated testing software"
driver.get("https://www.python.org/")
# # <span id="priceblock_saleprice" class="a-size-medium a-color-price priceBlockSalePriceString">$24.99</span>
# price = driver.find_element_by_id("priceblock_saleprice")
# # price is a selenium object
# print(price.text)

# <input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="" tabindex="1">
search_bar = driver.find_element_by_name("q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

# <img class="python-logo" src="/static/img/python-logo@2x.png" alt="python™" width="290" height="82">
logo = driver.find_element_by_class_name("python-logo")
print(logo.size)

# <div class="small-widget documentation-widget">
#                         <h2 class="widget-title"><span aria-hidden="true" class="icon-documentation"></span>Docs</h2>
# <p>Documentation for Python's standard library, along with tutorials and guides, are available online.</p>
# <p><a href="https://docs.python.org">docs.python.org</a></p>
#                     </div>
doc_link = driver.find_element_by_css_selector(".documentation-widget a")
# https://docs.python.org
print(doc_link.text)


# <a href="https://github.com/python/pythondotorg/issues">Submit Website Bug</a>
# copy -> copy xpath
bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# close the browser on the single tab
# driver.close()
# close the entire browser
driver.quit()
