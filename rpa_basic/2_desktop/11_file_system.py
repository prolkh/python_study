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
