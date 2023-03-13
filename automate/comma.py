def comma(my_list):
	my_list.insert(-1, 'and')
	return my_list

spam = ['apples', 'bananas', 'tofu', 'cats']
scores = [23, 34, 55, 67, 88, 90, 78, 162, 179]
print(comma(spam))
print(comma(scores))
