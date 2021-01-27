from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')

browser.switch_to_frame('iframeResult')

# index를 통해 옵션 선택
# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[3]')

# text()를 통해 선택하는 방법
# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Audi"]')

# contains() text() 부분 일치로 검색
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[contains(text(), "Au")]')

elem.click()

time.sleep(5)
browser.quit()
