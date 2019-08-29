from datetime import datetime
import pickle

#try:
#note_list=[]

class notes:
	counter =0
	
	
	#except:
	#	print("note list empty")
	#	note_list=[]
	

	
	def __init__(self, note):
		notes.counter+=1
		self.__id=notes.counter
		self.__note= note
		self.__create_time=datetime.now()
		self.__update_time=datetime.now()

	


	def get_note(self):
		return self.__note

	def get_info(self):
		info_dict={}
		info_dict["id"]=self.__id
		info_dict["note"]=self.__note
		info_dict["create_time"]=self.__create_time
		info_dict["update_time"]=self.__update_time
		return info_dict

	#@save_state
	def update_note(self,note):
		self.__note=note
		self.__update_time=datetime.now()
		

	def match_id(self,id):
		if self.__id==id:
			return True
		else:
			return False



		