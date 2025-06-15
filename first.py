import openpyxl as xl

wb = xl.load_workbook('transactions.xlsx') #load the entire excel file and return a sheet object
sheet = wb['Sheet1'] # load the first sheet

cell = sheet["A1"] # value of cell gets loaded
print(cell.value)
print()

print(sheet.max_row) ## returns the maximum number of rows in the sheet (also includes the header i.e row names)

print()
for eachRow in range(2,sheet.max_row+1):

    print(sheet.cell(eachRow,3).value)
    # we want third column (index=3) of every row

