import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("650x480") # 가로 * 세로

# 진행단계를 나타내는 상태 바를 만들 수 있다.
# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # 끝이 정해져있지 않은 반복하는 형식
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # 끝까지 가면 정지하는 형식
# progressbar.start(10) # 10ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop() # 작동 중지

# btn = Button(root, text="클릭", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): # 1 ~ 100
        time.sleep(0.01) # 0.01 초 대기

        p_var2.set(i) # progress bar 의 값 설정
        progressbar2.update() # ui 업데이트
        print(p_var2.get())

Button(root, text="시작", command=btncmd2).pack()

root.mainloop()