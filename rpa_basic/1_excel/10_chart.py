from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

from openpyxl.chart import BarChart, Reference, LineChart

# Bar chart
# B2:B11 범위의 데이터를 차트로 만들기 위해 Reference 객체 생성
# bar_value = Reference(ws, min_row=2, max_row=11, min_col=2, max_col=3)
# bar_chart = BarChart() # 챠트종류 설정
# bar_chart.add_data(bar_value) # 챠트에 데이터 추가
# ws.add_chart(bar_chart, "E1") # 챠트를 시트에 추가
# wb.save("sample_chart.xlsx")

# Line chart(제목 포함)
line_value = Reference(ws, min_row=1, max_row=11, min_col=2, max_col=3)
line_chart = LineChart() # 챠트종류 설정
line_chart.add_data(line_value, titles_from_data=True) # 챠트에 데이터 추가
line_chart.title = "성적표" # 챠트 제목
line_chart.style = 10 # 챠트 스타일
line_chart.y_axis.title = "점수" # y축 제목
line_chart.x_axis.title = "번호" # x축 제목
ws.add_chart(line_chart, "E1") # 챠트를 시트에 추가
wb.save("line_chart.xlsx")
