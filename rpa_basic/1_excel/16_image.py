from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb = Workbook()
ws = wb.active

img = Image("img.png") # 이미지 불러오기
ws.add_image(img, "c3") # C3 위치에 이미지 추가
wb.save("sample_image.xlsx")



