# 그림판을 켜서 글자를 입력하는 자동화 프로그램 만들기

import pyautogui
import time
import sys
import pyperclip


pyautogui.hotkey('win', 'r')
pyautogui.write('mspaint')
pyautogui.press('enter')

pyautogui.sleep(2)

window = pyautogui.getWindowsWithTitle('제목 없음 - 그림판')[0] # 그림판 1개만 띄워져 있다고 가정
if window.isMaximized == False:
    window.maximize() # 최대화

# 글자 버튼 클릭
btn_text = pyautogui.locateOnScreen("btn_text.png")
if btn_text:
    pyautogui.click(btn_text, duration=0.5)
else:
    print("찾기 실패")
    sys.exit()

# 흰 영역 클릭
# pyautogui.click(200, 200, duration=0.5)
pyautogui.click(btn_text.left - 200, btn_text.top + 200)

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')

my_write('참 잘했어요!')

# 5초 대기
pyautogui.sleep(5)

# 프로그램 종료
window.close()
pyautogui.sleep(0.5)
pyautogui.press('n')
