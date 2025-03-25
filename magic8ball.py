import random
random_number = random.randint(0,8)
question = input("Ask away...")


if random_number == 1:
  print("Yes - definitely.")
elif random_number == 2:
  print("It is decidedly so.")
elif random_number == 3:
  print("Without a doubt.")
elif random_number == 4:
  print("Reply hazy, try again.")
elif random_number == 5:
  print("ask again later.")
elif random_number == 6:
  print("Better not tell now.")
elif random_number == 7:
  print("My sources say no.")
elif random_number == 8:
  print("Very doubtful.")
else:
  print("Outlook not so good.")
