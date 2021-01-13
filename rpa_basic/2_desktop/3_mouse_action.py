import pyautogui

pyautogui.sleep(3) # 3초 대기
# print(pyautogui.position()) # 현재 마우스 포인터 위치 출력
# pyautogui.click(20, 15, duration=1) # 1초 동안 (20, 15) 좌표로 이동 후 마우스 클릭

pyautogui.click() # pyautogui.mouseDown() pyautogui.mouseUp()

# pyautogui.doubleClick() # 더블 클릭
# pyautogui.click(clicks=10) # 10번 클릭

# pyautogui.rightClick() # 오른쪽 클릭
# pyautogui.middleClick() # 마우스 휠 클릭

pyautogui.moveTo(100, 15)
# pyautogui.drag(100, 0) # 현재 위치 기준으로 x 100만큼 y 0 만큼 드래그
pyautogui.drag(100, 0, duration=0.25) # 너무 빠른 동작으로 drag 수행이 안될때 duration 설정

pyautogui.scroll(300) # 위 방향으로 300 스크롤
pyautogui.scroll(-300) # 아래 방향으로 300 스크롤