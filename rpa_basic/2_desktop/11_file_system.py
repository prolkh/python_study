# 파일 기본
import os
# print(os.getcwd()) # current working directory 현재 작업 공간
# os.chdir("python_study") # rpa_basic 으로 작업공간 이동
# print(os.getcwd())
# os.chdir("..") # 부모 폴더로 이동
# print(os.getcwd())
# os.chdir("../..") # 조부모 폴더로 이동
# print(os.getcwd())
# os.chdir("c:/") # 주어진 절대 경로로 이동
# print(os.getcwd())


# 파일 경로 만들기
join = os.path.join(os.getcwd(), "my_file.txt") # 절대 경로 생성
print(join)

# 파일 경로에서 폴더 정보 가져오기
dirname = os.path.dirname(r"D:\python\my_file.txt")
print(dirname)

# 파일의 생성날짜
import time
import datetime

getctime = os.path.getctime("test.py")
print(getctime)
# 날짜 정보를 strftime을 통해서 연월일 시분초 형태로 출력
print(datetime.datetime.fromtimestamp(getctime).strftime("%Y-%m-%d %H:%M:%S"))

# 파일의 수정 날짜
getmtime = os.path.getmtime("test.py")
print(datetime.datetime.fromtimestamp(getmtime).strftime("%Y-%m-%d %H:%M:%S"))

# 파일의 마지막 접근 날짜
getatime = os.path.getmtime("test.py")
print(datetime.datetime.fromtimestamp(getatime).strftime("%Y-%m-%d %H:%M:%S"))

# 파일 크기
file_path = r"D:\python\test.py"
getsize = os.path.getsize(file_path)
print(getsize) # 바이트 단위로 파일 크기 가져오기

# 파일 목록 가져오기
listdir = os.listdir() # 작업 공간내 모든 폴더, 파일 목록 가져오기
print(listdir)
print(os.listdir("python_study")) # 작업 경로 밑의 폴더

# 하위 폴더 전부 목록 가져오기
walk = os.walk("python_study/rpa_basic") # 하위에 포함된 모든 파일 출력
for root, dirs, files in walk:
    print(root, dirs, files)

# 파일 검색
name = "11_file_system.py"
result = []
for root, dirs, files, in os.walk("."):
    if name in files:
        result.append(os.path.join(root, name))
print(result)

# 패턴을 이용한 검색
# *.xlsx
import fnmatch
pattern = "*.txt" # .py로 끝나는 모든 파일
result = []
for root, dirs, files, in os.walk(os.getcwd()):
    for name in files:
        if fnmatch.fnmatch(name, pattern): # 이름과 패턴이 일치하면
            result.append(os.path.join(root, name))
print(result)


# 주어진 경로가 폴더인지 파일인지
isdir = os.path.isdir("python_study")
print(isdir) # 폴더면 True

isfile = os.path.isfile("sample.xlsx")
print(isfile) # 파일이면 True

print(os.path.isfile("babo.png")) # 없으면 False

# 주어진 경로가 존재하는지
exists = os.path.exists("sample.xlsx")
print(exists) # 존재하면 True

# 파일 만들기
# open("new_file.txt", "a").close() # 빈 파일 생성

# 파일명 변경하기
# os.rename("new_file.txt", "new_file_rename.txt") # new_file.txt -> new_file_rename.txt

# 파일 삭제하기
# os.remove("new_file_rename.txt")

# 폴더 만들기
# os.mkdir("new_folder") # 현재 경로 기준으로 폴더 생성
# os.mkdir("d:/python_study/coding") # 절대 경로 기준으로 폴더 생성

# os.mkdir("new_file/a/b/c") # 실패 : 하위 폴더를 가지는 폴더 생성 시도
# os.mkdirs("new_filse/a/b/c") # 성공: 하위 폴더를 가지는 폴더 생성

# 폴더명 변경하기
# os.rename("new_folder", "new_folder_rename")

# 폴더 지우기
# os.rmdir("new_folders") # 폴더 안이 비었을 때만 삭제 가능

import shutil # shell utilities
# shutil.rmtree("new_folders") # 폴더 안이 비어 있지 않아도 완전 삭제 가능
# 모든 파일이 삭제될 수 있으므로 주의 !!

# 파일 복사하기
# 어떤 파일을 폴더 안으로 복사하기
# shutil.copy("run_btn.png", "test_folder") # 원본 파일 경로, 대상 폴더 경로

# 파일을 폴더 안에 새로은 이름으로 복사하기
# shutil.copy("run_btn.png", "test_folder/copy.png") # 원본 파일 경로, 대상 폴더 경로(변경된 파일명까지)
# shutil.copyfile("run_btn.png", "test_folder/copyfile.png") # 원본 파일 경로, 대상 폴더 경로(변경된 파일명까지)

# shutil.copy2("run_btn.png", "test_folder/copy2.png") # 원본 파일 경로, 대상 폴더 경고(파일 명까지)

# copy, copyfile : 메타정보 복사x
# copy2 : 메타정보 복사x

# 폴더 복사
# shutil.copytree("folder", "copytree") # 원본 폴더 경로, 대상 폴더 경로

# 폴더 이동(이동할 폴더가 없으면 폴더명이 변경됨)
# shutil.move("folder", "move")
