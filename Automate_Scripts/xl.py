import openpyxl, os

os.chdir('c:\\users\\wandroid\\documents')


book=openpyxl.load_workbook('promedio.xlsx')
print(book['Hoja1']['A1'].value )
sheet_one=book['Hoja1']
sheet_one['A1']=4012

libro=openpyxl.Workbook()
hoja=libro['Sheet']['A1']=20
libro.save('sample.xlsx')
