import numpy as np
import pandas as pd
import matplotlib as plt
#
# path = r'C:\Learning\pydata-book-master\ch02\names\yob1880.txt'
# table = pd.read_csv(path,names = ['name','sex','births'])
columns =  ['name','sex','births']
# print(table[:10])
pieces=[]
for i in range(1880,2010):
    path = r'C:\Learning\pydata-book-master\ch02\names\yob%d.txt' %i
    # print(path)
    data = pd.read_csv(path,names=columns)
    data['year']=i
    pieces.append(data)

# print(pieces[:10])
names = pd.concat(pieces,ignore_index=True)
# print(names[:-10])

get_last_letter=lambda x:x[-1]
last_letters  = names.name.map(get_last_letter)
last_letters.name='last_letter'
# print(last_letters[:10])
table = names.pivot_table('births',index = last_letters,columns=['sex','year'],aggfunc=sum)
# print(table[:10])
sub_table = table.reindex(columns=[1910,1960,2009],level='year')
print(sub_table.head())
sub_table_sum = sub_table.sum()
print(sub_table_sum)
let_prop = sub_table/sub_table_sum.astype(float)
print(let_prop.head())
print(108376.0/396416.0)