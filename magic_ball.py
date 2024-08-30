import random
name = ""
question = input()
answers = [
    "Yes ",
    "No",
    "Try again",
    "100 %",
    "Better not tell you now",
    "My sources say no",
    "Outlook not so good",
    " Very doubtful",
    " If it is alsmost end , you will", 
    "Try harder",
]
answers = random.choice(answers)
while question == "":
    question = input("Please enter a question (or type 'q' to quit): ")
    if question.lower() == "q":
        print("Goodbye!")
        break
if question.lower() != "q":
    if name == "":
        print("Question"+ question)
    else:
        print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answers)
