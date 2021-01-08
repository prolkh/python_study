import pyautogui

# moveTo() : 상대좌표로 마우스 이동
pyautogui.moveTo(200, 100) # 지정한 위치(가로 x, 세로 y)로 마우스를 이동
pyautogui.moveTo(100, 200, duration = 0.5) # 0.5초 동안 100, 200 위치로 이동


pyautogui.moveTo(100, 100, duration = 0.5)
pyautogui.moveTo(200, 200, duration = 0.5)
pyautogui.moveTo(300, 300, duration = 0.5)

# move() : 상대 좌표로 이동(현재 커서가 있는 위치로부터)
pyautogui.moveTo(100, 100, duration=0.25)
pyautogui.move(100, 100, duration=0.25)
pyautogui.move(100, 100, duration=0.25)

# position() : 마우스 포인터의 위치
print(pyautogui.position()) # Point(x, y)

# 마우스 x위치, y위치 출력
p = pyautogui.position()
print(p[0], p[1]) # x, y
print(p.x, p.y) # x, y