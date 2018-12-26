import xlwt

# 创建一个Excel 写对象
wb = xlwt.Workbook()
# 给指定的Excel 对象添加一个 sheet
shee1 = wb.add_sheet('用户信息')

# 给指定的 sheet 写入数据
# write(行,列,内容)
shee1.write(0, 0, '姓名')
shee1.write(0, 1, '年龄')
shee1.write(1,0,'张三')
shee1.write(1,1,'18')

# 保存文件 切记如果已存在文件则是覆盖
wb.save('./data2.xls')
