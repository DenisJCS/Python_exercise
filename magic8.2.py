import random
name= ''
question= "Is it will of God that Esfir be my wife ?";
answers = [

"Yes definitely",
"It is decidedly so",
 "Without doubt",
 "Reply hazy, try again",
 "Ask again",
 "Better not tell you now",
 "My sources say no",
 "Outlook not so good",
 " Very doubtful",
 " If it is alsmost end , you will", 
 "Try harder",
 ]
answers = random.choice(answers)
if name == "":
  print("Question: " + question)
else:
  print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answers)





