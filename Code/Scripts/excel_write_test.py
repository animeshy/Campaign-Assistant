import xlwt

file_name = '1-jan-8-janTEST.xls'
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('test')
sheet.write(0,0,'test')
workbook.save(file_name)
