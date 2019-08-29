#
#import sys
#sys.path.insert(0,'/home/samarth/pythonProgs/Projects/projpkg')
import projpkg.pkg1.f1 as f1

def inputLastname():
	lname=input("Enter last name: ")
	return lname

fname =f1.inputfirstname()
lname= inputLastname()
print("{} {}". format(fname,lname))

