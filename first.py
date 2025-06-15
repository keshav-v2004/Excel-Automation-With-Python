import openpyxl as xl

wb = xl.load_workbook('transactions.xlsx') #load the entire excel file and return a sheet object
sheet = wb['Sheet1'] # load the first sheet

cell = sheet["A1"] # value of cell gets loaded
print(cell.value)
