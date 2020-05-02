# function that gets us the information we need from piazza
def getPiazzaInfo(username, password):
	# get our api
	from piazza_api import Piazza
	import time

	# initalize piazza client
	p = Piazza()
	# login
	p.user_login(email = username,password = password)

	# get our class list
	classes = p.get_user_classes()

	# information for all classes
	classesInfo = []
	# iterate till we have one item per class in the list,
	# containing all needed elements for that class
	for c in classes:
		# individual class information
		classInfo = {}
		# set class name and number as per piazza
		classInfo['name'] = c['name']
		classInfo['number'] = c['num']
		# get url/nid of the class
		curClass = p.network(c['nid'])

		# get our iterator for the posts of that class
		posts = curClass.iter_all_posts(limit = 5)

		# store post info in here
		neededInfo = []

		# since piazza api has a speed limit,
		# we are enclosing the data in a try catch
		try:
			# iterate through posts
			for post in posts:
				# store post information in here
				postInfo = {}

				# set post subject and content
				postInfo['subject'] = post['history'][0]['subject']
				postInfo['content'] = post['history'][0]['content']

				# store followups information here
				postInfo['followUps'] = []

				# iterate through 'main' follow ups
				for mainFollowUp in post['children']:

					# if the follow up has a subject, then
					# it is valid
					if 'subject' in mainFollowUp:
						# store followup info here
						followUp = {}

						# set followup information
						followUp['mainComment'] = mainFollowUp['subject']

						# store and iterate through follow up responses
						followUp['subComments'] = []
						for subComment in mainFollowUp['children']:
							followUp['subComments'].append(subComment['subject'])

						# append followup to followups
						postInfo['followUps'].append(followUp)
				
				# append post to posts
				neededInfo.append(postInfo)

			# store posts information for a class
			classInfo['posts'] = neededInfo

			# add class information to our list
			classesInfo.append(classInfo)
		except:
			# if we tried too fast,
			# then there was an error
			print("piazza api trying too fast!")

	# return our object of class informations
	return classesInfo


