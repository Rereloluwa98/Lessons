
# This code is for the cyclone roller coster ride requirements!

height = int(input("Whats your height in cm?"))
credits = int(input("How much credits do you have?"))

if height >= 137 and credits >= 10:
  print("Enjoy the ride!")
elif height < 137 and credits >= 10:
  print("get back shorty!")
elif height >= 137 and credits < 10:
  print("need more credits!")
else:
  print("Sorry, you have not met the requirements.")