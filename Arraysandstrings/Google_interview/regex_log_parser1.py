#Program to print and get the sort thread for the processes in the 
import re
import collections

document_text = open('/Users/deep/Desktop/github/datastructures_python/Arraysandstrings/Google_interview/test3_1.txt', 'r')
text_string = document_text.read().split('\n')
#print text_string
match_pattern = re.compile(r'^\w+\s(\w)\s\w+\s(\d)')

frequency = collections.defaultdict(list)

#frequency = collections.defaultdict(int)
for line in text_string:
	match_output = match_pattern.search(line)
 	#print match_output 
	key, value = match_output.groups()
	print key, value
	if key in frequency:
		frequency[key].append(value)
	else:
		frequency[key] = [value]


for key, value in frequency.iteritems():
	#print key, value
	
	sort_list = all(value[i] <= value[i+1] for i in xrange(len(value)-1)) 
	if sort_list:
		print 'Threads are in sync'
	else:
		print 'Threads are not in sync'