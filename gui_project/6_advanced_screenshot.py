import time
import keyboard # pip install keyboard
from PIL import ImageGrab # pip install Pillow

def screenshot():
    # 2020년 12월 19일 오전 2시 36분 -> _20200601_023630
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time)) # ex) image_20200601_023630.png

keyboard.add_hotkey("F9", screenshot) # 사용자가 F9 키를 누르면 스크린 샷 저장
# keyboard.add_hotkey("a", screenshot) # a
# keyboard.add_hotkey("ctrl+shift+s", screenshot) # ctrl + shift + s

keyboard.wait("esc") # 사용자가 esc 를 누를 때까지 프로그램 실행상태