import os
from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모쨩")
root.geometry("480x300+300+100") # 가로 * 세로 + 가로시작위치 + 세로시작위치

filename="noname.txt"

def open_file():
    if os.path.isfile(filename): # 파일 있으면 True, 없으면 False
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END) # 텍스트 위젯 본문 삭제
            txt.insert(END, file.read())
            root.title(filename)



def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END-1)) # 모든 내용을 가져와서 저장

menubar = Menu(root) # 메뉴바를 만든다.
# 파일
menu_file = Menu(menubar, tearoff=0)
menu_file.add_command(label="새로만들기(N)", stat="disable")
menu_file.add_command(label="새 창(W)", stat="disable")
menu_file.add_command(label="열기(O)", command=open_file)
menu_file.add_command(label="저장(S)", command=save_file)
menu_file.add_command(label="다른 이름으로 저장(A)", stat="disable")
menu_file.add_separator()
menu_file.add_command(label="페이지 설정(U)", stat="disable")
menu_file.add_command(label="인쇄(P)", stat="disable")
menu_file.add_separator()
menu_file.add_command(label="끝내기(X)", command=root.quit)
menubar.add_cascade(label="파일(F)", menu=menu_file)
# 편집
menu_edit = Menu(menubar, tearoff=0)
menu_edit.add_command(label="실행 취소(U)", stat="disable")
menu_edit.add_separator()
menu_edit.add_command(label="잘라내기(T)", stat="disable")
menu_edit.add_command(label="토막내기(To)", stat="disable")
menu_edit.add_command(label="복사(C)", stat="disable")
menu_edit.add_command(label="붙여넣기(P)", stat="disable")
menu_edit.add_command(label="삭제(L)", stat="disable")
menu_edit.add_separator()
menu_edit.add_command(label="Bing으로 검색(S)", stat="disable")
menu_edit.add_command(label="찾기(F)", stat="disable")
menu_edit.add_command(label="다음 찾기(N)", stat="disable")
menu_edit.add_command(label="이전 찾기(V)", stat="disable")
menu_edit.add_command(label="바꾸기(R)", stat="disable")
menu_edit.add_command(label="이동(G)", stat="disable")
menu_edit.add_separator()
menu_edit.add_command(label="모두 선택(A)", stat="disable")
menu_edit.add_command(label="시간/날짜(D)", stat="disable")
menubar.add_cascade(label="편집(E)", menu=menu_edit)

# 서식
menu_style = Menu(menubar, tearoff=0)
menu_style.add_checkbutton(label="자동 줄 바꿈(W)", stat="disable")
menu_style.add_command(label="글꼴(F)...", stat="disable")
menubar.add_cascade(label="서식(S)", menu=menu_style)

# 보기
menu_view = Menu(menubar, tearoff=0)
menu_view.add_command(label="확대하기/축소하기", stat="disable")
menu_view.add_checkbutton(label="상태표시줄(S)", stat="disable")
menubar.add_cascade(label="보기(V)", menu=menu_view)

# 도움말
menu_help = Menu(menubar, tearoff=0)
menu_help.add_checkbutton(label="도움말 보내기(H)", stat="disable")
menu_help.add_command(label="피드백 보내기(F)", stat="disable")
menu_help.add_separator()
menu_help.add_command(label="메모장 정보(A)", stat="disable")
menubar.add_cascade(label="도움말", menu=menu_help)

# 스크롤 바 (예제에서는 위젯이 없으므로 root에 넣음)
scrollbar=Scrollbar(root)
scrollbar.pack(side="right", fill="y")


# 본문 영역
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt.yview)


root.config(menu=menubar) # 윈도우 창에 메뉴를 등록한다.
root.mainloop()