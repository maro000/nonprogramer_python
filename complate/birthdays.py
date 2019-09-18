birthdays = {'alive': '4/1', 'bob': '12/12', 'carol': '4/4'}

while True:
    print('Please enter your name')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(name + "'s birthday is" + birthdays[name])
    else:
        print(name + "'s birthdays is unregisted")
        print('please enter birthday')
        bday = input()
        birthdays[name] = bday
        print('birtdays update')
