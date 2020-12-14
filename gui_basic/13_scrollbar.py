from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("650x480") # 가로 * 세로

# 스크롤바 위젯은 프레임 안에 넣는 것이 관리가 편함
# 스크롤바 생성 전에 프레임을 먼저 생성
frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y") # fill="y" 스크롤바의 크기를 프레임 크기에 맞춤설정

# yscrollcommand=scrollbar.set 이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)

for i in range(1, 32): # 1 ~ 31 일
    listbox.insert(END, str(i) +  "일") # 1일, 2일, ...
listbox.pack(side="left")

scrollbar.config(command=listbox.yview) # 스크롤바의 위치를 리스트박스의 위치에 매핑
root.mainloop()