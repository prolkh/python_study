from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("650x480") # 가로 * 세로

# html의 select 와 유사한 widget
listbox = Listbox(root, selectmode="extended", height=0) # 다중 선택 가능
# listbox = Listbox(root, selectmode="single", height=0) # 하나만 선택 가능
listbox.insert(0, "apple")
listbox.insert(1, "strawberry")
listbox.insert(2, "banana")
listbox.insert(END, "watermelon") # 제일 마지막 항목에 추가
listbox.insert(END, "grape")
listbox.pack()


def btncmd():
    # listbox.delete(0) # 제일 처음 값 삭제
    listbox.delete(END) # 제일 마지막 값 삭제

    # 리스트 박스 요소 개수 확인
    print("there are ", listbox.size(), 'element(s) in the box')

    # 리스트 박스 요소 항목 확인
    print("element 1 ~ 3", listbox.get(0, 2))

    # 리스트 박스 선택된 항목 확인 (위치로 반환 0, 1, 2...)
    print("selected element", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()
root.mainloop()