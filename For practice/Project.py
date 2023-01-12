import random
CNumber = random.randrange(44,89)
user = int(input('Enter you number:-'))
if user > CNumber:
    print('Comnumber',CNumber)
    print("Your number is high")
elif CNumber < user:
    print("Your number too low")
else:
    print("Your number is equal")


