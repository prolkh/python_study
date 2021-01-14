import pyautogui

### 파일 버튼 이미지로 찾아서 클릭하기
# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu) # 없으면 None을 출력함
# pyautogui.click(file_menu)

### 휴지통 버튼 이미지로 찾아서 클릭하기
# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

### https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox 에서 체크박스 이미지 스크린샷후저장
# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i, duration=0.25)

# checkbox = pyautogui.locateOnScreen("checkbox.png")
# pyautogui.click(checkbox)



### 속도 개선
### 1. GrayScale > 흑백으로 변환후 비교
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.click(trash_icon)

### 2. 범위 지정
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1500, 750, 400, 100)) # region=(x, y, width, height)
# pyautogui.click(trash_icon)

### 3. 정확도 조정 pip install opencv-python
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", confidence=0.7) # 기본값은0.999
# pyautogui.click(trash_icon)

### 자동화 대상이 바로 보여지지 않는 경우
### 1. 계속 기다리기
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")
# pyautogui.click(file_menu_notepad)

### 2. 일정 시간 동안 기다리기(TimeOut)
import time
import sys

# timeout = 10 # 10초 대기
# start = time.time() # 시작 시간 설정
# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time()
#     if end - start > timeout: # 지정한 시간 10초를 초과하면
#         print("시간 종료")
#         sys.exit()

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target


def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program")
    sys.exit()

my_click("file_menu_notepad.png", 5)





pyautogui.click(file_menu_notepad)