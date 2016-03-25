__author__ = "Akhil Gupta"

'''
	This script id to make the inverted index of the review with respect
	to hotel_id 
'''

import json
import pymongo

class IndexToMongo():
	
	def __init__(self):	

		self.client = pymongo.MongoClient()
		self.db= self.client['foodoh']
	
	def index(self):

		with open("sanitised_data.json") as f:
			ct =1
			for line in f:
				print ct 
				data = json.loads(line)			
				ide = data["hotel_id"]
				self.db.reviews.update({"hotel_id":ide},{"$addToSet":{"reviews":data}},True)
				ct +=1

indextomongo = IndexToMongo()
indextomongo.index()