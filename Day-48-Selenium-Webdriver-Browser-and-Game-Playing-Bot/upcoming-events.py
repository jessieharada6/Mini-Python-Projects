from selenium import webdriver

# init selenium
chrome_driver_path = "/Users/jewang/Desktop/16/Mini-Python-Projects/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.python.org/")

# selenium get data
dates = []
events = []

for i in range(1, 6):
    dates_elements = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/time')
    dates.append(dates_elements.text)

for i in range(1, 6):
    events_elements = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a')
    events.append(events_elements.text)

driver.quit()

# build dictionary
events_dictionary = {}
for i in range(len(dates)):
    events_dictionary[i ] = {
        "time": dates[i],
        "name": events[i]
    }

print(events_dictionary)

# or
# get an array of event_time and event_name selenium objects
# event_time = driver.find_elements_by_css_selector(".event-widget time")
# event_name = driver.find_elements_by_css_selector(".event-widget li a")
# events = {}
# for n in range(len(event_times)):
#   events[n] = {
#     "time": event_times[n].text,
#      "event": event_name[n].text
# }



