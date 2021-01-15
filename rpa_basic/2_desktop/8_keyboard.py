import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개 띄운 상태에서 실행해야됨
w.activate()

pyautogui.write("12345")
pyautogui.write("12345", interval=0.25)

pyautogui.write(['t', 'e', 's', 't', 'left', 'left', 'right', 'l', 'a', 'enter'])


### automate the boring stuff with python
# 'a', 'b', 'c', 'A', 'B', 'C', '1', '2', '3', '!', '@', '#', and so on	The keys for single characters
# 'enter' (or 'return' or '\n')	The ENTER key
# 'esc'	The ESC key
# 'shiftleft', 'shiftright'	The left and right SHIFT keys
# 'altleft', 'altright'	The left and right ALT keys
# 'ctrlleft', 'ctrlright'	The left and right CTRL keys
# 'tab' (or '\t')	The TAB key
# 'backspace', 'delete'	The BACKSPACE and DELETE keys
# 'pageup', 'pagedown'	The PAGE UP and PAGE DOWN keys
# 'home', 'end'	The HOME and END keys
# 'up', 'down', 'left', 'right'	The up, down, left, and right arrow keys
# 'f1', 'f2', 'f3', and so on	The F1 to F12 keys
# 'volumemute', 'volumedown', 'volumeup'	The mute, volume down, and volume up keys (some keyboards do not have these keys, but your operating system will still be able to understand these simulated keypresses)
# 'pause'	The PAUSE key
# 'capslock', 'numlock', 'scrolllock'	The CAPS LOCK, NUM LOCK, and SCROLL LOCK keys
# 'insert'	The INS or INSERT key
# 'printscreen'	The PRTSC or PRINT SCREEN key
# 'winleft', 'winright'	The left and right WIN keys (on Windows)
# 'command'	The Command () key (on macOS)
# 'option'	The OPTION key (on macOS)

### 특수문자
# shift 4 -> $
pyautogui.keyDown('shift') # shift 키를 누른 상태에서
pyautogui.press('4') # 숫자 4를 입력하고
pyautogui.keyUp('shift') # shift 키를 뗀다

### 조합키 사용은 아래처럼 간편하게 사용 가능
pyautogui.hotkey('shift', '5')

### 한글 작성은 package 설치 필요 pip install pyperclip
import pyperclip

pyperclip.copy("코딩하자") # 코딩하다 글자를 클립보드에 저장
pyautogui.hotkey('ctrl', 'v') # 클립보드에 있는 내용 붙여넣기

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')

my_write('코딩하자아')


### 자동화 프로그램 종료
# win : ctrl + alt + del
# mac : cmd + shift + option + q
