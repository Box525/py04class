import xlrd

# 读取 指定的 Excel 文件 注意 文件后缀
wb = xlrd.open_workbook(r'./data.xls')

# 获取所有的 sheet 表(tables)
print(wb.sheet_names())

# 获取指定的表的名称
sheet1_name = wb.sheet_names()[0]
print(sheet1_name)

# 根据sheet 索引或者名称获取到 sheet 内容
#sheet1 = wb.sheet_by_index(0) # sheet的索引 是用0开始
sheet1 = wb.sheet_by_name('用户')

print(sheet1)
# sheet的名称 行数  列数
print(sheet1.name,sheet1.nrows,sheet1.ncols)

# 获取整行和整列的值
rows = sheet1.row_values(0)
print(rows)
print(rows[:2])
for line in range(sheet1.nrows):
    print(line,sheet1.row_values(line))
cols = sheet1.col_values(1)
print(cols)
# 获取单元格内容
print(sheet1.cell(0,1).value)
print(sheet1.cell(0,0).value.encode('utf-8'))
print(sheet1.cell_value(1,0))
print(sheet1.row(0)[0].value)

# 获取单元格内容的数据类型
# ctype 是用来判断当前单元格内容的数据类型
# 0 empty 1 string 2 number 3 date 4 boolean  5 error
print(sheet1.row(1)[0].ctype)
print(sheet1.row(1)[1].ctype)
print(sheet1.row(1)[2].ctype)

#

'''
姓名  性别  分数
s01  男    100

'''
'''
1.获取到当前 学生的成绩的最大值和最小值
2.遍历当前学生表中的每一行数据
3.声明 用来存放 最高成绩的学生的列表list 
可能学生 不止一个1个，每一个学生的信息都用字典来表示
4.对遍历的每一行中的 成绩 和 最高或者最低做 比较 符合条件 
就生产对应的字典（name sex scroe） 追加到对应的list中
'''
'''
max_score = 100
min_score = 10

total_rows = sheet1.nrows
max_list = []
min_list = []
for line in range(1,total_rows):
    row_content = sheet1.row_values(line)
    # score_value = row_content[2]
    if row_content[2] == max_score:
        user = {}
        user['name'] = row_content[0]
        user['sex'] = row_content[1]
        user['score'] = row_content[2]
        max_list.append(user)
    elif :
        pass
'''  
