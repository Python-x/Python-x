list1 = ["魔术师1","魔术师2","魔术师3","魔术师4"]
def show_magicians(list):
	for i in list:
		print(i)
def make_great(list):
	for q in range(0,len(list)):
		list[q] = list[q]+"The Great"
	print(list)
show_magicians(list1)
make_great(list1)
