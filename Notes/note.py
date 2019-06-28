from datetime import datetime
import pickle

class notes:
	counter =0
	note_list=[]
	
	def __init__(self, note):
		notes.counter+=1
		self.__id=notes.counter
		self.__note= note
		self.__create_time=datetime.now()
		self.__update_time=datetime.now()

	def save_state(func):
		def inner_func(*args,**kwargs):
			print("saving state")
			filer =open("notes.dump", "wb")
			pickle.dump(n, filer)
			filer.close
			value=func(*args, **kwargs)
			return value
		return inner_func


	def get_note(self):
		return self.__note

	def get_info(self):
		info_dict={}
		info_dict["id"]=self.__id
		info_dict["note"]=self.__note
		info_dict["create_time"]=self.__create_time
		info_dict["update_time"]=self.__update_time
		return info_dict

	
	def update_note(self,note):
		self.__note=note
		self.__update_time=datetime.now()
		

	def match_id(self,id):
		if self.__id==id:
			return True
		else:
			return False



		