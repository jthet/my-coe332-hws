import names

name_list = []
while len(name_list) < 5:  # Generate five names with exactly 8 characters (9 including space) 
    name = names.get_full_name()  
    if len(name) == 9:   # Check name length 
        name_list.append(name)   # Append valid name to list 

        
print("Five names that are exactly eight characters each:")    
for name in name_list:  # Print all the names in the list 
    print(name)