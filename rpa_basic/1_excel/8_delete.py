from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.delete_rows(8) # Delete row 8
# ws.delete_rows(8, 3) # Delete 3 rows starting at row 8
# wb.save("sample_delete_rows.xlsx")

# ws.delete_cols(2) # Delete column B
ws.delete_cols(2, 2) # Delete 2 columns starting at column B
wb.save("sample_delete_cols.xlsx")
