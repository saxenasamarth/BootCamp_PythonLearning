from pymongo import MongoClient

client=MongoClient()
db=client["MiniAmazon"]


def uname_exists(uname_val):
	if db.users.find_one({"username":uname_val})!=None:
		return True
	else:
		return False


def createUser(userProfile_dict):
	db.users.insert(userProfile_dict)


