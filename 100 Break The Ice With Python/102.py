s = 'Hello321Bye360'
print(f'Digit - {sum(1 for i in s if i.isdigit())}\nLetter - {sum(1 for i in s if i.isalpha())}')