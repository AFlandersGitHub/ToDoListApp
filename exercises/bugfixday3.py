#BugFixingExercise1BAD
'''for i in buttons:
    print(i.capitalize())

buttons = ["cancel", "reply", "submit"]'''

#BugFixingExercise1GOOD
buttons = ['cancel', 'reply', 'submit']

for i in buttons:
    i = i.capitalize()
    print(i)

#BugFixingExercise2BAD
'''buttons = ["cancel", "reply", "submit"]

for i in buttons:
    print(i.capitalize())'''

#BugFixingExercise2GOOD
buttons = ["cancel", "reply", "submit"]

for i in buttons:
    print(i.capitalize())

#BugFixingExercise3BAD
'''for item in ["sandals", "glasses", "trousers"):
    print(item.capitalize)'''

#BugFixingExercise3GOOD
for item in ["sandals", "glasses", "trousers"]:
    print(item.capitalize())