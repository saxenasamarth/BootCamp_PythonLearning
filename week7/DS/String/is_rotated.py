# Check if a string is rotated version of other

def is_rotated(str1, str2):
	new_str = str2+str2
	return str1 in new_str
	
print(is_rotated("hello", "llohe"))
print(is_rotated("hello", "llheo"))	