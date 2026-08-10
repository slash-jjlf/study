# 파일 기본
import os  # noqa: I001

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
# import time
# import datetime

# file_path = os.path.join(os.getcwd(), "11_file_system.py")
# print(file_path)

# #파일의 생성 날짜
# ctime = os.path.getctime(file_path)
# # 날짜 정보를 strftiem을 통해서 연월일 시분초 형태로 출력
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 수정 날짜
# mtime = os.path.getmtime(file_path)
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 접근 날짜
# atime = os.path.getatime(file_path)
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# # 파일 크기
# size = os.path.getsize(file_path)
# print(size) # 바이트 단위로 가져옴

# 파일 목록 가져오기
# print(os.listdir()) # 모든 폴더, 파일 목록 가져오기
# print(os.listdir(".venv"))

# 파일 목록 가져오기 (하위 폴더 모두 포함)
# result = os.walk(".")
# # print(result)

# for root, dirs, files in result:
#     print(root, dirs, files)

# 만약 폴더 내에서 특정 파일들을 찾으려면?
# name = "11_file_system.py"
# result = []
# for root, dirs, files in os.walk("."):
#     if name in files:
#         result.append(os.path.join(root, name))

# print(result)

# 만약 폴더 내에 특정 패턴을 가진 파일들을 찾으려면?
# *.txt, *.py, *.png 등등

# import fnmatch
# pattern = "*.png"
# result = []

# for root, dirs, files in os.walk("."):
#     for name in files:
#         if fnmatch.fnmatch(name, pattern):
#             result.append(os.path.join(root, name))
# print(result)


# 주어진 경로가 파일인지? 폴더인지?
# print(os.path.isdir(".venv")) # .venv는 폴더인가?
# print(os.path.isfile(".venv")) #.venv는 파일인가?

# print(os.path.isdir("run_btn.png"))
# print(os.path.isfile("run_btn.png"))

# # 만약 지정된 경로에 해당하는 파일이나 폴더가 없다면?
# print(os.path.isfile("run_btnnn.png"))

# 주어진 경로가 존재하는가?
# if os.path.exists(".venv"):
#     print("파일 또는 폴더가 존재합니다.")
# else:
#     print("존재하지 않습니다.")


# 파일 만들기
# open("new_file.txt", "a").close() # 빈 파일 생성

# # 파일명 변경하기
# os.rename("new_file.txt", "new_file_rename.txt")

# 파일삭제
# os.remove("new_file_rename.txt")


# 폴더 만들기
# os.mkdir("new_folder") # 현재 경로 기준으로 폴더 생성(절대 경로 기준으로 폴더도 생성 가능)
# 폴더가 이미 존재할때는 에러남

# 하위 폴더를 가지는 폴더 생성
# os.makedirs("new_folders/a/b/c") 

# 폴더명 변경하기 
# os.rename("new_folder", "new_folder_rename")

# 폴더 지우기
# os.rmdir("new_folders") # 실패함(폴더안에 내용이 있기 때문)
import shutil # shell utilities
# shutil.rmtree("new_folders") # 폴더 안이 비어 있지 않아도 완전 삭제 가능(주의!!)

# 파일 복사하기
# 어떤 파일을 폴더 안으로 복사하기
# shutil.copy("run_btn.png", "test_folder" )
# 어떤 파일을 폴더 안에 새로운 이름으로 복사하기
# shutil.copy("run_btn.png", "test_folder/run_btn_renamed.png")

# 폴더 복사
# shutil.copytree("test_folder", "test_folder2") # 원본 폴더 경로, 대상 폴더 경로

# 폴더 이동
# shutil.move("test_folder", "test_folder2")
# shutil.move("test_folder2/test_folder", ".")
shutil.move("test_folder2", "test_folder3") # 폴더명이 변경되는 효과