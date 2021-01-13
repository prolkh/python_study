import pyautogui
# pyautogui.mouseInfo() # 마우스 커서 정보를 알려주는 유용한 툴이다.

pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용
# pyautogui.FAILSAFE = False # 화면 네 귀퉁이에 마우스를 놓으면 작동하는 안전장치 해제(비추옵션)

for i in range(10):
    pyautogui.move(100, 100)
    # pyautogui.sleep(1)