from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

# frame 전환
browser.switch_to.frame('iframeResult') # frame 전환

elem = browser.find_element_by_xpath('//*[@id="male"]') # 성공
elem.click()

# frame 빠져나오기
browser.switch_to.default_content()

elem = browser.find_element_by_xpath('//*[@id="male"]') # 에러
elem.click()

time.sleep(5)
browser.quit()