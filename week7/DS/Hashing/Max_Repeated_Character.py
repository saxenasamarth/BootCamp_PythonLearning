def get_max_occuring(input_str):
	store_dict = {}
	for char in input_str:
		if char in store_dict:
			store_dict[char]+=1
		else:
			store_dict[char] = 1
	max_char = ""
	max_count = 0
	for char in store_dict:
		if store_dict[char] > max_count:
			max_char = char
			max_count = store_dict[char]
	return max_char

print(get_max_occuring("Hello World"))	