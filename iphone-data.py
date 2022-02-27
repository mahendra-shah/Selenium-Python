from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pprint import pprint

PATH = "/home/mahendra/selenium-setup/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://amazon.in/")
driver.implicitly_wait(10)

searchBox =driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys('Apple Iphone')
driver.find_element_by_xpath("//input[@name='field-keywords']").send_keys(Keys.ENTER)
driver.find_element_by_xpath("//span[text()='Apple']").click()

phones = driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
prices = driver.find_elements_by_xpath("//span[@class='a-price-whole']")

namesList = []
priceList = []

for phone in range(len(phones)):
    namesList.append(phones[phone].text)
    priceList.append(prices[phone].text)

dataDict = {}
for data in range(len(namesList)):
    dataDict[namesList[data]] = priceList[data]

time.sleep(4)
driver.quit()