__author__ = "Akhil Gupta" 


'''
	This script is used to normalize the score of the same reviews
	occuring multiple times in a data set.
'''


import json

class NormalizeScore():

	def __init__(self):
		
		self.without_score = open("data_without_score_test.json").readlines()
		self.with_score = open("data.json").readlines()
		self.error_log = open("error_log.json","a")
		self.count = 1
	
	def _indexdata(self,dic):
		
		with open('sanitized_data_test.json', 'a') as fp:
			json.dump(dic,fp)
			fp.write('\n')

	def normalizingScore(self):

		count = self.count 
		for row  in self.without_score:
			print count
			# dws is data_with_score
			# dwts is data_witout_score
			dwts =  json.loads(row)			
			large = 5.1
			sum_of_score = 0
			records_count =0
			
			for record in self.with_score:
				dws = json.loads(record)
				
				try :

					if dwts["review"] == dws["review"]:
						dws_score = eval(dws["score"])						
						if dws_score<large:
							records_count+=1
							sum_of_score+=dws_score
							large = dws_score
																
				except Exception as e:
					print "Exception ::", e
					self.error_log.write(str(dws)+"###"+str(dwts)+"\n")
					
			avg = sum_of_score/records_count					
			dwts["score"] = avg		
			count+=1
			self._indexdata(dwts)

normalizescore = NormalizeScore()
normalizescore.normalizingScore()