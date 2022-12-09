print("Welcome to my video game quiz!")

print("Enter 'x' to start. Enter 'o' to exit program.")
start = input("Are you ready to start? ")
score = 0 

if start.lower() != "x":
  quit()

print("Let the games begin!")
print("What was the best selling video game in December of 2017?")
print("A-COD WW2\tB-Fifa 18\tC-Assassins Creed Origins")
answer = input("Select an answer: ")
if answer.upper() == "A":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

print("Which character isn't apart of the Mortal Kombat franchise?")
print("A-Noob Saibot\tB-D'Vorah\tC-Chun-Li")
answer = input("Select an answer: ")
if answer.upper() == "C":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

print("What is special about Ellie in The Last of Us franchise?")
print("A-Telekinesis\tB-Immune to Infection 18\tC-Immortality")
answer = input("Select an answer: ")

if answer.upper() == "B":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

print("Who said the infamous quote 'All we had to do was follow the damn train CJ!'in GTA San Andreas?")
print("A-Big Smoke\tB-Sweet 18\tC-Ryder")
answer = input("Select an answer: ")
if answer.upper() == "A":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

print("Which company developed the Outlast franchise?")
print("A-Capcom\tB-Red Barrels 18\tC-Ubisoft")
answer = input("Select an answer: ")
if answer.upper() == "B":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

print("You answered " + str(score) + " questions correct!" )
print("Your overall score is " + str((score/5) * 100) + "%.")
  
  
  


  


  