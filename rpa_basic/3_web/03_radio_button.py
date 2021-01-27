from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to_frame('iframeResult') # frame 전환

elem = browser.find_element_by_xpath('//*[@id="male"]')

# 선택이 안 되어 있으면 선택하기
if elem.is_selected() == False: # 라디오 버튼이 선택되어 있지 않으면
    print("선택하기")
    elem.click()
else: # 라디오 버튼이 선택되어 있다면
    print("암것도 안 함")

time.sleep(5)

# 선택이 안 되어 있으면 선택하기
if elem.is_selected() == False: # 라디오 버튼이 선택되어 있지 않으면
    print("선택하기")
    elem.click()
else: # 라디오 버튼이 선택되어 있다면
    print("암것도 안 함")

browser.quit()
