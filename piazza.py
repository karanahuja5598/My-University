# from piazza_api import Piazza

# p = Piazza()
# p.user_login(email = "usert4363@gmail.com",password = "cs494Awesome")

# user_profile = p.get_user_profile()

# print(p.get_user_classes())

# get a list of user classes
# classes = p.get_user_classes()

# ts100 = p.network("k7aywdror8n4o0")

# access the first class from that list
# class1 = p.network(classes[0]['nid'])

# posts = class1.iter_all_posts(limit=5)

# for post in posts:
# 	print(str(post))

# post1 = posts.__next__()

def getPiazzaInfo(username, password):
	from piazza_api import Piazza
	p = Piazza()
	p.user_login(email = username,password = password)
	classes = p.get_user_classes()
	class1 = p.network(classes[0]['nid'])
	posts = class1.iter_all_posts(limit=5)
	neededInfo = []
	for post in posts:
		postInfo = {}
		postInfo['subject'] = post['history'][0]['subject']
		postInfo['content'] = post['history'][0]['content']
		postInfo['followUps'] = []
		for mainFollowUp in post['children']:
			followUp = {}
			followUp['mainComment'] = mainFollowUp['subject']
			followUp['subComments'] = []
			for subComment in mainFollowUp['children']:
				followUp['subComments'].append(subComment['subject'])
			postInfo['followUps'].append(followUp)
		neededInfo.append(postInfo)
	return neededInfo

# for post in neededInfo:
# 	print('Post Title: {0}'.format(post['subject']))
# 	print('Post Content: {0}'.format(post['content']))
# 	print('Follow Up Discussions: ')
# 	for followUp in post['followUps']:
# 		print('    {0}'.format(followUp['mainComment']))
# 		for subComment in followUp:
# 			print('        {0}'.format(subComment))


