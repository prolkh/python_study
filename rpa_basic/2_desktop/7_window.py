import pyautogui

fw = pyautogui.getActiveWindow() # 현재 활성화된 창
print(fw.title) # 창의 제목 정보 > 7_window.py - python - Visual Studio Code
print(fw.size) # 창의 크기 정보 (width, height)
print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표정보
pyautogui.click(fw.left + 50, fw.top + 20)


# print("##### 모든 윈도우 정보 출력 #####")
# for w in pyautogui.getAllWindows():
#     print(w) # 모든 윈도우 가져오기

w = pyautogui.getWindowsWithTitle("Steam")[0]
print(w)
if w.isActive == False: # 현재 활성화가 되지 않았다면
    w.activate() # 활성화 (맨 앞으로 가져오기)

if w.isMaximized == False: # 현재 최대화가 되지 않았다면
    w.maximize()

if w.isMinimized == False: # 현재 최소화가 되지 않았다면
    w.minimize()

pyautogui.sleep(1)

w.restore() # 화면 원복

w.close() # 윈도우 닫기
