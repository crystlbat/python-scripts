import os
import openpyxl
import glob

file_list=glob.glob('C:/CALLS_TEMP/*.txt')
print(file_list)
filenames=[]
for file in file_list:
    filenames.append(os.path.basename(file).lstrip('Left_').lstrip('Right_'))
print(filenames)
org_filenames=[]
[org_filenames.append(file) for file in filenames if file not in org_filenames]
print(org_filenames)

def merger(filename):
    print(filename)
    wb = openpyxl.load_workbook(r'C:\CALLS_TEMP\transcripts.xlsx')
    wb.create_sheet(filename)
    path_right='C:/CALLS_TEMP/Right_'+filename
    path_left='C:/CALLS_TEMP/left_'+filename
    print(path_right,path_left)
    with open(path_right, 'r') as trans:
        lines_right=trans.readlines()
    print(lines_right)
    sheet=wb[filename]
    sheet["A1"].value="Agent"
    i=2
    for line in lines_right:
        sheet[f'A{i}'].value=line
        i+=1
    with open(path_left, 'r') as trans:
        lines_left=trans.readlines()
    sheet["B1"].value = "Customer"
    i = 2
    for line in lines_left:
        sheet[f'B{i}'].value = line
        i += 1
    wb.save(r'C:\CALLS_TEMP\transcripts.xlsx')

for file in org_filenames:
    merger(file)