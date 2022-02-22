from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


iperson = input("Enter person name or contact here: ")
imessage = input("Type Your Message here: ")

PATH = "/home/mahendra/selenium-setup/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://web.whatsapp.com/")
driver.implicitly_wait(30)
# driver.maximize_window()

searchBox =driver.find_element_by_xpath("//div[@title='Search input textbox']").send_keys(iperson)
driver.implicitly_wait(10)

person = driver.find_element_by_xpath("//span[@title="+'"'+iperson+'"'+"]").click()
driver.implicitly_wait(10)


typeBox = driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[1]/span[2]/div[1]/div[2]/div[1]/div[1]/div[2]").send_keys(imessage)

driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[1]/span[2]/div[1]/div[2]/div[1]/div[1]/div[2]").send_keys(Keys.ENTER)


time.sleep(4)
driver.quit()

