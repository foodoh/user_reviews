__author__ = "Akhil Gupta"

'''
	This script is used to remove the same reviews in data set.

	Note : To generate "data.json"	 which contains score of each review 
	uncomment "score = data['score']" line and in "_indexingRefinedData()"
	replace "data_without_score.json" with "data.json"
'''



import ast
import json

class ReviewRefine():
	
	def __init__(self):
		
		self.fileobj = open("reviews.txt","r").readlines()		
		self.temp_list=[]
		self.count = 1
	
	def _indexingRefinedData(self,final_list):
	 	
	 	count = self.count
		for i in final_list:
			print count
			data = i.split("###")
			dic ={}
			# print data
			dic["hotel_id"] = data[0]
			dic["review"] = data[1]
			dic["title"] = data[2]

			with open('data_without_score.json', 'a') as fp:
				json.dump(dic,fp)
				fp.write('\n')
			count+=1
	
	def refiningReview(self):
		
		fileobj = self.fileobj
		li = self.temp_list
		for row in fileobj:
			data = ast.literal_eval(row)
			ide = data['hotel']
			rev = data['review']
			title = data['title']

			# score = data['score']
			final_review = ide+"###"+rev+"###"+title+"###"
			li.append(final_review)
		print len(li)
		# removed all duplicated reviews.
		final_list = list(set(li))
		print len(final_list)
		self._indexingRefinedData(final_list)

reviewrefine = ReviewRefine()
reviewrefine.refiningReview()	