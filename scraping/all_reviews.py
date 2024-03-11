import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

c_name = []
c_rating = []
c_review = []
t_posted = []


driver = webdriver.Chrome()
url = "https://www.flipkart.com/shivark-new-designer-set-3-black-dial-watch-1-bracelet-boys-analog-men/product-reviews/itm097ce701fe44a?pid=WATGNH9QQKC7JZEY&lid=LSTWATGNH9QQKC7JZEYKCULEP&marketplace=FLIPKART"
driver.get(url)
driver.maximize_window()
soup = BeautifulSoup(driver.page_source,"lxml")
sleep(3)

parent_div = soup.find_all("div",class_="row _1ExUpQ")


customer_name = soup.find_all("p",class_="_2sc7ZR _2V5EHH _1QgsS5")
customer_rating = soup.find_all("div",class_="_3LWZlK _1BLPMq _3B8WaH")
customer_review = soup.find_all("div",class_="_6K-7Co")
print(soup.select_one("div p:nth-of-type(2)").text)

for div in parent_div:
    time_posted = div.find_all("p")
    t_posted.append(time_posted[1].text)

for name,rating,review in zip(customer_name,customer_rating,customer_review):
    c_name.append(name.text)
    c_rating.append(rating.text)
    c_review.append(review.text)


print(c_name)
print(c_rating)
print(c_review)
print(t_posted)
new_list = t_posted[1::2]

print(new_list)

sleep(4)