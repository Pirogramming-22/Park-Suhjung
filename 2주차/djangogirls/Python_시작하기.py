2 + 3
2 ** 3
"Ola"
"Hi there " + "Ola"
"Ola" * 3
"Runnin' down the hill"
'Runnin\' down the hill'
"Ola".upper()
len("Ola")
len(str(304023))
name = "Ola"
name
name = "Sonja"
name
len(name)
a = 4
b = 6
a * b
city = "Tokyo"
city

'Maria'
print(name)
Maria
lottery = [3, 42, 12, 19, 30, 59]
len(lottery)
lottery.sort()
print(lottery)
lottery.reverse()
print(lottery)
print(lottery[1])
print(lottery)
[59, 42, 30, 19, 12, 3, 199]
lottery.pop(0)
print(lottery)
[42, 30, 19, 12, 3, 199]


participant = {'name': 'Ola', 'country': 'Poland', 'favorite_numbers': [7, 42, 92]}
print(participant['name'])
participant['favorite_language'] = 'Python'
len(participant)
participant.pop('favorite_numbers')
participant['country'] = 'Germany'
print('Hello, Django girls!')

if 3 > 2:
    print('It works!')

if 5 > 2:
    print('5 is indeed greater than 2')
else:
    print('5 is not greater than 2')


name = 'Sonja'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Sonja':
    print('Hey Sonja!')
else:
    print('Hey anonymous!')

volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")



if volume < 20 or volume > 80:
    volume = 50
    print("That's better!")


def hi():
    print('Hi there!')
    print('How are you?')

hi()


def hi(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')

hi()


hi("Ola")

def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')

for i in range(1, 6):
    print(i)