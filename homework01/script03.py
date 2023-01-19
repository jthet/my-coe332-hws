import names
# Creates name list
name_list = []
for i in range(5):
    name_list.append(names.get_full_name())

#finds the length of the name without the spaces
def name_length(name):
	return len(name.replace(" ", ""))

#prints the name and then length
for name in name_list:
	print(f"{name} {name_length(name)}")

