dict = [
    {
    'first_name': "deep",
    'last_name': "sutaria",
    'age': 10},
    {'first_name': "vruddhi",
    'last_name': "sutaria",
    'age': 10},
    {'first_name': "nita",
    'last_name': "vora",
    'age': 10}
       ]

filter={
   'last_name': "sutaria"
    }
    

output = []
for key, value in filter.items():
    for each in dict:
         if each[key] == value:
            output.append(each) 
print output
            
#[{'first_name': 'deep', 'last_name': 'sutaria', 'age': 10}, 
# {'first_name': 'vruddhi', 'last_name': 'sutaria', 'age': 10}]