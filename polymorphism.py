class Panda(object):
   def isMammal(self):
       return True
        
class Penguin(object):
   def isMammal(self):
       return False        
panda = Panda()
penguin = Penguin()
def check_animal(obj):
   print(obj.isMammal())    
    
print(check_animal(panda))
print(check_animal(penguin))