import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://shopping.naver.com/')

# 무선 마우스 입력
elem = browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]')
elem.send_keys('무선마우스')
elem.send_keys(Keys.ENTER)

# 스크롤
# 지정한 위치로 스크롤 내리기
# browser.execute_script('window.scrollTo(0, 1080)')

# 화면 가장 아래로 스크롤 내리기
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

time.sleep(5)
browser.quit()
