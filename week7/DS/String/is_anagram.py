# Check if two strings are anagrams

def is_anagram(str1, str2):
	store_dict = {}
	for c in str1:
		if c in store_dict:
			store_dict[c]+=1
		else:
			store_dict[c]=1
	for c in str2:
		if c not in store_dict or store_dict[c]==0:
			return False
		else:
			store_dict[c]-=1
	return set(store_dict.values()) == {0}
	
def is_anagram_xor(str1, str2):
	val = ord(str1[0])
	for char in str1[1:]:
		val = val^ord(char)
	for char in str2:
		val = val^ord(char)
	return val==0
	
print(is_anagram("good mrng", "mrng good"))
print(is_anagram("good", "mrng good"))
print(is_anagram_xor("good mrng", "mrng good"))
print(is_anagram_xor("good", "mrng good"))	