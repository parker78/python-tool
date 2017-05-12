# -*- encoding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import openpyxl as px
doc=px.load_workbook('dnynbiao.xlsx',use_iterators=True)
names=doc.get_sheet_names()
sheet=doc.get_sheet_by_name(names[0])
rows=sheet.iter_rows()
header=[]
for row in rows:
    for k in range(0,len(row)):
        header.append(row[k].value)
    break
#data=[]
#for row in rows:
#    for k in range(0,len(row)):
#        data.append(row[k].value)
#    break
#print header
#print data
'''
插入原型
insert table_name(a,b,c) values (a1,b1,c1)
'''

#插入头处理
insert_head='insert into '
insert_table_name='ftmetricanalysis0'
#insert_table_name='tbzbcs0'
insert_col='('
i=0
for sstr in header:
    if 0!=i:
        insert_col=insert_col+','
    i=i+1
    insert_col=insert_col+str(sstr)
insert_col=insert_col+') values '
insert_str=''
j=0
for row in rows:
    i=0;
   #j=0;
    if 0!=j:
        insert_str=insert_str+','
    j=j+1
    insert_str=insert_str+'('
    for k in range(0,len(row)):
        if 0!=i :
            insert_str=insert_str+','
        i=i+1;
        insert_str=insert_str+str(row[k].value)
    insert_str=insert_str+')'
    if 2==j:
        break
print insert_head+insert_table_name+insert_col+insert_str
