import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

path = r'C:\Learning\pydata-book-master\ch02\names\yob1880.txt'
names1880 = pd.read_csv(path,names=['name','sex','births'])
# print(names1880.sort('births',ascending=True))
group_by_sex = names1880.groupby('sex').births.sum()
# print(group_by_sex)
#conact all of years firls
years = range(1880,2011)
pieces = []
columns = ['name','sex','births']

for year in years:
    path =  r'C:\Learning\pydata-book-master\ch02\names\yob%d.txt' % year
    frame=pd.read_csv(path,names=columns)
    frame['year']=year
    # print(type(frame))
    pieces.append(frame)
names = pd.concat(pieces,ignore_index=True)
# print(names[:10])
total_birth_by_year = pd.pivot_table(names,index='year',columns='sex',aggfunc='sum')
# print(total_birth_by_year)

def add_prop(group):
    births = group.births.astype(float)
    group['prop'] = births/group.births.sum()
    return group

names = names.groupby(['sex','year']).apply(add_prop).sort('prop',ascending=False)
# print(names_prop[:10])

close = np.allclose(names.groupby(['sex','year']).prop.sum(),1)
print(close)

def get_top1000(group):
    grouped = group.sort_index(by='births',ascending=False)
    return grouped[:1000]

top1000 = names.groupby(['sex','year']).apply(get_top1000)
# print(top100)
pieces = []
for year,grp in names.groupby(['sex','year']):
    newGrp = grp.sort_index(by='births',ascending=False)[:10]
    pieces.append(newGrp)

top1000 = pd.concat(pieces,ignore_index=True)

# print(top100)
boys= top1000[top1000.sex=='M']
girls = top1000[top1000.sex=='F']

total_births = top1000.pivot_table('births',index = 'year',columns='name',aggfunc=sum).fillna(0)
sub_total = total_births[['John','Harry','Mary']]
# print(sub_total)

# sub_total.plot(subplots=True,figsize=(12,10),grid=False,title='Num of birth per year')
# plt.show()

table = top1000.pivot_table('prop',index='year',columns='sex',aggfunc=sum).fillna(0)
table.plot(title='sum of table1000 by year and sex',yticks = np.linspace(0,1.2,13),xticks = range(1880,2020,10))
# plt.show()

# df = boys[boys.year==2010]
# print(df)
# print(df.prop.cumsum())

def get_qutial_def(group,q=0.5):
    group = group.sort_index(by='prop',ascending=False)
    return group.prop.cumsum().searchsorted(q)+1

diversity = top1000.groupby(['year','sex']).apply(get_qutial_def)
# diversity = diversity.unstack('sex')
print(diversity.head(10))

diversity = diversity.unstack('sex')
print(diversity.head(10))