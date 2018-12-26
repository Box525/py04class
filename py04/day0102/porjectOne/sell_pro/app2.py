import csv

with open('data.csv','w+',encoding="utf8",newline='')as c:
    writer_csv = csv.writer(c,dialect="excel")
    with open("ESKO_11.txt",encoding='utf8')as f:
        for line in f.readlines():
            line_list = line.strip('\n').split()
            print(line_list)