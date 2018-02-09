#!/usr/bin/python
#coding:utf-8
import xlrd
import xlwt
import os
from datetime import date,datetime
 
os.chdir("assets/")
way = os.getcwd()
print (way)

def read_excel(sheetname):
  workbook = xlrd.open_workbook(sheetname)
  sheetName = workbook.sheet_names()[0]
  print (sheetName)

  # 由索引和名字获取表
  sheetIndex = workbook.sheet_by_index(0)
  sheetByName = workbook.sheet_by_name(sheetName)  
  
  # sheet的名称，行数，列数  
  print (sheetIndex.name,sheetIndex.nrows,sheetIndex.ncols)

  # 获取整行和整列的值（数组）  
  rows = sheetIndex.row_values(3) # 获取第四行内容  
  cols = sheetIndex.col_values(2) # 获取第三列内容  
  print (rows)
  print (cols)
  
  # 获取单元格内容  
  print (sheetIndex.cell(1,0).value.encode('utf-8'))
  print (sheetIndex.cell_value(1,0).encode('utf-8'))
  print (sheetIndex.row(1)[0].value.encode('utf-8'))
    
  # 获取单元格内容的数据类型  
  print (sheetIndex.cell(1,0).ctype)

read_excel('sheet.xlsx')