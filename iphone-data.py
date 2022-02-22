# from webbrowser import Chrome
# from click import Option
# from webdriver_manager.chrome import ChromeDriverManager
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
# next_button = driver.find_element_by_xpath("//text()[.='Next']/ancestor::a[1]")  # for clicking next button

namesList = []
priceList = []

for phone in range(len(phones)):
    namesList.append(phones[phone].text)
    priceList.append(prices[phone].text)
    

dataDict = {}
for data in range(len(namesList)):
    dataDict[namesList[data]] = priceList[data]


pprint(dataDict)
# print('*'*20)
# print(priceList)

time.sleep(4)
driver.quit()





# phone.click()
# price = phone.find_element_by_xpath("/html[1]/body[1]/div[4]/div[2]/div[3]/div[10]/div[14]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/span[1]/span[2]")
# # price.append(price.text)
# print(price.text)
# driver.get("https://www.amazon.in/")



# # driver.close()
