from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://demoqa.com/")
sleep(2)
elem = driver.get("https://demoqa.com/elements")
sleep(2)
lista = ['firstName','lastName']
web_tables = driver.find_element(By.ID,'item-3')
web_tables.click()
driver.execute_script("window.scrollTo(0,400)")
sleep(4)
add_record = driver.find_element(By.ID,'addNewRecordButton')
add_record.click()
sleep(3)
for i in lista:
    fname = driver.find_element(By.ID,i)
    fname.send_keys('Rohit')
email = driver.find_element(By.ID,'userEmail')
email.send_keys('test1@gmail.com')
age = driver.find_element(By.ID,'age')
age.send_keys(33)
salary = driver.find_element(By.ID,'salary')
salary.send_keys(22000)
department = driver.find_element(By.ID,'department')
department.send_keys('IT')
submit = driver.find_element(By.ID,'submit')
submit.click()
sleep(5)
search = driver.find_element(By.ID,'searchBox')
search.send_keys('hit')
search.send_keys(Keys.RETURN)
sleep(5)

x = "hell"
y = "o"
print("hell"+y)