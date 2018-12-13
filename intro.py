message = 'Hello World'

print(message[2])
print(message.lower())
print(message.upper())
print(message.count('e'))


print(message.find('World'))
new_message= message.replace('World','Universe')
print(new_message)

greeting = 'Hello'
name = 'Jibin'

message = '{} , {}'.format(greeting,name)
mes1 = f'{greeting} , {name.upper()} ! Welcome'
print(message)
print(mes1)