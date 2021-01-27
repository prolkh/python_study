from selenium import webdriver
import time
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox')

browser.switch_to_frame('iframeResult')

#elem = browser.find_element_by_xpath('//*[@id="vehicle1"]')
elem = browser.find_element(By.XPATH, '//*[@id="vehicle1"]')

if elem.is_selected() == False:
    print("선택")
    elem.click()
else:
    print('암것도 안 함')

time.sleep(5)



