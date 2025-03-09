#Bugfixingexercise- Fix the created bugs

#Bugfixingexercise1 Prompt Below (SyntaxError: '[' was never closed)
    #answers = ['Yes', 'No', 'Yes', 'No', 'No'

#Solution
answers = ['Yes', 'No', 'Yes', 'No', 'No']
print(answers)

#Solution output
    #['Yes', 'No', 'Yes', 'No', 'No']

#Bug-Fixing Exercise 2 Prompt Below (SyntaxError: invalid syntax. Perhaps you forgot a comma?)
    #my_answer = input("What is your answer?")
    #answers = ['Yes', 'No', 'Yes' 'No' my_answer]

#Solution
my_answer1 = input("What is your answer?")
answers1 = ['Yes', 'No', 'Yes', 'No', my_answer1]
print(answers1)

#Solution output
    #['Yes', 'No', 'Yes', 'No', 'No']
    #What is your answer?13
    #['Yes', 'No', 'Yes', 'No', '13']
    #Process finished with exit code 0

#Bug-Fixing Exercise 3 Prompt Below (SyntaxError: invalid syntax. Perhaps you forgot a comma?)
    #my_answer2 = input(What is your answer?)
    #answers2 = ['Yes', 'No', 'Yes', 'No', my_answer2]

#Solution
my_answer2 = input("What is your answer?")
answers2 = ['Yes', 'No', 'Yes', 'No', my_answer2]
print(answers2)

#Solution output
    #['Yes', 'No', 'Yes', 'No', 'No']
    #What is your answer?13
    #['Yes', 'No', 'Yes', 'No', '13']
    #What is your answer?15
    #['Yes', 'No', 'Yes', 'No', '15']
    #Process finished with exit code 0

#Bug-Fixing Exercise 4 Prompt Below (TypeError: 'builtin_function_or_method' object is not subscriptable)
    #my_answer3 = input["What is your answer?"]
    #answers3 = ['Yes', 'No', 'Yes', 'No', my_answer3]

#Solution
my_answer3 = input("What is your answer?")
answers3 = ['Yes', 'No', 'Yes', 'No', my_answer3]
print(answers3)

#Solution output
    #['Yes', 'No', 'Yes', 'No', 'No']
    #What is your answer?13
    #['Yes', 'No', 'Yes', 'No', '13']
    #What is your answer?15
    #['Yes', 'No', 'Yes', 'No', '15']
    #What is your answer?17
    #['Yes', 'No', 'Yes', 'No', '17']
    #Process finished with exit code 0
