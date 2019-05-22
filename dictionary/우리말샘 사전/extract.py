import xlrd
import openpyxl
import os


wb = openpyxl.Workbook()
ws = wb.active
row_index = 1


file_list = os.listdir('./')

for file in file_list:
    if '.py' not in file:

        workbook = xlrd.open_workbook(file)
        worksheet = workbook.sheet_by_index(0)
        nrows = worksheet.nrows

        for i in range(nrows):
            j = worksheet.row_values(i)
            if len(j[6]) != 0:
                for k in range(len(j)):
                    ws.cell(row=row_index, column=k+1, value=j[k])
                row_index += 1


wb.save("./dict.xlsx")
wb.close()
