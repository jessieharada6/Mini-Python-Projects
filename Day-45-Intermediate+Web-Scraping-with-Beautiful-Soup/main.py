from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()
    # print(contents)

soup = BeautifulSoup(contents, "html.parser")
# title tag + string
print(soup.title)
# title tag
print(soup.title.name)
# string
print(soup.title.string)
# formatted contents
print(soup.prettify())

print("----------------------------------------")
print("anchor tag")
# first anchor tag
print(soup.a)
# all anchor tags
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    # only texts
    print(tag.getText())

for tag in all_anchor_tags:
    # only links
    print(tag.get("href"))

# return first h1 element
print("----------------------------------------")
print("TRY <h1 id='name'>Angela Yu</h1>")
heading = soup.find(name="h1")
print(heading)
# return particular <h1 id=name ... in a list
heading = soup.find_all(name="h1", id="name")
print(heading)

# class is a reserved word, use class_
print("----------------------------------------")
print("TRY <h3 class='heading'>Books and Teaching</h3>")
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.get("class"))
print(section_heading.getText())
print(section_heading.name)

# Similar to <style> in html, where we specify css
# we can select in a similar way
print("----------------------------------------")
print("TRY <p><em>Founder of <strong><a href='https://www.appbrewery.co/'>The App Brewery</a></strong>.</em></p>")
# select - select all
# select_one - select the first one returning list
company_url = soup.select_one(selector="p a")
print(company_url)
print(company_url.getText())
print(company_url.get("href"))

# id using # sign - https://www.w3schools.com/cssref/sel_id.asp
print("----------------------------------------")
print("TRY <h1 id='name'>Angela Yu</h1>")
name = soup.select_one(selector="#name")
print(name)

# class using .heading
print("----------------------------------------")
print("TRY <h3 class='heading'>Books and Teaching</h3>")
# return a list of all tags with class of heading
print(soup.select(".heading"))