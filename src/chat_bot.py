import time
print("Hi, my name is Vincent.")
time.sleep(1)
print("What´s your name?")
user = input()
if user == "Joachim":
    print("Good morning my creator!")
else:
    print("Nice to meet you {}.".format(user))
time.sleep(1)