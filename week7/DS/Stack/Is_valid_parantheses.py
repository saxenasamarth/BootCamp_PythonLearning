#Check if valid Parentheses

def is_valid_parantheses(input_str):
	stack = []
	match_dict = {')':'(', '}':'{', ']':'['}
	for char in input_str:
		if char in ["(", "[", "{"]:
			stack.append(char)
		else:
			pop_char = stack.pop()
			if match_dict[char] != pop_char:
				return False		
	return len(stack)==0
		
print(is_valid_parantheses("()"))
print(is_valid_parantheses("()[]{}"))
print(is_valid_parantheses("(]"))		