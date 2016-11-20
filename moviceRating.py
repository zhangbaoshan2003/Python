import pandas as pd

unames = ['user_id','gender','age','occupation','zip']
users = pd.read_table(r'C:\Learning\pydata-book-master\ch02\movielens\users.dat',sep='::',header = None,names = unames)

rnames = ['user_id','movie_id','rating','timestamp']
ratings = pd.read_table(r'C:\Learning\pydata-book-master\ch02\movielens\ratings.dat',sep="::",header=None,names=rnames)

mnames = ['movie_id','title','genres']
movies = pd.read_table(r'C:\Learning\pydata-book-master\ch02\movielens\movies.dat',sep="::",header=None,names=mnames)

# print(users[:10])
# print(ratings[:10])
# print(movies[:10])

merge1 = pd.merge(ratings,users,on='user_id')
data = pd.merge(merge1,movies,on='movie_id')
# print(data[:10])
check = data[data.title=='eXistenZ (1999)']
# print(check)

mean_ratings = data.pivot_table('rating',index='title',columns='gender',aggfunc='mean')
# print(mean_ratings[:10])
rating_title = data.groupby('title').size()
# print(type(rating_title))
active_title = rating_title.index[rating_title>=500]

mean_ratings = mean_ratings.ix[active_title]
# print(mean_ratings)

top_mean_ratings = mean_ratings.sort_index(by='F',ascending=False)
# print(top_mean_ratings)
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_diff = mean_ratings.sort_index(by='diff')
# print(sorted_diff[:10])
# print(sorted_diff[::-1][:10])

#stand deviation fo rating group by title
rating_std_by_title = data.groupby('title').rating.std()
rating_std_by_title =rating_std_by_title.ix[active_title]
print(rating_std_by_title.order(ascending=False)[:10])
#[mean_ratings.title=='Dumb & Dumber (1994)']
