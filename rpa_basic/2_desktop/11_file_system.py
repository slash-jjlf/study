# 파일 기본
import os

# print(os.getcwd()) # current working directory 현재 작업 공간
# os.chdir(".venv") # .venv로 작업 공간 이동 
# print(os.getcwd())
# os.chdir("..") # 부모 폴더로 이동
# print(os.getcwd())
# os.chdir("../..") # 조부모 폴더로 이동
# print(os.getcwd())
# os.chdir("c:/") # 주어진 절대 경로로 이동
# print(os.getcwd())

# 파일 경로 만들기
# file_path = os.path.join(os.getcwd(), "my_file.txt") # 절대 경로 생성
# print(file_path)

# 파일 경로에서 폴더 정보만 가져오기
# print(os.path.dirname(r"C:\Users\slash\Desktop\study\rpa_basic\2_desktop\my_file.txt")) # 파일이 있는 폴더의 정보만 가져옴

# 파일 정보 가져오기
import time
import datetime

file_path = os.path.join(os.getcwd(), "11_file_system.py")
print(file_path)

#파일의 생성 날짜
ctime = os.path.getctime(file_path)
# 날짜 정보를 strftiem을 통해서 연월일 시분초 형태로 출력
print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# 파일의 수정 날짜
mtime = os.path.getmtime(file_path)
print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# 파일의 접근 날짜
atime = os.path.getatime(file_path)
print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# 파일 크기
size = os.path.getsize(file_path)
print(size) # 바이트 단위로 가져옴
