from piazza_api import Piazza

p = Piazza()
p.user_login(email = "usert4363@gmail.com",password = "cs494Awesome")

user_profile = p.get_user_profile()

print(p.get_user_classes())

ts100 = p.network("k7aywdror8n4o0")

posts = ts100.iter_all_posts(limit=5)

for post in posts:
	print(str(post))