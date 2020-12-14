import tkinter.messagebox as messagebox
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("650x480") # 가로 * 세로

# 메시지 박스(alert과 같은 개념)
# 기차 예매 시스템이라고 가정
def info():
    messagebox.showinfo("알림", "정상적으로 예매 완료되었습니다.") # messagebox.showinfo(알림타이틀, 알림내용)

def warn():
    messagebox.showinfo("경고", "해당 좌석은 매진되었습니다.")

def error():
    messagebox.showerror("에러", "결제 오류가 발생했습니다.")

def okcancel():
    messagebox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")

def retrycancel():
    messagebox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")

def yesno():
    messagebox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")

def yesnocancel():
    response = messagebox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다. \n 저장하고 프로그램을 종료하시겠습니까?")
    # 네 : 저장 후 종료
    # 아니오 : 저장 하지 않고 종료
    # 취소 : 프로그램 종료 취소 (현재 화면에서 계속 작업)
    print("응답:", response) # True, False, None -> 예 1, 아니오 0, 그 외
    if response == 1: # 네, OK
        print("예")
    elif response == 0: # 아니오
        print("아니요")
    else:
        print("취소")
    

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()

root.mainloop()