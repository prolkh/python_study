from random import randint
import win32com.client


excel = win32com.client.Dispatch("Excel.Application")

wb = excel.Workbooks.Open(r'D:\python\magamsample.xlsx')
ws = wb.Worksheets('Sheet')
# ws.title = "BullSheet"


        
ws.Range('A1:A20').Sort(Key1=ws.Range('A1'), Order1=1, Orientation=1)
ws.Range('B1:B20').Sort(Key1=ws.Range('B1'), Order1=1, Orientation=1)
wb.Save()
excel.Application.Quit()

