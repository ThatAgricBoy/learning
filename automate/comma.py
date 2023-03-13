def comma(my_list):
	my_list.insert(3, 'and')
	return my_list

spam = ['apples', 'bananas', 'tofu', 'cats']
my_list = spam
print(comma(my_list))
