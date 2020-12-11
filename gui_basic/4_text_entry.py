from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("650x480") # 가로 * 세로

root.resizable(False, False) # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

txt = Text(root, width=30, height=5) # textarea 생성
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30) # Entry는 한줄로만 입력 가능
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd():
    print(txt.get("1.0", END))    # 1번라인, 0번째 column부터 끝까지
    print(e.get())

    txt.delete("1.0", END) # 내용 삭제
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()