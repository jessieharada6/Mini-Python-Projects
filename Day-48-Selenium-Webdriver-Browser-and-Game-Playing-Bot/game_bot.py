from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# https://gist.github.com/angelabauer/affb3ce61bc79ada90dea26052c27c2b
chrome_driver_path = "/Users/jewang/Desktop/16/Mini-Python-Projects/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# time
five_sec = time.time() + 5
five_min = time.time() + 5 * 60

# cookie info
cookie = driver.find_element_by_id("cookie")
current_cookie_count = driver.find_element_by_id("money")
cookie_per_sec = driver.find_element_by_id("cps")

# store is id
items = driver.find_elements_by_css_selector("#store b")
costs = []
purchases = []
for item in items:
    c = item.text.split("-")
    print(c)
    if len(c) == 2:
        cost = int(c[1].strip().replace(",", ""))
        costs.append(cost)
        purchase = c[0].strip()
        purchases.append(purchase)

while True:
    cookie.click()
    # check if I can afford any tools
    if time.time() > five_sec:
        max_cost = 0
        max_index = 0
        # the most expensive tool that i can afford
        for cost in costs:
            cookie_count  =int(current_cookie_count.text.replace(",",""))
            if cookie_count > cost:
                max_cost = max(max_cost, cookie_count)
        for i in range(len(costs)):
            if max_cost >= costs[i]:
                max_index = i
        # <div id="buyGrandma" onclick="Buy('Grandma');" style="background-image:url(grandmaicon.png);" class=""><b>Grandma - <moni></moni> 100</b>A nice grandma to bake more cookies.</div>
        driver.find_element_by_id(f"buy{purchases[max_index]}").click()
        five_sec = time.time() + 5

    if time.time() > five_min:
        print(cookie_per_sec.text)
        break