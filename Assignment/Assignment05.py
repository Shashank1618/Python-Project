#get(key, default): This method returns the value for a specified key. If the key is not found, it returns the default value (or None if not provided).

my_dict = {'name': 'Alice', 'age': 25}
print(my_dict.get('name')) 
print(my_dict.get('gender', 'Not specified')) 


#items(): This method returns a view object that displays a list of dictionary's key-value tuple pairs.

my_dict = {'name': 'Alice', 'age': 25}
print(my_dict.items()) 


