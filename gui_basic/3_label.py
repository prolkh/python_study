from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("650x480") # 가로 * 세로

label1 = Label(root, text="안녕하세요") # div 와 같은 방식으로 사용
label1.pack()

photo = PhotoImage(file="D:\\python\\python_study\\gui_basic\\img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")

    global photo2   # 전역변수로 설정하여 garbage collector가 삭제 안 하도록 함
    photo2 = PhotoImage(file="D:\\python\\python_study\\gui_basic\\img2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()


root.mainloop()