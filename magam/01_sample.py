from random import randint
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
# ws.title = "BullSheet"

# 반복문을 이용해서 랜덤 숫자 채우기
for x in range(1, 21): # 10개 row
    for y in range(1, 3): # 2개 column
        ws.cell(row=x, column=y, value=randint(0, 5)) # 0~100 사이의 랜덤숫자
        
wb.save("magamsample.xlsx")

