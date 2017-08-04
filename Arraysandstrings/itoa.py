#http://www.geeksforgeeks.org/implement-itoa/
def convert_to_string(num, base=10):
	if num == 0:
		return '0'


	if num < 0 and base == 10:
		num = -num

	elif num // base == 0:
		return chr(num + ord('0'))

	return convert_to_string(num // base, base) + chr(num % base + ord('0'))

print convert_to_string(1567,10)
print convert_to_string(-1567,10)
print convert_to_string(1567,2)
print convert_to_string(1567,8)
#print convert_to_string(1567,16) #Hexadecimal