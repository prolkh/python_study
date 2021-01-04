from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.delete_rows(3) # 3번째 행에 있는 2번 학생 데이터 삭제
ws.delete_rows(3, 3) # 3번째 행부터 3개의 행 삭제

wb.save("sample_delete_row.xlsx")

# ws.delete_cols(2) # 2번째 열 (B) 삭제
ws.delete_cols(2, 2) # 2번째 열부터 2개의 열 삭제

wb.save("sample_delete_cols.xlsx")