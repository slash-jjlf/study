from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.insert_rows(8) # Insert a new row at row 8
# ws.insert_rows(8, 5) # Insert 5 new rows starting at row 8
# wb.save("sample_insert_rows.xlsx")

ws.insert_cols(2, 3) # Insert 3 new columns starting at column B
wb.save("sample_insert_cols.xlsx")

