a = ['max', 2, 'dol']
b = ['max', 2, 'pip', 77]
c = a + b
my_list = []
for i in c:
	if i not in my_list:
		my_list.append(i)
	else:
		pass

print(my_list)