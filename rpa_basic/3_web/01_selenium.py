from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe")

# 네이버 이동
browser.get("http://naver.com")

# 요소 찾기(링크 텍스트)
elem = browser.find_element_by_link_text("카페") 

# 속성 가져오기
elem.get_attribute("href")
elem.get_attribute("class")

# 클릭
elem.click()

# 뒤로가기
browser.back()

# 앞으로가기
# browser.forward()
 

# 요소 찾기(아이디)
elem = browser.find_element_by_id("query")

# 요소에 글자 입력
elem.send_keys("코딩") 


# 키보드 누르기(엔터)
from selenium.webdriver.common.keys import Keys 
elem.send_keys(Keys.ENTER)

# 요소 찾기(태그이름)
elem = browser.find_element_by_tag_name("a")
elem.get_attribute("href")

# 요소s 찾기(태그이름)
elem = browser.find_elements_by_tag_name("a")
for e in elem:
    e.get_attribute("href")

# 다음으로 이동
browser.get("http://daum.net")

# 요소 찾기(이름)
elem = browser.find_element_by_name("q")
elem.send_keys("코딩")
elem.send_keys("코딩")

# 요소에 입력한 내용 지우기
elem.clear()

elem.send_keys("코딩")

# 요소 찾기(xpath) 후 클릭
elem = browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]')
elem.click()

# 참고 : https://selenium-python.readthedocs.io/locating-elements.html
