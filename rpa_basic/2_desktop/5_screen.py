import pyautogui
# 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장

# pyautogui.mouseInfo()

pixel = pyautogui.pixel(20, 15)
print(pixel) # 좌표의 rgb 값 출력 (29, 29, 29)

# 좌표의 픽셀값 비교
print(pyautogui.pixelMatchesColor(20, 15, (29, 29, 29))) # True
print(pyautogui.pixelMatchesColor(20, 15, pixel)) # True
