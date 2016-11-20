import json
from collections import Counter
import pandas as pd
from pandas import DataFrame,Series
from matplotlib import pyplot as plt
import numpy as np;

path = r'C:\Learning\pydata-book-master\ch02\usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]
print(records[0])
frame = DataFrame(records)

#print(frame['tz'][:10])
#print(frame.columns())
tz_counts = frame['tz'].value_counts()
#print(tz_counts)

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz=='']='Missing'
#print(clean_tz.value_counts()[:10])

tz_counts = clean_tz.value_counts()[:10]
tz_counts.plot(kind='barh')
#plt.show()

results =Series([x.split()[0] for x in frame.a.dropna()])
#print(results[:10])
# print(frame.a.notnull)

cframe =frame[frame.a.notnull()]
# print("CFrame:%n")
# print(cframe['tz'][:10])
# print("cframe counts:")
# print(len(cframe))
os = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
by_tz_os = cframe.groupby(['tz',os])
cout = by_tz_os.size().unstack().fillna(0)
print(cout)
indexer= cout.sum(1).argsort()
print(indexer)
