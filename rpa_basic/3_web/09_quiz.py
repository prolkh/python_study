import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/') # w3schools 주소 접속
browser.maximize_window() # 창 크기 최대화

elem = browser.find_element_by_xpath('//*[@id="main"]/div[1]/div[1]/a[1]')
elem.click() # LEARN HTML 클릭

elem = browser.find_element_by_xpath('//*[@id="topnav"]/div/div[1]/a[10]')
elem.click() # HOW TO 클릭

elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact")]')
elem.click() # Contact Form click


first_name = '동'
last_name = '마해'
country = 'Canada'
subject = '퀴즈 제출'


elem = browser.find_element_by_xpath('//*[@id="fname"]')
elem.send_keys(first_name) # 성 입력

elem = browser.find_element_by_xpath('//*[@id="lname"]')
elem.send_keys(last_name) # 이름 입력

elem = browser.find_element_by_xpath('//*[@id="country"]/option[text()="{}"]'.format(country))
elem.click() # 국가 선택

elem = browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea')
elem.send_keys(subject)  # 내용 입력

time.sleep(5)
elem = browser.find_element_by_xpath('//*[@id="main"]/div[3]/a')
elem.click() # submit 클릭

time.sleep(5)
browser.quit() # 브라우저 종료



