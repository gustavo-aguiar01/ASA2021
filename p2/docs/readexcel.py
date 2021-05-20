import xlrd

loc = ("al024-testsheet.xls")
f = open("times.dat", "a")
f.write("n k V E V+E VE T \n")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

k = 1
for i in range(1, sheet.nrows):
    f.write(str(int(sheet.cell_value(k, 1))) + " " + str(int(sheet.cell_value(k, 2))) + " " + 
    str(int(sheet.cell_value(k, 3))) + " " + str(int(sheet.cell_value(k, 4))) + " " + str(int(sheet.cell_value(k, 5)))
    + " " + str(int(sheet.cell_value(k, 8))) + " " + str(int(sheet.cell_value(k, 7))) + "\n")
    k += 1

f.close()