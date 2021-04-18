first = 'Immanuel'
last = 'Prasad'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
course = 'Python for Beginners'
print(message)
print(msg)

print('Upper : ' + message.upper())
print('Lower : ' + message.lower())
print('Find : ' + str(course.find("B")))
print('Replace : ' + message.replace('a', 'A'))
print('Title : ' + message.title())
print("Boolean : " + 'is' in message)
