import instaloader

L = instaloader.Instaloader()

acc = 'radioqaum'
L.interactive_login(acc)

from itertools import islice
from math import ceil

from instaloader import Instaloader, Profile


X_percentage = 10 # percentage of posts that should be downloaded


profile = Profile.from_username(L.context, acc)
posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda p: p.likes + p.comments, reverse=True)
print(posts_sorted_by_likes)

X = ceil(profile.mediacount * X_percentage / 100)
print(X)
#print(islice(posts_sorted_by_likes,X))

#for post in list(islice(posts_sorted_by_likes,X)):
#     print(post)

#     L.download_post(post, acc)
top_X=[]
for i in range(X):
    #print('+++++++++++++++')
    top_X.append(posts_sorted_by_likes[i])
    #print(posts_sorted_by_likes[i])
print(top_X)
    #L.download_post(posts_sorted_by_likes[i],acc)
for post in top_X:
    L.download_post(post, acc)

print("done")