import instaloader

L = instaloader.Instaloader()

f = open('input.txt','r')
accounts = f.read()
p = accounts.split('\n')

PROFILE = p[:]
print(PROFILE)

for ind in range(len(PROFILE)):
    pro = PROFILE[ind]
    profile = instaloader.Profile.from_username(L.context, pro)
    main_followers = profile.followers
    posts = profile.mediacount
    id = profile.userid
    print(id)
    print(main_followers)
    print(posts)
    print(profile.is_verified)
    print('\n')