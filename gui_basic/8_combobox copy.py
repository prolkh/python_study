import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("650x480") # 가로 * 세로

# combobox 사용을 위해서는 tkinter.ttk 를 import 해줘야한다.
# combobox는 드롭다운 목록이다. html의 select와 매우 유사하다.
values = [str(i) + "일" for i in range(1, 32)] # 1 ~ 31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정

# 값 수정이 불가능한 콤보 박스 만들기
readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0) # 0번째 인덱스 값 선택
readonly_combobox.pack()



def btncmd():
    print(combobox.get()) # 선택된 값 표시

btn = Button(root, text="클릭", command=btncmd)
btn.pack()
root.mainloop()