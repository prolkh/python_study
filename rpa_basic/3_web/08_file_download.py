import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 파일을 다운로드할 경로 설정
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory':r'D:\python'})

browser = webdriver.Chrome(options=chrome_options)
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')

browser.switch_to_frame('iframeResult')

# 다운로드 링크 클릭
elem = browser.find_element_by_xpath('/html/body/p[2]/a')
elem.click()

time.sleep(5)
browser.quit()
