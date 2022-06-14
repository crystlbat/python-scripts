import openpyxl
from openpyxl.worksheet.hyperlink.Hyperlink import Hyperlink

workbook=r'C:\output mock hit\HIT CHECK REPOSITORY.xlsx'
wb=openpyxl.load_workbook(workbook)
sheets=wb.sheetnames
print(sheets)
sheet=wb['List']

link = f'{workbook}-Sheet1!A2'
sheet.hyperlink.Hyperlink(ref='List!A1', location='Sheet1!A1',display="hmmm")



wb.save(r'C:\output mock hit\HIT CHECK REPOSITORY.xlsx')
